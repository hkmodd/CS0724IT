import time

# Start
print("\nCiao! Benvenuto su Namebander! 🎸")

# Funzione per verificare se l'input dell'utente per città contiene numeri
def input_citta(testo):
    while True:
        valore = input(testo)
        if any(char.isdigit() for char in valore):
            print("Solo io che sono un programma vengo dalla città 00110100 00110010")
        else:
            return valore

# Funzione per verificare se l'input dell'utente per animali contiene numeri
def input_animale(testo):
    while True:
        valore = input(testo)
        if any(char.isdigit() for char in valore):
            print("Elon Musk sei tu!?")
        else:
            return valore

# Richiesta di input all'utente
citta_origine = input_citta("\nPrima di tutto, dimmi, da quale città vieni? ")
nome_animale = input_animale("\nPerfetto! Ora, qual è il nome del tuo adorato animale domestico? ")

# Animazione di caricamento
print("\nGenerazione del nome della band in corso...")
barra_lunghezza = 30
for i in range(barra_lunghezza + 1):
    time.sleep(0.1)
    barra = '[' + '#' * i + ' ' * (barra_lunghezza - i) + ']'
    percentuale = int((i / barra_lunghezza) * 100)
    print(f"\r{barra} {percentuale}%", end="", flush=True)

# Delay prima della stampa finale del risultato
time.sleep(1)

# Combinazione dei due nomi per formare il risultato
nome_band = citta_origine + " " + nome_animale

# Stampa del risultato
print("\n\nFantastico!")
print("Il nome della tua band sarà:", nome_band)
