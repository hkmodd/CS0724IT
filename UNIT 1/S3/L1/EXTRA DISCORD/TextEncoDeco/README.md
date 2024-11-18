# TextEncoDeco - Python 🕵️‍♂️

Benvenuti nella guida completa alla steganografia testuale con cifrazione mediante password! Questo progetto è stato ideato e sviluppato da me con l'obiettivo di nascondere informazioni in testi apparentemente innocui, utilizzando una tecnica semplice ma efficace. 💡

---

## 🔍 Obiettivi del progetto
1. **Steganografia testuale**: Nascondere messaggi all'interno di un testo di copertura generato casualmente.
2. **Sicurezza aggiuntiva**: Utilizzo di una password per proteggere il messaggio codificato.
3. **Facilità d'uso**: Permettere a chiunque di inviare e ricevere messaggi nascosti in formato `.txt`.

---

## 📂 Struttura del progetto

### File inclusi:
- **`encode_text.py`**: Script per codificare un messaggio.
- **`decode_text.py`**: Script per decodificare un messaggio nascosto.
- **`processed_corpus.txt`**: File di supporto contenente parole per generare il testo di copertura.
- **`output_encodato.txt`**: Esempio di file generato contenente il testo codificato.

---

## 🛠️ Come funziona

### 1. Codifica 🖋️
Il programma richiede:
- **Un messaggio da codificare**: Inserito dall'utente.
- **Una password (opzionale)**: Per cifrare ulteriormente il messaggio.

L'output sarà un file `.txt` con un testo apparentemente innocuo, ma che contiene al suo interno il messaggio nascosto.

### 2. Decodifica 🔓
Per decodificare il messaggio:
- Inserire il file `.txt` generato.
- Inserire la password (se usata durante la codifica).

---

## 🔑 Importanza della password
La password è un ulteriore livello di sicurezza: senza di essa, anche avendo il file, risulta impossibile decifrare il contenuto nascosto. **Non condividere mai la password tramite lo stesso canale del file codificato!** 🛡️

---

## 📋 Esempio di utilizzo

### Codifica
1. Eseguire `encode_text.py`.
2. Inserire il messaggio da nascondere.
3. Inserire una password (facoltativa).
4. Il file generato (`output_encodato.txt`) sarà pronto per essere inviato.

### Decodifica
1. Eseguire `decode_text.py`.
2. Selezionare il file `.txt` da decodificare.
3. Inserire la password (se impostata).
4. Il messaggio nascosto verrà mostrato in chiaro.

---

## ✨ Ragionamenti alla base
- **Perché la steganografia testuale?** 🧐  
  La steganografia testuale è una tecnica meno evidente rispetto a quella basata su immagini o file audio, ma è altrettanto efficace per comunicazioni discrete.
  
- **Utilizzo del file di parole (`processed_corpus.txt`)**  
  Questo file contiene una lista di parole casuali utilizzate per generare il testo di copertura. È progettato per sembrare naturale e rendere più difficile individuare il messaggio nascosto.

---

## ⚙️ Requisiti tecnici
- **Python 3.x**: Assicurarsi di avere Python installato sul sistema.

---

## 👨‍💻 Autore
Progetto realizzato da **Sebastiano Gelmetti**, 💻  
Per domande o suggerimenti, contattatemi!

---

## 🚀 Note finali
Questo progetto è stato creato per scopi educativi e non deve essere utilizzato per attività illegali. 🛑  
Sperimentate, divertitevi e rimanete sempre etici!

