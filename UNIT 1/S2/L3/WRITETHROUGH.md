# Namebander 🎸

Benvenuto su **Namebander**, un semplice programma interattivo in Python che ti aiuterà a creare un nome per la tua band usando la città di provenienza e il nome del tuo animale domestico. Attraverso questa documentazione, troverai una spiegazione dettagliata di ogni parte del codice per comprendere appieno come funziona il programma.

## Indice

1. [Introduzione](#introduzione)
2. [Funzionalità del Programma](#funzionalità-del-programma)
3. [Installazione e Requisiti](#installazione-e-requisiti)
4. [Struttura del Codice](#struttura-del-codice)
   - [Importazioni e Librerie](#importazioni-e-librerie)
   - [Benvenuto all'Utente](#benvenuto-allutente)
   - [Funzione di Verifica per la Città](#funzione-di-verifica-per-la-città)
   - [Funzione di Verifica per il Nome dell'Animale](#funzione-di-verifica-per-il-nome-dellanimale)
   - [Richiesta di Input all'Utente](#richiesta-di-input-allutente)
   - [Animazione di Caricamento](#animazione-di-caricamento)
   - [Generazione del Nome della Band](#generazione-del-nome-della-band)
5. [Esecuzione del Programma](#esecuzione-del-programma)
6. [Note Finali](#note-finali)

---

## Introduzione

**Namebander** è un programma di esempio che utilizza l'input dell'utente per generare il nome di una band. La scelta del nome si basa sulla città di provenienza dell'utente e sul nome del suo animale domestico, combinando i due input con un tocco di creatività.

## Funzionalità del Programma

- Verifica dell’input dell'utente per garantire che il nome della città e dell'animale non contengano numeri.
- Simulazione di un’animazione di caricamento per migliorare l’esperienza utente.
- Generazione e visualizzazione del nome della band.

## Installazione e Requisiti

Assicurarsi di avere **Python 3.x** installato.

### Installazione

Nessuna installazione di pacchetti aggiuntivi è necessaria; il programma utilizza solo la libreria **time**, inclusa in Python.

## Struttura del Codice

### Importazioni e Librerie

```python
import time
```

- **`import time`**: La libreria `time` è usata per creare ritardi (con `time.sleep()`), che simulano un’animazione di caricamento e aggiungono attesa prima del risultato finale.

### Benvenuto all'Utente

```python
print("\nCiao! Benvenuto su Namebander! 🎸")
```

- Questo messaggio iniziale di benvenuto introduce l'utente al programma e stabilisce un tono amichevole e musicale.

### Funzione di Verifica per la Città

```python
def input_citta(testo):
    while True:
        valore = input(testo)
        if any(char.isdigit() for char in valore):
            print("Solo io che sono un programma vengo dalla città 00110100 00110010")
        else:
            return valore
```

- **`def input_citta(testo)`**: Funzione che verifica che l'input dell'utente per la città non contenga numeri.
  - Utilizza un **loop `while`** per assicurarsi che l'utente reinserisca l'input finché questo non è valido.
  - La condizione **`if any(char.isdigit() for char in valore)`** controlla se ci sono cifre nel testo inserito.
  - Se l’input contiene numeri, viene mostrato un messaggio umoristico, e l’utente deve reinserire il valore.

### Funzione di Verifica per il Nome dell'Animale

```python
def input_animale(testo):
    while True:
        valore = input(testo)
        if any(char.isdigit() for char in valore):
            print("Elon Musk sei tu!?")
        else:
            return valore
```

- **`def input_animale(testo)`**: Simile alla funzione precedente, ma per il nome dell’animale domestico.
  - Verifica che l’input non contenga cifre.
  - In caso di input non valido, mostra un messaggio che invita l’utente a riprovare.

### Richiesta di Input all'Utente

```python
citta_origine = input_citta("\nPrima di tutto, dimmi, da quale città vieni? ")
nome_animale = input_animale("\nPerfetto! Ora, qual è il nome del tuo adorato animale domestico? ")
```

- Queste righe raccolgono gli input dell'utente per la **città** e per il **nome dell'animale domestico**, utilizzando le funzioni precedenti che filtrano i dati per ottenere valori coerenti e validi.

### Animazione di Caricamento

```python
print("\nGenerazione del nome della band in corso...")
barra_lunghezza = 30
for i in range(barra_lunghezza + 1):
    time.sleep(0.1)
    barra = '[' + '#' * i + ' ' * (barra_lunghezza - i) + ']'
    percentuale = int((i / barra_lunghezza) * 100)
    print(f"\r{barra} {percentuale}%", end="", flush=True)
```

- **Animazione di Caricamento**:
  - Dopo aver ricevuto gli input, viene visualizzata una barra di avanzamento che simula un processo di caricamento.
  - **`time.sleep(0.1)`**: Crea un ritardo di 0.1 secondi ad ogni iterazione per rallentare il caricamento, rendendolo visibile.
  - La barra è aggiornata progressivamente ad ogni ciclo del `for`, usando `#` per indicare l’avanzamento e una percentuale che si aggiorna per mostrare il completamento.

### Generazione del Nome della Band

```python
time.sleep(1)
nome_band = citta_origine + " " + nome_animale
```

- Dopo l’animazione, viene aggiunto un breve **ritardo finale** con `time.sleep(1)` per creare attesa.
- Il nome della band è quindi generato unendo il nome della città e dell'animale, con uno spazio tra i due termini.

### Stampa del Risultato

```python
print("\n\nFantastico!")
print("Il nome della tua band sarà:", nome_band)
```

- Viene mostrato il risultato finale con il nome della band creato.

## Esecuzione del Programma

1. Avviare il programma.
2. Inserire la città di provenienza e assicurarsi di non includere numeri.
3. Inserire il nome dell'animale domestico, evitando numeri.
4. Attendere l'animazione di caricamento.
5. Vedere il nome della band generato!

## Note Finali

Questo programma è stato progettato per mostrare come un'interfaccia utente semplice e interattiva possa migliorare l'esperienza generale, pur mantenendo il codice di facile comprensione e manutenzione.

---

Con questa documentazione, speriamo che il programma **Namebander** sia chiaro e divertente da esplorare. Buona generazione del nome della band!
