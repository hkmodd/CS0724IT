# piet_interpreter_example_extended.py

from piet_interpreter import PietInterpreter
from PIL import Image
import random
import logging

# Configura il logging per tracciare le azioni dell'interprete
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Funzione per generare immagini Piet offuscate
# Genera immagini con percorsi di codel complessi e sfide offuscate

def generate_obfuscated_image(image_path, output_path, complexity=5):
    """
    Genera un'immagine Piet offuscata a partire da un'immagine esistente.
    :param image_path: Percorso dell'immagine di input
    :param output_path: Percorso per salvare l'immagine modificata
    :param complexity: Livello di offuscamento (1-10)
    """
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    for _ in range(complexity * 10):  # Più alto è complexity, più codels verranno modificati
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels[x, y] = new_color

    image.save(output_path)
    logging.info(f"Immagine offuscata generata: {output_path}")

# Carica l'immagine Piet
img_path = "Hello_World.png"  # Assicurati che il file esista nella directory
obfuscated_img_path = "Hello_World_obfuscated.png"
generate_obfuscated_image(img_path, obfuscated_img_path, complexity=7)

# Carica l'immagine obfuscata
image = Image.open(obfuscated_img_path)

# Inizializza l'interprete
interpreter = PietInterpreter(image)

# Esegui il codice Piet e gestisci eventuali errori
try:
    logging.info("Inizio esecuzione del programma Piet...")
    output = interpreter.run()
    logging.info("Esecuzione completata.")
    print("Risultato del programma Piet:", output)
except Exception as e:
    logging.error("Errore durante l'esecuzione del codice Piet: %s", e)

# Stress Test dell'Interprete
logging.info("Avvio Stress Test dell'interprete con immagini di grande complessità...")
for i in range(5):
    complexity_level = random.randint(5, 10)
    temp_img_path = f"stress_test_{i}.png"
    generate_obfuscated_image(img_path, temp_img_path, complexity=complexity_level)
    try:
        temp_image = Image.open(temp_img_path)
        interpreter = PietInterpreter(temp_image)
        output = interpreter.run()
        logging.info(f"Risultato Stress Test {i}: {output}")
    except Exception as e:
        logging.error(f"Errore durante il test {i}: {e}")

logging.info("Stress Test completato.")

# Funzione di analisi per trovare vulnerabilità nell'uso dei codels
# Identifica possibili buffer overflow o overflow di codels

def analyze_image_for_overflow(image_path):
    """
    Analizza un'immagine Piet per identificare possibili vulnerabilità di overflow.
    :param image_path: Percorso dell'immagine da analizzare
    """
    image = Image.open(image_path)
    width, height = image.size
    codel_map = {}
    pixels = image.load()

    # Mappa i codels per identificare eventuali pattern pericolosi
    for x in range(width):
        for y in range(height):
            color = pixels[x, y]
            if color in codel_map:
                codel_map[color] += 1
            else:
                codel_map[color] = 1

    for color, count in codel_map.items():
        if count > width * height * 0.1:  # Se più del 10% dell'immagine è dello stesso colore, potrebbe indicare overflow
            logging.warning(f"Potenziale overflow trovato nel colore {color}: {count} occorrenze.")

analyze_image_for_overflow(obfuscated_img_path)
