# Funzione per creare grafico time-sharing
def crea_grafico_time_sharing(processi, quantum, total_time, title, filename):
    fig, ax = plt.subplots(figsize=(10, 6))
    y_pos = range(len(processi))
    bar_height = 0.4
    current_time = [0] * len(processi)
    
    # Disegnare i quanti di CPU
    for t in range(total_time):
        for i, process in enumerate(processi):
            if t % len(processi) == i:  # Ciclo dei processi
                ax.barh(y_pos[i], quantum, left=current_time[i], height=bar_height, color='yellow', label='Tempo utilizzo CPU' if t == 0 else "")
                current_time[i] += quantum

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

# Grafico time-sharing
crea_grafico_time_sharing(processi, quantum=1, total_time=12, title="Sistemi Time-Sharing", filename="time_sharing")
