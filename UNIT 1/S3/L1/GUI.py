import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Dati relativi ai processi
processi = ['P1', 'P2', 'P3', 'P4']

# Dati per i grafici
mono_tasking_data = [
    {'start': 0, 'cpu': 3, 'wait': 2},
    {'start': 5, 'cpu': 2, 'wait': 1},
    {'start': 8, 'cpu': 1, 'wait': 0},
    {'start': 9, 'cpu': 4, 'wait': 1}
]
multi_tasking_data = [
    {'start': 0, 'cpu': 3, 'wait': 2},
    {'start': 2, 'cpu': 2, 'wait': 1},
    {'start': 4, 'cpu': 1, 'wait': 0},
    {'start': 5, 'cpu': 4, 'wait': 1}
]
time_sharing_data = [
    {'process': 'P1', 'start_times': [0, 4, 8]},
    {'process': 'P2', 'start_times': [1, 5, 9]},
    {'process': 'P3', 'start_times': [2, 6]},
    {'process': 'P4', 'start_times': [3, 7, 10]}
]

# Funzione per creare grafici statici
def crea_grafico_statico(dati, titolo):
    fig, ax = plt.subplots(figsize=(8, 4))
    y_pos = range(len(dati))
    bar_height = 0.4

    for i, processo in enumerate(dati):
        ax.barh(i, processo['cpu'], left=processo['start'], color='yellow', edgecolor='black', height=bar_height, label='CPU' if i == 0 else "")
        if processo['wait'] > 0:
            ax.barh(i, processo['wait'], left=processo['start'] + processo['cpu'], color='green', edgecolor='black', height=bar_height, label='Attesa' if i == 0 else "")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(processi)
    ax.set_xlim(0, 15)
    ax.set_xlabel('Tempo (secondi)')
    ax.set_title(titolo)
    ax.legend(loc='upper right')
    return fig

# Funzione per creare grafico Time-sharing animato
def crea_grafico_time_sharing_animato(dati, titolo, nome_file_gif):
    fig, ax = plt.subplots(figsize=(8, 4))
    bar_height = 0.4
    y_pos = range(len(dati))

    def update(frame):
        ax.clear()
        ax.set_yticks(y_pos)
        ax.set_yticklabels([p['process'] for p in dati])
        ax.set_xlim(0, 15)
        ax.set_xlabel('Tempo (secondi)')
        ax.set_title(titolo)
        for i, processo in enumerate(dati):
            for start_time in processo['start_times']:
                if start_time <= frame:
                    ax.barh(i, 1, left=start_time, color='yellow', edgecolor='black', height=bar_height)

    ani = FuncAnimation(fig, update, frames=16, repeat=False)
    ani.save(nome_file_gif, writer='pillow')
    return fig

# Classe per la GUI
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Grafici Sistemi Operativi")
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.descriptions = [
            "Sistema Mono-tasking: ogni processo viene eseguito interamente prima di passare al successivo.",
            "Sistema Multi-tasking: i processi condividono il tempo della CPU, riducendo i tempi morti.",
            "Sistema Time-sharing: ogni processo riceve un quantum fisso e viene eseguito ciclicamente."
        ]
        self.figures = [
            crea_grafico_statico(mono_tasking_data, "Sistema Mono-tasking"),
            crea_grafico_statico(multi_tasking_data, "Sistema Multi-tasking"),
            crea_grafico_time_sharing_animato(time_sharing_data, "Sistema Time-sharing", "time_sharing_corrected.gif")
        ]
        self.current_index = 0

        self.canvas = None
        self.label = None
        self.buttons = []

        self.show_graph()

    def show_graph(self):
        if self.canvas:
            self.canvas.get_tk_widget().pack_forget()
        if self.label:
            self.label.pack_forget()
        for button in self.buttons:
            button.pack_forget()

        # Mostra il grafico
        fig = self.figures[self.current_index]
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Mostra la descrizione
        self.label = ttk.Label(self.frame, text=self.descriptions[self.current_index], font=("Arial", 12))
        self.label.pack(side=tk.BOTTOM, pady=10)

        # Pulsante per avanzare o terminare
        self.buttons = []
        if self.current_index < len(self.figures) - 1:
            next_button = ttk.Button(self.frame, text="Avanti", command=self.next_graph)
            next_button.pack(side=tk.BOTTOM, pady=10)
            self.buttons.append(next_button)
        else:
            finish_button = ttk.Button(self.frame, text="Termina", command=self.root.quit)
            finish_button.pack(side=tk.BOTTOM, pady=10)
            self.buttons.append(finish_button)

    def next_graph(self):
        self.current_index += 1
        self.show_graph()

# Avvio dell'app GUI
root = tk.Tk()
app = App(root)
root.mainloop()
