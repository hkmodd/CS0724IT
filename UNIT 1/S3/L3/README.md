
# 🛡️ Cifrario di Cesare: Cripta e Decripta Messaggi 🕵️‍♂️

## 📜 Descrizione
Benvenuto nel **cifratore un tanto al chilo**! 🥳 Questo programma permette di **criptare** o **decriptare** un messaggio utilizzando il famoso **Cifrario di Cesare**, un metodo di crittografia semplice ma efficace.

✨ **Funzionalità principali:**
1. **Criptare** un messaggio specificando uno shift scelto da te.
2. **Decriptare** un messaggio già cifrato utilizzando un attacco brute force che prova tutti gli shift possibili.

---

### 📝 Esercizio richiesto
L'esercizio richiesto era:

> Dato un messaggio cifrato cercare di trovare il testo in chiaro:  
> Messaggio cifrato: "HSNFRGH"  

Il messaggio più probabile si trova usando **Shift 3** ed è **EPKCODE**.

---

## ⚙️ Come funziona?

### 🔒 **Crittografia**
Il Cifrario di Cesare sposta ogni lettera del messaggio originale (testo in chiaro) di un numero fisso di posizioni nell'alfabeto. Ad esempio:
- Se il testo in chiaro è `CIAO` e lo shift è `3`, il messaggio cifrato sarà `FLDR`.

### 🔑 **Decrittografia**
Per decifrare, il programma:
1. **Tenta tutti gli shift possibili** (da 1 a 25).
2. Mostra il risultato per ogni shift in modo da poter identificare il testo originale.

---

## 🚀 Come usare il programma

1. **Esegui il programma**:
   ```bash
   python nome_del_file.py
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

### 🛠️ Tecnologie usate
- **Python 3**: Linguaggio di programmazione.
- **Stringhe**: Per manipolare i caratteri e gestire gli shift nell'alfabeto.

### ✍️ Note importanti
- Il programma accetta solo **lettere maiuscole**.
- Gli spazi e i caratteri speciali vengono ignorati.

---

## 📈 Esempi d'uso

### 🔒 Criptare
```
Scegli un'operazione:
1: Criptare un messaggio
2: Decriptare un messaggio
Inserisci 1 o 2: 1

Inserisci il messaggio da criptare (solo lettere altrimenti ti cancello il sistema): CIAO
Inserisci lo shift (1-25): 3

Messaggio criptato: FLDR
```

### 🔓 Decriptare
```
Scegli un'operazione:
1: Criptare un messaggio
2: Decriptare un messaggio
Inserisci 1 o 2: 2

Inserisci il messaggio cifrato (solo lettere, non farmi incazzare): FLDR

Sto decifrando il messaggio...
Shift 1: EKCQ
Shift 2: DJBP
Shift 3: CIAO
Shift 4: BHZN
...
```

---
