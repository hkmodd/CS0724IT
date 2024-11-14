# Funzione principale per calcolare il perimetro di diverse figure geometriche
# Questa funzione permette all'utente di scegliere tra quadrato, cerchio e rettangolo,
# e successivamente calcola il perimetro in base ai dati forniti dall'utente.
def calcola_perimetro():
    # Chiediamo all'utente quale figura vuole calcolare
    scelta = input("\nBenvenuto in Geompy!\n\n📐 Scegli una figura geometrica per calcolare il perimetro:\n1. Quadrato\n2. Cerchio\n3. Rettangolo\n\nInserisci il numero della figura che desideri (1-3): ")
    if scelta not in ["1", "2", "3"]:
        # Se la scelta non è valida, avvisiamo l'utente e richiamiamo la funzione per riprovare
        print("\nErrore: Numero non valido. Riprova.")
        return calcola_perimetro()

    # Definiamo una funzione interna per richiedere valori numerici all'utente
    # Questa funzione gestisce errori di input e consente l'uso della virgola come decimale
    def richiedi_valore(messaggio):
        while True:
            try:
                valore = input(messaggio).replace(',', '.')  # Convertiamo la virgola in punto per accettare entrambi
                return float(valore)
            except ValueError:
                # Se l'utente inserisce un valore non numerico, ripetiamo la richiesta
                print("\nCos'è? Un'equazione? Riprova inserendo un numero.")

    # Calcolo del perimetro per il quadrato
    if scelta == "1":
        lato = richiedi_valore("Lunghezza lato quadrato (cm): ")
        print(f"\nIl perimetro del quadrato è: {lato * 4} cm")
    # Calcolo del perimetro per il cerchio
    elif scelta == "2":
        raggio = richiedi_valore("Raggio del cerchio (cm): ")
        print(f"\nLa circonferenza del cerchio è: {2 * 3.1416 * raggio:.2f} cm")
    # Calcolo del perimetro per il rettangolo
    elif scelta == "3":
        base = richiedi_valore("Lunghezza base rettangolo (cm): ")
        altezza = richiedi_valore("Altezza rettangolo (cm): ")
        print(f"\nIl perimetro del rettangolo è: {2 * (base + altezza)} cm")

# Chiamata alla funzione per iniziare il calcolo
calcola_perimetro()
