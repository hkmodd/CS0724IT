from PIL import Image
from pattern_recognition import PatternRecognitionModel

class PietInterpreter:
    def __init__(self, image_path, model_path):
        # Carica l'immagine utilizzando Pillow (PIL)
        try:
            self.image = Image.open(image_path)
            if self.image.format not in ['PNG', 'GIF']:
                raise ValueError("L'immagine deve essere in formato PNG o GIF.")
        except FileNotFoundError:
            raise ValueError("Immagine non trovata. Verifica il percorso.")
        except Exception as e:
            raise ValueError(f"Errore durante il caricamento dell'immagine: {e}")

        # Parametri necessari per l'analisi dell'immagine
        self.stack = []
        self.width, self.height = self.image.size
        self.pointer = (0, 0)  # Partenza in alto a sinistra
        self.direction = "right"  # Direzione iniziale di movimento
        self.direction_pointers = ["right", "down", "left", "up"]
        self.model = PatternRecognitionModel(model_path)  # Rete neurale per riconoscere i pattern

    def run(self):
        """
        Esegue il codice Piet a partire dall'immagine.
        """
        result = self._process_image()
        return result

    def _process_image(self):
        """
        Esegue l'elaborazione dell'immagine per interpretare il programma.
        """
        output = ""

        max_steps = 1000
        steps = 0

        while self._valid_pointer() and steps < max_steps:
            steps += 1
            current_color = self._get_current_color()

            # Ignora il canale alpha (se esiste)
            if len(current_color) == 4:
                current_color = current_color[:3]

            # Utilizza la rete neurale per riconoscere il pattern
            recognized_operation = self.model.recognize(current_color)

            # Stampa di debug per verificare il colore e la posizione corrente
            print(f"Puntatore: {self.pointer}, Colore corrente: {current_color}, Operazione riconosciuta: {recognized_operation}")

            if recognized_operation == "ostacolo":
                print("Ostacolo nero trovato, cambio direzione.")
                if not self._find_valid_direction():
                    print("Nessuna direzione valida trovata, fine programma.")
                    break
            elif recognized_operation == "ignora":
                self._move_pointer()
                continue
            else:
                # Gestione delle operazioni vere e proprie basata sul colore
                self._execute_operation(recognized_operation)
            
            # Muove il puntatore nella direzione attuale
            self._move_pointer()
        
        # Recupera i dati dallo stack e genera l'output
        if self.stack:
            output = "".join(map(str, self.stack))
        
        return output

    def _valid_pointer(self):
        """Verifica se il puntatore è in un'area valida dell'immagine"""
        x, y = self.pointer
        return 0 <= x < self.width and 0 <= y < self.height

    def _get_current_color(self):
        """Ritorna il colore del pixel nella posizione corrente del puntatore"""
        x, y = self.pointer
        return self.image.getpixel((x, y))

    def _move_pointer(self):
        """Muove il puntatore nella direzione attuale"""
        x, y = self.pointer

        if self.direction == "right":
            self.pointer = (x + 1, y)
        elif self.direction == "left":
            self.pointer = (x - 1, y)
        elif self.direction == "up":
            self.pointer = (x, y - 1)
        elif self.direction == "down":
            self.pointer = (x, y + 1)

    def _find_valid_direction(self):
        """Cambia direzione finché non trova una direzione valida per muoversi"""
        original_direction = self.direction
        for _ in range(len(self.direction_pointers)):
            self._change_direction()
            if self._valid_pointer() and self._get_current_color() != (0, 0, 0):
                return True
        # Nessuna direzione valida trovata
        self.direction = original_direction
        return False

    def _change_direction(self):
        """Cambia direzione in caso di ostacolo (nero)"""
        current_index = self.direction_pointers.index(self.direction)
        self.direction = self.direction_pointers[(current_index + 1) % len(self.direction_pointers)]
    
    def _execute_operation(self, operation):
        """Esegue un'operazione basata sul pattern riconosciuto"""
        # Questo è un esempio semplificato per mostrare il funzionamento base.
        # In una vera implementazione, dovremmo basare l'operazione sulle transizioni di colore.

        if operation == "aggiungi_H":
            self.stack.append('H')
        elif operation == "aggiungi_e":
            self.stack.append('e')
        elif operation == "aggiungi_l":
            self.stack.append('l')
        elif operation == "aggiungi_o":
            self.stack.append('o')
        elif operation == "aggiungi_spazio":
            self.stack.append(' ')
        elif operation == "aggiungi_W":
            self.stack.append('W')
        elif operation == "aggiungi_r":
            self.stack.append('r')
        elif operation == "aggiungi_d":
            self.stack.append('d')
        else:
            print(f"Operazione non riconosciuta: {operation}, nessuna operazione eseguita.")
