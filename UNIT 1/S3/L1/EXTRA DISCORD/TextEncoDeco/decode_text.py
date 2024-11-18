# decode_text.py

import os
import hashlib
from getpass import getpass
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox

def decode_text():
    def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        file_path_entry.delete(0, "end")
        file_path_entry.insert(0, file_path)

    def decode():
        input_file = file_path_entry.get()
        password = password_entry.get()

        if not input_file:
            messagebox.showerror("Errore", "Devi selezionare un file da decodificare.")
            return

        try:
            # Calcola un hash della password per generare una chiave di decifratura
            password_hash = hashlib.sha256(password.encode()).hexdigest() if password else None

            # Legge il testo codificato
            with open(input_file, 'r', encoding='utf-8') as f:
                encoded_text = f.read()

            # Estrai la sequenza di spazi (singoli e doppi)
            binary_message = ''
            i = 0
            while i < len(encoded_text):
                if encoded_text[i] == ' ':
                    if i + 1 < len(encoded_text) and encoded_text[i + 1] == ' ':
                        binary_message += '1'  # Due spazi rappresentano '1'
                        i += 2  # Salta il secondo spazio
                    else:
                        binary_message += '0'  # Un solo spazio rappresenta '0'
                        i += 1
                else:
                    i += 1

            # Decifra il messaggio binario utilizzando la password hash
            if password_hash:
                decrypted_message = ''.join([str(int(b) ^ int(password_hash[i % len(password_hash)], 16) % 2) for i, b in enumerate(binary_message)])
            else:
                decrypted_message = binary_message

            # Decodifica il messaggio binario in testo
            message = ''
            for i in range(0, len(decrypted_message), 8):
                byte = decrypted_message[i:i+8]
                if len(byte) == 8:  # Assicurati di avere byte completi
                    message += chr(int(byte, 2))

            messagebox.showinfo("Messaggio Decodificato", message)

        except FileNotFoundError:
            messagebox.showerror("Errore", "Il file specificato non è stato trovato.")
        except ValueError:
            messagebox.showerror("Errore", "Password errata o file non valido.")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante la decodifica: {e}")

    root = Tk()
    root.title("Decodifica Messaggio Nascosto")

    Label(root, text="Password per la decodifica (lascia vuoto se non presente):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    password_entry = Entry(root, show="*")
    password_entry.grid(row=0, column=1, padx=10, pady=5)

    Label(root, text="Seleziona il file da decodificare:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    file_path_entry = Entry(root, width=40)
    file_path_entry.grid(row=1, column=1, padx=10, pady=5)

    browse_button = Button(root, text="Sfoglia", command=open_file)
    browse_button.grid(row=1, column=2, padx=5, pady=5)

    decode_button = Button(root, text="Decodifica ora!", command=decode)
    decode_button.grid(row=2, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    decode_text()
