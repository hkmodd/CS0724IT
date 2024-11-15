from piet_interpreter import PietInterpreter

# Percorso dell'immagine Piet
img_path = "Hello_World.png"
# Percorso del modello addestrato
model_path = "pattern_recognition_model.pth"  # Assicurati che il modello esista in questo percorso

# Inizializza l'interprete con l'immagine e il modello addestrato
interpreter = PietInterpreter(img_path, model_path)

# Esegui il codice Piet
output = interpreter.run()

# Stampa il risultato dell'esecuzione
print("Risultato del programma Piet:", output)
