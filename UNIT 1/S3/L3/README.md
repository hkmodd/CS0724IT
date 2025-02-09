
# Consegna S3/L3 ✉️ - 🛡️ Cifrario di Cesare: Cripta e Decripta Messaggi 🕵️‍♂️

## 📜 Descrizione
Benvenuto nel **cifratore un tanto al chilo**! 🥳 Questo programma permette di **criptare** o **decriptare** un messaggio utilizzando il famoso **Cifrario di Cesare**, un metodo di crittografia semplice ma efficace.

✨ **Funzionalità principali:**
1. **Criptare** un messaggio specificando uno shift scelto da te.
2. **Decriptare** un messaggio già cifrato utilizzando un attacco brute force che prova tutti gli shift possibili, con alfabeto ITALIANO (21 lettere).

---

### 📝 Esercizio richiesto
L'esercizio richiesto era:

> Dato un messaggio cifrato cercare di trovare il testo in chiaro:  
> Messaggio cifrato: "HSNFRGH"  

Il messaggio più probabile si trova usando **Shift 3** ed è **EPICODE**.

---

## ⚙️ Come funziona?

### 🔒 **Crittografia**
Il Cifrario di Cesare sposta ogni lettera del messaggio originale (testo in chiaro) di un numero fisso di posizioni nell'alfabeto.

### 🔑 **Decrittografia**
Per decifrare, il programma:
1. **Tenta tutti gli shift possibili**
2. Mostra il risultato per ogni shift in modo da poter identificare il testo originale.

---

## 🚀 Come usare il programma

1. **Esegui il programma**:
   ```bash
   python PraticaS1L3.py
   ```

2. **Scegli un'opzione**:
   - **1** per criptare un messaggio.
   - **2** per decriptare un messaggio.

3. **Inserisci il tuo messaggio**:
   - Per la crittografia, specifica il messaggio e lo shift desiderato (un numero tra 1 e 25).
   - Per la decrittografia, inserisci il messaggio cifrato e lascia che il programma provi tutti gli shift.

---

## 🔧 Dettagli tecnici

### 📂 Struttura del codice
- **`encrypt_caesar(plaintext, shift)`**:
  Funzione per criptare un messaggio dato uno shift.
- **`decrypt_caesar(ciphertext, shift)`**:
  Funzione per decifrare un messaggio dato uno shift.
- **`brute_force_caesar(ciphertext)`**:
  Prova tutti gli shift possibili per decriptare un messaggio.
- **`main()`**:
  Gestisce l'interazione con l'utente e l'esecuzione delle operazioni.

### 🛠️ Strumenti usati
- **Python 3**: Linguaggio di programmazione.
- **Stringhe**: Per manipolare i caratteri e gestire gli shift nell'alfabeto.

### ✍️ Note importanti
- Il programma accetta solo **lettere maiuscole**.
- Gli spazi e i caratteri speciali vengono ignorati.

---