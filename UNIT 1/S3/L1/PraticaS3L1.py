import matplotlib.pyplot as plt

# Dati relativi ai processi
processi = ['P1', 'P2', 'P3', 'P4']

# Dati per il sistema Mono-tasking: ogni processo ha un inizio, un tempo di utilizzo CPU (giallo) e un tempo di attesa (verde)
mono_tasking_data = [
    {'start': 0, 'cpu': 3, 'wait': 2},
    {'start': 5, 'cpu': 2, 'wait': 1},
    {'start': 8, 'cpu': 1, 'wait': 0},
    {'start': 9, 'cpu': 4, 'wait': 1}
]

# Dati per il sistema Multi-tasking: i processi sfruttano la CPU in modo più efficiente, riducendo i tempi morti
multi_tasking_data = [
    {'start': 0, 'cpu': 3, 'wait': 2},
    {'start': 2, 'cpu': 2, 'wait': 1},
    {'start': 4, 'cpu': 1, 'wait': 0},
    {'start': 5, 'cpu': 4, 'wait': 1}
]

# Dati per il sistema Time-sharing: ogni processo viene gestito ciclicamente, con un quantum fisso di 1 secondo
time_sharing_data = [
    {'process': 'P1', 'start_times': [0, 4, 8]},
    {'process': 'P2', 'start_times': [1, 5, 9]},
    {'process': 'P3', 'start_times': [2, 6]},
    {'process': 'P4', 'start_times': [3, 7, 10]}
]


# Funzione per creare un grafico Gantt per Mono-tasking e Multi-tasking
def crea_grafico_gantt_esteso(dati, titolo, nome_file):
    # Configura il grafico
    fig, ax = plt.subplots(figsize=(10, 6))
    y_pos = range(len(dati))
    bar_height = 0.4

    # Aggiunge le barre dei processi
    for i, processo in enumerate(dati):
        # Barra gialla: tempo di utilizzo CPU
        ax.barh(i, processo['cpu'], left=processo['start'], color='yellow', edgecolor='black', height=bar_height, label='CPU' if i == 0 else "")
        # Barra verde: tempo di attesa (se presente)
        if processo['wait'] > 0:
            ax.barh(i, processo['wait'], left=processo['start'] + processo['cpu'], color='green', edgecolor='black', height=bar_height, label='Attesa' if i == 0 else "")

    # Imposta le etichette e la scala
    ax.set_yticks(y_pos)
    ax.set_yticklabels(processi)
    ax.set_xlim(0, 15)  # Imposta la timeline da 0 a 15 secondi
    ax.set_xlabel('Tempo (secondi)')
    ax.set_title(titolo)
    ax.legend(loc='upper right')

    # Salva il grafico e lo mostra
    plt.tight_layout()
    plt.savefig(f'{nome_file}.png')
    plt.show()


# Funzione per creare un grafico Gantt per Time-sharing
def crea_grafico_time_sharing_esteso(dati, titolo, nome_file):
    # Configura il grafico
    fig, ax = plt.subplots(figsize=(10, 6))
    bar_height = 0.4
    y_pos = range(len(dati))

    # Aggiunge le barre dei processi con i tempi distribuiti
    for i, processo in enumerate(dati):
        for tempo_inizio in processo['start_times']:
            ax.barh(i, 1, left=tempo_inizio, color='yellow', edgecolor='black', height=bar_height, label='CPU' if tempo_inizio == processo['start_times'][0] else "")

    # Imposta le etichette e la scala
    ax.set_yticks(y_pos)
    ax.set_yticklabels([processo['process'] for processo in dati])
    ax.set_xlim(0, 15)  # Imposta la timeline da 0 a 15 secondi
    ax.set_xlabel('Tempo (secondi)')
    ax.set_title(titolo)
    ax.legend(loc='upper right')

    # Salva il grafico e lo mostra
    plt.tight_layout()
    plt.savefig(f'{nome_file}.png')
    plt.show()


# Generazione dei grafici
crea_grafico_gantt_esteso(mono_tasking_data, "Sistemi Mono-tasking (Timeline 15s)", "mono_tasking_15s")
crea_grafico_gantt_esteso(multi_tasking_data, "Sistemi Multi-tasking (Timeline 15s)", "multi_tasking_15s")
crea_grafico_time_sharing_esteso(time_sharing_data, "Sistemi Time-sharing (Timeline 15s)", "time_sharing_15s")
