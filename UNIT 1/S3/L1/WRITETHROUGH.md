
# GraphGUI 📊 - Analisi di Sistemi Operativi: Mono-tasking, Multi-tasking e Time-sharing

Benvenuto su **GraphGUI**, un'applicazione interattiva sviluppata in Python per rappresentare graficamente le differenze tra i tre principali modelli di gestione dei processi nei sistemi operativi: **Mono-tasking**, **Multi-tasking** e **Time-sharing**. Questa documentazione offre una spiegazione dettagliata di ogni componente del programma, fornendo una guida chiara per comprenderne il funzionamento.

---

## Indice

1. [Introduzione](#introduzione)
2. [Funzionalità del Programma](#funzionalità-del-programma)
3. [Installazione e Requisiti](#installazione-e-requisiti)
4. [Struttura del Codice](#struttura-del-codice)
   - [Importazioni e Librerie](#importazioni-e-librerie)
   - [Generazione dei Grafici](#generazione-dei-grafici)
   - [Animazione per il Time-sharing](#animazione-per-il-time-sharing)
   - [Interfaccia Grafica (GUI)](#interfaccia-grafica-gui)
   - [Fallback alla Modalità Console](#fallback-alla-modalità-console)
5. [Esecuzione del Programma](#esecuzione-del-programma)
6. [Note Finali](#note-finali)

---

## Introduzione

**GraphGUI** è un'applicazione progettata per analizzare i modelli di gestione dei processi utilizzando grafici e animazioni. L'obiettivo è quello di rappresentare visivamente le differenze tra **Mono-tasking**, **Multi-tasking** e **Time-sharing**, facilitando la comprensione dei loro vantaggi e svantaggi.

---

## Funzionalità del Programma

- 📊 Generazione di grafici statici per Mono-tasking e Multi-tasking.
- 🔄 Animazione del modello Time-sharing.
- 🖥️ Interfaccia grafica interattiva per visualizzare i risultati.
- 🛠️ Fallback automatico alla modalità console per sistemi senza supporto GUI.

---

## Installazione e Requisiti

### Requisiti

- **Python 3.10 o superiore**.
- Librerie necessarie:
  - 📚 `matplotlib`
  - 📚 `tkinter`
  - 📚 `pillow` (per salvare le animazioni GIF)

### Installazione

1. Clonare o scaricare il progetto.
2. Installare le dipendenze richieste:
   ```bash
   pip install matplotlib pillow
   ```

---

## Struttura del Codice

### Importazioni e Librerie

```python
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import ttk
```

- **`matplotlib`**: Utilizzato per creare i grafici statici e animati.
- **`tkinter`**: Fornisce l'interfaccia grafica per visualizzare i grafici.
- **`pillow`**: Consente di salvare le animazioni come GIF.

---

### Generazione dei Grafici

#### Mono-tasking e Multi-tasking

I grafici per Mono-tasking e Multi-tasking sono generati utilizzando barre orizzontali:
- **Giallo**: Tempo di utilizzo CPU.
- **Verde**: Tempo di attesa.

```python
def crea_grafico_statico(dati, titolo):
    fig, ax = plt.subplots(figsize=(8, 4))
    y_pos = range(len(dati))
    bar_height = 0.4
    ...
    return fig
```

---

### Animazione per il Time-sharing

Il modello Time-sharing è rappresentato con un'animazione che mostra l'alternanza tra i processi:

```python
def crea_grafico_time_sharing_animato(dati, titolo, nome_file_gif):
    fig, ax = plt.subplots(figsize=(8, 4))
    def update(frame):
        ...
    ani.save(nome_file_gif, writer='pillow')
    return fig
```

---

### Interfaccia Grafica (GUI)

La GUI consente di navigare tra i grafici utilizzando pulsanti **Avanti** e **Termina**. Ogni grafico è accompagnato da una descrizione esplicativa.

---

### Fallback alla Modalità Console

Se la GUI non è supportata, i grafici vengono salvati automaticamente nella directory corrente:

- `mono_tasking_corrected.png`
- `multi_tasking_corrected.png`
- `time_sharing_corrected.gif`

---

## Esecuzione del Programma

1. Avviare lo script:
   ```bash
   python3 GraphGUI.py
   ```
2. Visualizzare i grafici nella GUI o accedere ai file generati in modalità console.

---

## Note Finali

**GraphGUI** dimostra come i concetti complessi della gestione dei processi possano essere resi accessibili e interattivi tramite visualizzazioni dinamiche. È uno strumento utile per lo studio e l'insegnamento dei sistemi operativi.

