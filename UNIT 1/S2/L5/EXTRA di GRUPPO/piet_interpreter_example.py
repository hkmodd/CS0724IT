
from piet_interpreter import PietInterpreter
from PIL import Image

# Carica l'immagine Piet
img_path = "esempio_piet.png"  # Immagine che contiene il codice Piet
image = Image.open(img_path)

# Inizializza l'interprete
interpreter = PietInterpreter(image)

# Esegui il codice Piet
output = interpreter.run()

# Stampa il risultato dell'esecuzione
print("Risultato del programma Piet:", output)
