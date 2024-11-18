# encode_text.py
import os
import hashlib
from getpass import getpass

def generate_cover_text(required_spaces, corpus_file):
    with open(corpus_file, 'r', encoding='utf-8') as f:
        words = f.read().split()

    cover_text = ''
    total_spaces = 0
    index = 0

    while total_spaces < required_spaces and index < len(words):
        cover_text += words[index] + ' '
        total_spaces += 1
        index += 1

    if total_spaces < required_spaces:
        raise ValueError("❌ Non è stato possibile generare il testo di copertura richiesto.")

    return cover_text.strip()

def encode_text():
    try:
        # Richiedi il messaggio da nascondere
        message = input("Inserisci il messaggio da nascondere: ")

        # Richiedi una password per la protezione
        password = getpass("Inserisci una password per la cifratura (lascia vuoto per non usare una password): ")

        # Se la password è vuota, si lascia il messaggio in chiaro, altrimenti si cifra
        if password:
            # Calcola un hash della password per generare una chiave di cifratura
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            # Codifica il messaggio in binario
            binary_message = ''.join([format(ord(i), '08b') for i in message])

            # Cifra il messaggio binario utilizzando la password hash
            encrypted_message = ''.join([str(int(b) ^ int(password_hash[i % len(password_hash)], 16) % 2) for i, b in enumerate(binary_message)])
        else:
            # Codifica il messaggio in binario senza cifratura
            encrypted_message = ''.join([format(ord(i), '08b') for i in message])

        # Calcola il numero di spazi necessari
        required_spaces = len(encrypted_message)

        # Percorso del file del corpus italiano
        corpus_file = "processed_corpus.txt"

        # Genera il testo di copertura
        cover_text = generate_cover_text(required_spaces, corpus_file)

        # Inserisce gli spazi per rappresentare il messaggio cifrato nel testo di copertura
        encoded_text = ''
        index = 0
        for char in cover_text:
            if char == ' ' and index < len(encrypted_message):
                if encrypted_message[index] == '1':
                    encoded_text += '  '  # Due spazi per '1'
                else:
                    encoded_text += ' '   # Uno spazio per '0'
                index += 1
            else:
                encoded_text += char

        # Assicurati che tutti i bit siano stati codificati
        if index < len(encrypted_message):
            remaining_bits = encrypted_message[index:]
            for bit in remaining_bits:
                if bit == '1':
                    encoded_text += '  '
                else:
                    encoded_text += ' '

        # Salva il file automaticamente
        output_filename = "output_encodato.txt"
        current_directory = os.getcwd()
        output_path = os.path.join(current_directory, output_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(encoded_text)
        print(f"\n💾 Testo codificato salvato automaticamente in '{output_path}'.")

    except Exception as e:
        print(f"❌ Errore durante la codifica: {e}")

if __name__ == "__main__":
    encode_text()
