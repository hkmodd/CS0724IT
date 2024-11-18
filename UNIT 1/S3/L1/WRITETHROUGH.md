
# GraphGUI 📊
**GraphGUI** è un'applicazione interattiva in Python progettata per analizzare e visualizzare i modelli di gestione dei processi nei sistemi operativi: **Mono-tasking**, **Multi-tasking** e **Time-sharing**. Questa documentazione esamina ogni sezione del codice per spiegare il funzionamento del programma.

---

## Indice

1. [Introduzione](#introduzione)
2. [Importazioni e Librerie](#importazioni-e-librerie)
3. [Dati per i Grafici](#dati-per-i-grafici)
4. [Generazione dei Grafici](#generazione-dei-grafici)
   - [Grafici Statici](#grafici-statici)
   - [Grafico Animato per Time-sharing](#grafico-animato-per-time-sharing)
5. [Classe App per la GUI](#classe-app-per-la-gui)
   - [Metodo `show_graph`](#metodo-show_graph)
   - [Gestione dei Pulsanti](#gestione-dei-pulsanti)
6. [Esecuzione del Programma](#esecuzione-del-programma)

---

## Introduzione

GraphGUI è stato creato per aiutare a comprendere visivamente i modelli di gestione dei processi nei sistemi operativi:
- **Mono-tasking**: Esecuzione sequenziale dei processi.
- **Multi-tasking**: Sovrapposizione e gestione efficiente dei processi.
- **Time-sharing**: Assegnazione di quanti fissi per l'esecuzione ciclica dei processi.

Il programma utilizza grafici statici e un'animazione per il modello Time-sharing, offrendo una GUI interattiva per navigare tra i grafici.

---

## Importazioni e Librerie

```python
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
```

### Funzione delle librerie:
- **`tkinter`**: Gestisce la GUI del programma.
- **`matplotlib`**: Genera grafici statici e animati.
- **`pillow`**: Salva le animazioni in formato GIF.

---

## Dati per i Grafici

I dati per i processi sono definiti come liste di dizionari, che specificano:
- **Tempo di inizio** (`start`).
- **Tempo di utilizzo CPU** (`cpu`).
- **Tempo di attesa** (`wait`).

Esempio:
```python
mono_tasking_data = [
    {'start': 0, 'cpu': 3, 'wait': 2},
    {'start': 5, 'cpu': 2, 'wait': 1},
    {'start': 8, 'cpu': 1, 'wait': 0},
    {'start': 9, 'cpu': 4, 'wait': 1}
]
```

Il modello Time-sharing utilizza una struttura diversa, specificando i tempi di esecuzione per ogni processo:
```python
time_sharing_data = [
    {'process': 'P1', 'start_times': [0, 4, 8]},
    {'process': 'P2', 'start_times': [1, 5, 9]},
    {'process': 'P3', 'start_times': [2, 6]},
    {'process': 'P4', 'start_times': [3, 7, 10]}
]
```

---

## Generazione dei Grafici

### Grafici Statici

I grafici statici rappresentano i modelli Mono-tasking e Multi-tasking. La funzione `crea_grafico_statico` utilizza barre orizzontali per visualizzare:
- **Giallo**: Tempo di utilizzo CPU.
- **Verde**: Tempo di attesa.

```python
def crea_grafico_statico(dati, titolo):
    fig, ax = plt.subplots(figsize=(8, 4))
    for i, processo in enumerate(dati):
        ax.barh(i, processo['cpu'], left=processo['start'], color='yellow', ...)
        if processo['wait'] > 0:
            ax.barh(i, processo['wait'], left=processo['start'] + processo['cpu'], color='green', ...)
    return fig
```

### Grafico Animato per Time-sharing

La funzione `crea_grafico_time_sharing_animato` genera un'animazione per mostrare come i processi si alternano in base al quantum. L'animazione viene salvata come GIF utilizzando `pillow`.

```python
def crea_grafico_time_sharing_animato(dati, titolo, nome_file_gif):
    ani = FuncAnimation(fig, update, frames=16, repeat=False)
    ani.save(nome_file_gif, writer='pillow')
    return fig
```

---

## Classe App per la GUI

La classe `App` gestisce l'interfaccia grafica, consentendo di navigare tra i grafici tramite pulsanti.

### Metodo `__init__`

Definisce la struttura della GUI:
- **`descriptions`**: Spiega ogni modello di gestione dei processi.
- **`figures`**: Contiene i grafici generati.
- **`current_index`**: Indica il grafico corrente.

### Metodo `show_graph`

Gestisce la visualizzazione del grafico corrente, aggiornando:
- **Canvas**: Per disegnare il grafico.
- **Label**: Per visualizzare la descrizione.
- **Pulsanti**: Per avanzare o terminare.

```python
def show_graph(self):
    fig = self.figures[self.current_index]
    self.canvas = FigureCanvasTkAgg(fig, master=self.frame)
    self.canvas.draw()
```

### Gestione dei Pulsanti

I pulsanti "Avanti" e "Termina" vengono aggiornati dinamicamente:
- **Avanti**: Mostra il grafico successivo.
- **Termina**: Chiude la finestra.

---

## Esecuzione del Programma

Il programma viene avviato creando un'istanza della classe `App`:
```python
root = tk.Tk()
app = App(root)
root.mainloop()
```

Se la GUI non è supportata, i grafici vengono salvati automaticamente nella directory corrente.

---

## Conclusione

GraphGUI offre un'analisi visiva dei modelli di gestione dei processi, combinando grafici statici, animazioni e una GUI intuitiva. È un potente strumento per lo studio e la comprensione dei sistemi operativi.
