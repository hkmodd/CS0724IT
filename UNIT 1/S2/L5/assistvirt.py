import datetime
import difflib

# Definizione delle varianti dei comandi accettati
varianti_comandi = {
    "qual è la data di oggi?": [
        "qual'è la data di oggi?", "quale la data di oggi?", "quale è la data di oggi?", 
        "data di oggi?", "oggi è che giorno?", "che giorno è oggi?", "data oggi?", "data del giorno?"
    ],
    "che ore sono?": [
        "ke ore sono?", "che ore sono", "che ora è?", "ora?", "che ore sono adesso?", 
        "quali sono le ore?", "l'ora corrente?", "che ore abbiamo?", "ora attuale?", "ora esatta?", "che ore?", "ore?"
    ],
    "come ti chiami?": [
        "qual è il tuo nome?", "quale il tuo nome?", "chi sei?", "chi è l'assistente?", 
        "come ti chiami", "il tuo nome qual è?", "tu come ti chiami?", "identificati", "nome assistente?", "come te chiami?"
    ],
    "che tempo fa?": [
        "com'è il tempo?", "che tempo c'è?", "fa freddo?", "fa caldo?", 
        "com'è il meteo?", "qual è la temperatura?", "quale temperatura c'è?", "meteo?", "temperatura oggi?", "com'è fuori?", "che clima c'è?"
    ]
}

# Crea una lista unica di tutti i comandi possibili e le loro varianti
comandi_possibili = {}
for comando, varianti in varianti_comandi.items():
    comandi_possibili[comando.lower()] = comando
    for variante in varianti:
        comandi_possibili[variante.lower()] = comando

def interpreta_input(comando):
    """
    Funzione che cerca di interpretare l'input dell'utente utilizzando fuzzy matching con difflib.
    """
    comando = comando.lower().strip()

    # Prima prova una corrispondenza esatta
    if comando in comandi_possibili:
        return comandi_possibili[comando]

    # Se non trova una corrispondenza esatta, usa il fuzzy matching
    miglior_match = difflib.get_close_matches(comando, comandi_possibili.keys(), n=1, cutoff=0.4)

    if miglior_match:
        return comandi_possibili[miglior_match[0]]
    else:
        return "Non ho capito la tua domanda."

def assistente_virtuale(comando):
    """
    Funzione che fornisce la risposta in base al comando interpretato.
    """
    comando_interpretato = interpreta_input(comando)

    if comando_interpretato == "qual è la data di oggi?":
        oggi = datetime.date.today()
        risposta = f"La data di oggi è {oggi.strftime('%d/%m/%Y')}\n"
    elif comando_interpretato == "che ore sono?":
        ora_attuale = datetime.datetime.now().time()
        risposta = f"L'ora attuale è {ora_attuale.strftime('%H:%M:%S')}\n"
    elif comando_interpretato == "come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale\n"
    elif comando_interpretato == "che tempo fa?":
        risposta = "Mi dispiace, non posso fornire informazioni sul meteo al momento.\n"
    else:
        risposta = "Non ho capito la tua domanda.\n"
    
    return risposta

def main():
    print("Benvenuto su AssistVirt.py!...\n")
    while True:
        try:
            print("Aspetto un input...\n")
            comando_utente = input()

            # Uscita se viene rilevato un comando di chiusura
            if comando_utente.lower().strip() in ["esci", "chiudi", "fine"]:
                print("Arrivederci!\n")
                break

            # Risposta dell'assistente
            print(assistente_virtuale(comando_utente))

        except KeyboardInterrupt:
            print("\nProgramma terminato manualmente. Arrivederci!\n")
            break
        except Exception as e:
            print("Si è verificato un errore imprevisto. Riprova.\n")

if __name__ == "__main__":
    main()
