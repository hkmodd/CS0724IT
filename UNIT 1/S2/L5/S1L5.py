import datetime

print("Inizio del programma...\n")  # Stampa per indicare che il programma è iniziato, con una riga vuota dopo

def assistente_virtuale(comando):
    comando = comando.lower().strip()  # Eliminare eventuali spazi extra
    if comando == "che giorno è?":
        oggi = datetime.date.today()
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y") + "\n"
    elif comando == "che ore sono?":
        ora_attuale = datetime.datetime.now().time()
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M:%S") + "\n"
    elif comando == "come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale\n"
    else:
        risposta = "Non ho capito la tua domanda.\n"
    return risposta

while True:
    print("Aspetto un input...\n")  # Messaggio che indica che l'assistente sta aspettando un input
    comando_utente = input()
    if comando_utente.lower().strip() in ["esci", "chiudi", "fine"]:
        print("Arrivederci!\n")
        break
    else:
        print(assistente_virtuale(comando_utente))
