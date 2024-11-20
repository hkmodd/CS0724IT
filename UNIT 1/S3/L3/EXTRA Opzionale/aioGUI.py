import tkinter as tk
from tkinter import messagebox, simpledialog
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
import base64

# Carica la chiave privata
def load_private_key():
    with open('private_key.pem', 'rb') as key_file:
        return serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )

# Carica la chiave pubblica
def load_public_key():
    with open('public_key.pem', 'rb') as key_file:
        return serialization.load_pem_public_key(key_file.read())

# Crittografia
def encrypt_message(public_key, message):
    return public_key.encrypt(
        message.encode(),
        padding.PKCS1v15()
    )

# Decrittografia
def decrypt_message(private_key, encrypted_message):
    return private_key.decrypt(
        encrypted_message,
        padding.PKCS1v15()
    )

# Firma
def sign_message(private_key, message):
    return private_key.sign(
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )

# Verifica firma
def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

# Funzioni GUI
def encrypt_gui():
    public_key = load_public_key()
    message = simpledialog.askstring("Crittografia", "Inserisci il messaggio da cifrare:")
    if message:
        encrypted = encrypt_message(public_key, message)
        encrypted_base64 = base64.b64encode(encrypted).decode('utf-8')
        messagebox.showinfo("Messaggio Cifrato", f"Cifrato (Base64): {encrypted_base64}")

def decrypt_gui():
    private_key = load_private_key()
    encrypted_message = simpledialog.askstring("Decriptazione", "Inserisci il messaggio cifrato (Base64):")
    if encrypted_message:
        try:
            decrypted = decrypt_message(private_key, base64.b64decode(encrypted_message))
            messagebox.showinfo("Messaggio Decriptato", f"Decriptato: {decrypted.decode('utf-8')}")
        except Exception:
            messagebox.showerror("Errore", "Decriptazione fallita. Verifica il messaggio cifrato.")

def sign_gui():
    private_key = load_private_key()
    message = simpledialog.askstring("Firma", "Inserisci il messaggio da firmare:")
    if message:
        signature = sign_message(private_key, message)
        signature_base64 = base64.b64encode(signature).decode('utf-8')
        messagebox.showinfo("Firma", f"Firma generata (Base64): {signature_base64}")

def verify_gui():
    public_key = load_public_key()
    message = simpledialog.askstring("Verifica", "Inserisci il messaggio originale:")
    signature = simpledialog.askstring("Verifica", "Inserisci la firma (Base64):")
    if message and signature:
        is_valid = verify_signature(public_key, message, base64.b64decode(signature))
        if is_valid:
            messagebox.showinfo("Verifica", "La firma è valida.")
        else:
            messagebox.showerror("Verifica", "La firma NON è valida.")

# Creazione della GUI
def main():
    root = tk.Tk()
    root.title("Crypto Tool 2024")
    root.geometry("400x300")

    # Stile moderno
    tk.Label(root, text="Crypto Tool 2024", font=("Helvetica", 16, "bold")).pack(pady=10)

    tk.Button(root, text="Cifra un messaggio", command=encrypt_gui, width=25, height=2, bg="#4CAF50", fg="white").pack(pady=5)
    tk.Button(root, text="Decifra un messaggio", command=decrypt_gui, width=25, height=2, bg="#2196F3", fg="white").pack(pady=5)
    tk.Button(root, text="Firma un messaggio", command=sign_gui, width=25, height=2, bg="#FFC107", fg="black").pack(pady=5)
    tk.Button(root, text="Verifica una firma", command=verify_gui, width=25, height=2, bg="#F44336", fg="white").pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
