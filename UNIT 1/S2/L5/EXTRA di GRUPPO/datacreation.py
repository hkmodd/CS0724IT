from PIL import Image
import os

# Definisci i colori per ogni classe
colors = {
    "aggiungi_H": (255, 0, 0),  # Rosso
    "aggiungi_e": (0, 255, 0),  # Verde
    "aggiungi_l": (0, 0, 255),  # Blu
    "aggiungi_o": (255, 255, 0),  # Giallo
    "aggiungi_spazio": (0, 255, 255),  # Ciano
    "aggiungi_W": (255, 0, 255),  # Magenta
    "aggiungi_r": (128, 128, 128),  # Grigio
    "aggiungi_d": (128, 0, 0)  # Marrone scuro
}

# Crea il dataset di immagini
os.makedirs("dataset/train", exist_ok=True)

for label, color in colors.items():
    class_dir = os.path.join("dataset/train", label)
    os.makedirs(class_dir, exist_ok=True)

    # Genera 100 immagini per ogni classe
    for i in range(100):
        img = Image.new("RGB", (32, 32), color)
        img_path = os.path.join(class_dir, f"{label}_{i}.png")
        img.save(img_path)

print("Immagini generate correttamente.")
