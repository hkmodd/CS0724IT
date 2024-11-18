import matplotlib.pyplot as plt

# Dati per i sistemi
processi = ['P1', 'P2', 'P3', 'P4']
tempi_cpu_mono = [3, 2, 1, 4]  # Tempi utilizzo CPU (mono-tasking)
tempi_attesa_mono = [2, 1, 0, 1]  # Tempi attesa eventi esterni (mono-tasking)

tempi_cpu_multi = [3, 2, 1, 4]  # Simili al mono-tasking per CPU
tempi_attesa_multi = [2, 1, 0, 1]  # Simili al mono-tasking per attesa

time_sharing = [1, 1, 1, 1]  # Supponendo time-sharing con quantum di 1 secondo

# Funzione per creare grafico tipo Gantt
def crea_grafico(processi, cpu_times, wait_times, title, filename):
    fig, ax = plt.subplots(figsize=(10, 6))
    y_pos = range(len(processi))
    bar_height = 0.4
    
    # Aggiungere barre per il tempo CPU
    ax.barh(y_pos, cpu_times, height=bar_height, color='yellow', label='Tempo utilizzo CPU')
    
    # Aggiungere barre per il tempo di attesa
    for i, (cpu, wait) in enumerate(zip(cpu_times, wait_times)):
        if wait > 0:
            ax.barh(y_pos[i], wait, left=cpu, height=bar_height, color='green', label='Tempo attesa eventi esterni' if i == 0 else "")
    
    # Etichette
    ax.set_yticks(y_pos)
    ax.set_yticklabels(processi)
    ax.set_xlabel('Tempo (secondi)')
    ax.set_title(title)
    ax.legend(loc='upper right')
    
    # Salvare il grafico
    plt.tight_layout()
    plt.savefig(f'/mnt/data/{filename}.png')
    plt.show()

# Grafico mono-tasking
crea_grafico(processi, tempi_cpu_mono, tempi_attesa_mono, "Sistemi Mono-tasking", "mono_tasking")

# Grafico multi-tasking
crea_grafico(processi, tempi_cpu_multi, tempi_attesa_multi, "Sistemi Multi-tasking", "multi_tasking")
