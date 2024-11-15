from PIL import Image
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from simple_cnn import SimpleCNN  # Importa SimpleCNN dal nuovo file

class PatternRecognitionModel:
    def __init__(self, model_path):
        # Definisci il modello come fatto nel file di training
        self.model = SimpleCNN()
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()  # Mettere il modello in modalità valutazione
        self.transform = transforms.ToTensor()

    def recognize(self, color):
        # Crea una piccola immagine (32x32 pixel) con il colore corrente
        color_image = Image.new("RGB", (32, 32), color)
        # Converti l'immagine in un tensor
        color_tensor = self.transform(color_image).unsqueeze(0)
        with torch.no_grad():
            output = self.model(color_tensor)
        _, predicted = torch.max(output, 1)
        # Mappa il risultato predetto all'operazione corrispondente
        return self._map_prediction_to_operation(predicted.item())

    def _map_prediction_to_operation(self, prediction):
        # Definire la mappatura delle predizioni in operazioni Piet
        mapping = {
            0: "ignora",
            1: "aggiungi_H",
            2: "aggiungi_e",
            3: "aggiungi_l",
            4: "aggiungi_o",
            5: "aggiungi_spazio",
            6: "aggiungi_W",
            7: "aggiungi_r",
            8: "aggiungi_d"
        }
        return mapping.get(prediction, "ignora")
