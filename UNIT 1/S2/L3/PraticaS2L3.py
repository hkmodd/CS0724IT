# Saluto iniziale
print("\nCiao! Benvenuto al generatore di nomi per band! 🎸")

# Funzione per verificare se l'input della città contiene numeri
def input_citta(testo):
    while True:
        valore = input(testo)
        if any(char.isdigit() for char in valore):
            print("Solo io che sono un programma vengo dalla città 00110100 00110010")
        else:
            return valore

# Funzione per verificare se l'input del nome dell'animale domestico contiene numeri
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

# Generazione del nome della band
nome_band = citta_origine + " " + nome_animale

# Stampa del risultato
print("\nFantastico!")
print("Il nome della tua band sarà:", nome_band)

