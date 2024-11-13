import time

# Funzione per interpretare la risposta come "sì" o "no"
def interpreta_risposta(risposta):
    risposta = risposta.strip().lower()
    parole_si = ["sì", "si", "ye", "yep", "yeah", "sure", "certamente", "ovvio", "ok", "s", "affirmativo"]
    parole_no = ["no", "nah", "nop", "n", "non", "mai", "niente"]

    for parola in parole_si:
        if parola == risposta:
            return "sì"

    for parola in parole_no:
        if parola == risposta:
            return "no"

    return None

# Funzione per chiedere l'età e gestire errori e tentativi
def chiedi_eta():
    tentativi = 0
    while tentativi < 3:
        eta_input = input("Inserisci la tua età (solo numeri): ").strip()
        if eta_input.isdigit():
            return int(eta_input)  # Se è un numero, convertilo e restituiscilo
        else:
            tentativi += 1
            print("Errore: Devi scrivere un numero valido!")
    
    # Se l'utente sbaglia 3 volte, mostra l'animazione del teschio
    animazione_teschio()
    return None

# Animazione del teschio che "esplode" (testuale)
def animazione_teschio():
    teschio = [
        "      _____ ",
        "    /     \\ ",
        "   | () () |",
        "    \\  ^  /",
        "     |||||",
        "     |||||",
    ]
    esplosione = [
        "   💥💥💥💥💥",
        "  💥       💥",
        " 💥   💥   💥",
        "💥         💥",
        "  💥     💥",
        "    💥💥",
    ]

    for linea in teschio:
        print(linea)
        time.sleep(0.5)
    time.sleep(1)
    
    for linea in esplosione:
        print(linea)
        time.sleep(0.5)

# Funzione per chiedere se l'utente è uno studente
def chiedi_se_studente():
    tentativi = 0
    while tentativi < 3:
        risposta = input("Sei uno studente? (sì/no): ")
        studente = interpreta_risposta(risposta)
        if studente is not None:
            return studente
        else:
            tentativi += 1
            print("Risposta non riconosciuta. Per favore, rispondi con 'sì' o 'no'.")

    # Dopo 3 tentativi falliti, entra in loop infinito
    while True:
        print("OOOOOO SMETTILAAAA!!")
        time.sleep(0.5)

# Programma principale
eta = chiedi_eta()
if eta is None:
    print("Hai superato il numero massimo di tentativi. Riprova più tardi!")
else:
    studente = chiedi_se_studente()

    if eta < 12:
        prezzo = 5
    elif 12 <= eta < 18:
        prezzo = 7
    elif 18 <= eta <= 65:
        prezzo = 10
    else:
        prezzo = 6

    if studente == "sì" and eta < 26:
        prezzo -= 2

    print(f"Il prezzo del biglietto è: {prezzo}€")
