# Consegna S2/L2 ✉️

Benvenuti nel repository dedicato agli esercizi di programmazione in linguaggio C. Questo progetto include un paio di semplici programmi per calcolare la **moltiplicazione** e la **media aritmetica** di due numeri inseriti dall'utente. Ideale per chi sta muovendo i primi passi con il linguaggio C!

---

## 📋 Descrizione degli Esercizi

### 1️⃣ Moltiplicazione tra Due Numeri

- **Descrizione**: Questo programma chiede all'utente di inserire due numeri interi e visualizza il risultato della loro moltiplicazione.
- **File**: [`moltiplicazione.c`](./moltiplicazione.c)

### 2️⃣ Media Aritmetica tra Due Numeri

- **Descrizione**: Questo programma calcola la media aritmetica di due numeri inseriti dall'utente.
- **File**: [`media.c`](./media.c)

---

## 🚀 Compilazione ed Esecuzione su Linux

### 🛠️ Requisiti

- **Compilatore GCC**: installato seguendo il docente da istruzioni:

  ```bash
  sudo apt update
  sudo apt install gcc
  ```

---

### Compilazione

Per compilare i file `.c`, basta utilizzare `gcc`, il compilatore GNU per C, come segue:

```bash
gcc moltiplicazione.c -o moltiplicazione
gcc media.c -o media
```

### Esecuzione

Una volta compilati, i programmi possono essere eseguiti con:

```bash
./moltiplicazione
./media
```

> **Nota**: Su sistemi Linux, non è necessario aggiungere un'estensione (come `.exe`) agli eseguibili. Per convenzione, i file eseguibili su Linux possono essere eseguiti direttamente senza un'estensione, utilizzando `./nomefile`.

---

## 📂 Struttura 

```plaintext
.
├── bin                  # Cartella binaries compilati
├── file di prova        # Cartella esercitazioni della teoria con docente
├── README.md            # Documentazione del progetto
├── moltiplicazione.c    # Codice sorgente per la moltiplicazione
└── media.c              # Codice sorgente per la media aritmetica
```

---

## 📝 Note per il Docente

Questo progetto è stato realizzato seguendo le **best practice per i sistemi Linux**, dove non è necessario aggiungere un'estensione ai file eseguibili per poterli eseguire. Ho scelto di non aggiungere un'estensione al file binario per mantenere la conformità con gli standard Linux e rendere l'esecuzione più semplice e intuitiva.

---

