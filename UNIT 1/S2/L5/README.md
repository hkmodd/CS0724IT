# Consegna S2/L5 - Assistente Virtuale - Python Project

## Descrizione
L'Assistente Virtuale è un programma Python progettato per rispondere a domande comuni come la data odierna, l'orario corrente, e altre interazioni di base. Il progetto sfrutta la libreria `datetime` per calcoli temporali e utilizza un sistema di fuzzy matching per interpretare l'input dell'utente, rendendo il programma flessibile anche in presenza di varianti lessicali.

## Funzionalità
- **Data corrente**: L'utente può chiedere la data odierna.
- **Orario corrente**: Risposta precisa sull'ora attuale.
- **Identità dell'assistente**: L'utente può scoprire il nome dell'assistente virtuale.
- **Input robusto**: Il programma riconosce varianti di comandi utilizzando fuzzy matching.
- **Chiusura intuitiva**: Comandi come "esci", "chiudi" o "fine" terminano il programma.

## Struttura del Codice
- **`interpreta_input`**: Funzione che analizza l'input dell'utente e restituisce il comando corrispondente, anche se scritto con errori.
- **`assistente_virtuale`**: Gestisce le risposte in base ai comandi interpretati.
- **`main`**: Ciclo principale che gestisce l'interazione con l'utente.

## Requisiti
- Python 3.x
- Librerie standard (`datetime`, `difflib`)

## Esecuzione
1. Assicurarsi di avere Python 3.x installato.
2. Salvare il codice in un file, ad esempio `AssistenteVirtuale.py`.
3. Avviare il programma tramite terminale:
   ```bash
   python AssistenteVirtuale.py
