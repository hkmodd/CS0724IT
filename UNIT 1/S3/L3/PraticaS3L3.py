import string

def encrypt_caesar(plaintext, shift):
    # Alfabeto italiano (senza J, K, W, X, Y)
    alphabet = "ABCDEFGHILMNOPQRSTUVZ"
    encrypted = ""
    for char in plaintext:
        if char in alphabet:
            index = (alphabet.index(char) + shift) % len(alphabet)
            encrypted += alphabet[index]
        else:
            encrypted += char
    return encrypted

def decrypt_caesar(ciphertext, shift):
    # Alfabeto italiano (senza J, K, W, X, Y)
    alphabet = "ABCDEFGHILMNOPQRSTUVZ"
    decrypted = ""
    for char in ciphertext:
        if char in alphabet:
            index = (alphabet.index(char) - shift) % len(alphabet)
            decrypted += alphabet[index]
        else:
            decrypted += char
    return decrypted

def brute_force_caesar(ciphertext):
    # Alfabeto italiano (senza J, K, W, X, Y)
    alphabet = "ABCDEFGHILMNOPQRSTUVZ"
    results = []
    for shift in range(1, len(alphabet)):
        decrypted = decrypt_caesar(ciphertext, shift)
        results.append((shift, decrypted))
    return results

def main():
    print("\nBenvenuto nel cifratore italiano! 🇮🇹")
    print("\nScegli un'operazione:")
    print("\n1: Criptare un messaggio")
    print("\n2: Decriptare un messaggio")
    choice = input("\nInserisci 1 o 2: ").strip()
    
    if choice == "1":
        plaintext = input("\nInserisci il messaggio da criptare (solo lettere dell'alfabeto italiano): ").upper().replace(" ", "")
        shift = int(input("\nInserisci lo shift (1-20): "))
        encrypted = encrypt_caesar(plaintext, shift)
        print(f"\nMessaggio criptato: {encrypted}")
    
    elif choice == "2":
        ciphertext = input("\nInserisci il messaggio cifrato (solo lettere dell'alfabeto italiano): ").upper().replace(" ", "")
        print("\nSto decifrando il messaggio...")
        results = brute_force_caesar(ciphertext)
        for shift, text in results:
            print(f"Shift {shift}: {text}")
    
    else:
        print("\nOperazione non valida. Riprova!")

if __name__ == "__main__":
    main()