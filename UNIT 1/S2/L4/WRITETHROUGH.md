# Perimepy 📐 - Calcolatore di Perimetri Geometrici

Benvenuto su **Perimepy**, un semplice programma interattivo in Python che ti permette di calcolare il perimetro di diverse figure geometriche. In questa documentazione troverai una spiegazione dettagliata di ogni parte del codice per comprendere appieno il funzionamento del programma.

## Indice

1. [Introduzione](#introduzione)
2. [Funzionalità del Programma](#funzionalità-del-programma)
3. [Installazione e Requisiti](#installazione-e-requisiti)
4. [Struttura del Codice](#struttura-del-codice)
   - [Funzione Principale](#funzione-principale)
   - [Richiesta di Input all'Utente](#richiesta-di-input-allutente)
   - [Calcolo del Perimetro](#calcolo-del-perimetro)
5. [Esecuzione del Programma](#esecuzione-del-programma)
6. [Note Finali](#note-finali)

---

## Introduzione

**Perimepy** è un programma che utilizza l'input dell'utente per calcolare il perimetro di tre figure geometriche: il **quadrato**, il **cerchio** e il **rettangolo**. È pensato per essere intuitivo e interattivo, ideale per chi sta imparando Python e vuole esercitarsi con la gestione dell'input utente e le funzioni matematiche di base.

## Funzionalità del Programma

- **Scelta della Figura Geometrica**: L'utente può scegliere tra tre figure geometriche: quadrato, cerchio o rettangolo.
- **Gestione degli Errori di Input**: Il programma verifica la validità dei dati inseriti dall'utente e gestisce eventuali errori.
- **Supporto per Virgole e Punti**: Accetta separatori decimali sia con virgola che con punto, rendendo l'inserimento dei dati più flessibile.

## Installazione e Requisiti

Assicurarsi di avere **Python 3.x** installato.

### Installazione

Nessuna installazione di pacchetti aggiuntivi è necessaria; il programma utilizza solo librerie standard di Python.

## Struttura del Codice

### Funzione Principale

```python
def calcola_perimetro():
    # Chiediamo all'utente quale figura vuole calcolare
    scelta = input("\nBenvenuto in Geompy!\n\n📐 Scegli una figura geometrica per calcolare il perimetro:\n1. Quadrato\n2. Cerchio\n3. Rettangolo\n\nInserisci il numero della figura che desideri (1-3): ")
    if scelta not in ["1", "2", "3"]:
        # Se la scelta non è valida, avvisiamo l'utente e richiamiamo la funzione per riprovare
        print("\nErrore: Numero non valido. Riprova.")
        return calcola_perimetro()
```

La funzione principale **`calcola_perimetro()`** inizia chiedendo all'utente quale figura geometrica vuole calcolare. Se l'input non è valido, il programma lo informa e ripete la richiesta.

### Richiesta di Input all'Utente

```python
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
```

La funzione interna **`richiedi_valore()`** permette di gestire l'input dell'utente, assicurandosi che venga fornito un valore numerico valido. Se l'utente inserisce un valore non valido, viene richiesto di riprovare.

### Calcolo del Perimetro

```python
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
```

In base alla scelta dell'utente, il programma calcola il perimetro del quadrato, del cerchio o del rettangolo. Il risultato viene poi visualizzato sullo schermo.

## Esecuzione del Programma

1. **Avvio del Programma**: Esegui il file `perimetro.py` con Python 3.
2. **Scelta della Figura**: Scegli tra quadrato, cerchio o rettangolo.
3. **Inserimento dei Dati**: Inserisci le dimensioni richieste, utilizzando punto o virgola come separatore decimale.
4. **Visualizzazione del Risultato**: Il perimetro viene calcolato e mostrato immediatamente.

## Note Finali

Questo programma è stato progettato per dimostrare come si possano costruire semplici applicazioni interattive con Python, migliorando la gestione degli errori di input e fornendo un'esperienza utente coinvolgente.

---

Con questa documentazione aggiornata, **Geompy** dovrebbe essere chiaro e facile da usare. Buon calcolo dei perimetri!
