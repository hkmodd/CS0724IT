
import base64
import binascii
import codecs
import re
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd


def detect_encoding(data):
    """
    Rileva se il dato fornito è codificato e suggerisce la codifica probabile.
    """
    try:
        # Test Base64
        base64.b64decode(data, validate=True)
        return "Base64"
    except Exception:
        pass

    try:
        # Test Base58 (controlla caratteri validi per Base58)
        if re.match("^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]+$", data):
            return "Base58"
    except Exception:
        pass

    try:
        # Test Hexadecimal
        binascii.unhexlify(data)
        return "Hexadecimal"
    except Exception:
        pass

    try:
        # Test URL encoding
        if re.match(r"%[0-9a-fA-F]{2}", data):
            return "URL-encoded"
    except Exception:
        pass

    return "Unknown"


def decode_data(data, encoding):
    """
    Decodifica i dati in base al tipo di encoding rilevato.
    """
    try:
        if encoding == "Base64":
            return base64.b64decode(data).decode("utf-8", errors="ignore")
        elif encoding == "Base58":
            # Base58 decoding (manuale per semplicità)
            alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
            base58_map = {char: index for index, char in enumerate(alphabet)}
            decoded = 0
            for char in data:
                decoded = decoded * 58 + base58_map[char]
            return decoded.to_bytes((decoded.bit_length() + 7) // 8, 'big').decode("utf-8", errors="ignore")
        elif encoding == "Hexadecimal":
            return binascii.unhexlify(data).decode("utf-8", errors="ignore")
        elif encoding == "URL-encoded":
            return codecs.decode(data, "url")
        else:
            return "Unsupported encoding"
    except Exception as e:
        return f"Decoding failed: {str(e)}"


def analyze_input():
    """
    Analizza il testo inserito dall'utente e aggiorna la tabella con i risultati.
    """
    input_data = input_text.get("1.0", "end").strip()
    if not input_data:
        messagebox.showwarning("Input mancante", "Inserisci un testo da analizzare!")
        return

    detected_encoding = detect_encoding(input_data)
    decoded_result = decode_data(input_data, detected_encoding)

    table.insert("", "end", values=(input_data, detected_encoding, decoded_result))


# Creazione della GUI con Tkinter
root = tk.Tk()
root.title("Rilevatore e Decodificatore di Dati Offuscati")

# Frame superiore
top_frame = ttk.Frame(root, padding=10)
top_frame.grid(row=0, column=0, sticky="ew")

ttk.Label(top_frame, text="Inserisci il testo da analizzare:", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
input_text = tk.Text(top_frame, width=60, height=5)
input_text.grid(row=1, column=0, sticky="ew", pady=5)

analyze_button = ttk.Button(top_frame, text="Analizza", command=analyze_input)
analyze_button.grid(row=2, column=0, sticky="e")

# Frame per la tabella
table_frame = ttk.Frame(root, padding=10)
table_frame.grid(row=1, column=0, sticky="nsew")

ttk.Label(table_frame, text="Risultati:", font=("Arial", 12)).grid(row=0, column=0, sticky="w")

# Tabella
columns = ("Input", "Detected Encoding", "Decoded Data")
table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=200)

table.grid(row=1, column=0, sticky="nsew")

# Scrollbar per la tabella
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=1, column=1, sticky="ns")

# Configurazione della finestra
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# Esecuzione della GUI
root.mainloop()
