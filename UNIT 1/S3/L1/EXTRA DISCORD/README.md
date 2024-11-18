# 💻 Gli Alchimisti della Steganografia

Benvenuti, **cavalieri del sapere**! 🌟 Dopo aver superato le prime sfide, è tempo di esplorare l'antica arte della **steganografia**. Questo repository vi guiderà attraverso le tecniche fondamentali per nascondere messaggi all'interno di immagini, audio e testi, con esempi pratici in Python.

---

## 📖 Indice

- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Steganografia nelle Immagini](#steganografia-nelle-immagini)
  - [encode_lsb.py](#encode_lsbpy)
  - [decode_lsb.py](#decode_lsbpy)
- [Steganografia nei File Audio](#steganografia-nei-file-audio)
  - [encode_audio.py](#encode_audiopy)
  - [decode_audio.py](#decode_audiopy)
- [Steganografia nel Testo](#steganografia-nel-testo)
  - [encode_text.py](#encode_textpy)
  - [decode_text.py](#decode_textpy)
- [Considerazioni Etiche](#considerazioni-etiche)
- [Conclusione](#conclusione)
- [Riferimenti](#riferimenti)

---

## Introduzione

La **steganografia** è l'arte di nascondere messaggi all'interno di altri media in modo che l'esistenza stessa del messaggio sia nascosta. 🔒 A differenza della crittografia, che maschera il contenuto di un messaggio, la steganografia nasconde il messaggio in bella vista.

---

## Prerequisiti

- **Python 3.x** 🐍
- **Librerie Python**:
  - `Pillow` per la manipolazione delle immagini
    ```bash
    pip install Pillow
    ```
  - Nessuna libreria aggiuntiva per l'audio (usa la libreria `wave` integrata)

---

## Steganografia nelle Immagini

### encode_lsb.py

**Descrizione:** Questo script codifica un messaggio di testo all'interno di un'immagine utilizzando la tecnica dei Least Significant Bit (LSB).

```python
# encode_lsb.py

from PIL import Image

def encode_lsb(image_path, message, output_image_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    message += chr(0)  # Terminatore del messaggio
    binary_message = ''.join([format(ord(i), '08b') for i in message])

    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                pixel = list(img.getpixel((col, row)))
                for n in range(0, 3):
                    if index < len(binary_message):
                        pixel[n] = pixel[n] & ~1 | int(binary_message[index])
                        index += 1
                encoded.putpixel((col, row), tuple(pixel))
            else:
                break
    encoded.save(output_image_path)
    print(f"✅ Messaggio nascosto in {output_image_path}")

# Esempio di utilizzo
# encode_lsb('input_image.png', 'Messaggio segreto', 'encoded_image.png')
```

### decode_lsb.py

**Descrizione:** Questo script estrae un messaggio nascosto all'interno di un'immagine utilizzando la tecnica LSB.

```python
# decode_lsb.py

from PIL import Image

def decode_lsb(image_path):
    img = Image.open(image_path)
    width, height = img.size
    binary_message = ''
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for n in range(0, 3):
                binary_message += str(pixel[n] & 1)

    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '00000000':
            break
        message += chr(int(byte, 2))
    print(f"📩 Messaggio estratto: {message}")
    return message

# Esempio di utilizzo
# decode_lsb('encoded_image.png')
```

---

## Steganografia nei File Audio

### encode_audio.py

**Descrizione:** Questo script codifica un messaggio di testo all'interno di un file audio WAV.

```python
# encode_audio.py

import wave

def encode_audio(audio_in_path, message, audio_out_path):
    song = wave.open(audio_in_path, mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    message += chr(0)
    binary_message = ''.join([format(ord(i), '08b') for i in message])
    length = len(binary_message)

    for i in range(length):
        frame_bytes[i] = (frame_bytes[i] & ~1) | int(binary_message[i])

    modified_frames = bytes(frame_bytes)
    with wave.open(audio_out_path, 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(modified_frames)
    song.close()
    print(f"✅ Messaggio nascosto in {audio_out_path}")

# Esempio di utilizzo
# encode_audio('input_audio.wav', 'Messaggio segreto', 'encoded_audio.wav')
```

### decode_audio.py

**Descrizione:** Questo script estrae un messaggio nascosto all'interno di un file audio WAV.

```python
# decode_audio.py

import wave

def decode_audio(audio_path):
    song = wave.open(audio_path, mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    binary_message = [str(frame_bytes[i] & 1) for i in range(len(frame_bytes))]
    binary_message = ''.join(binary_message)

    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '00000000':
            break
        message += chr(int(byte, 2))
    song.close()
    print(f"🎵 Messaggio estratto: {message}")
    return message

# Esempio di utilizzo
# decode_audio('encoded_audio.wav')
```

---

## Steganografia nel Testo

### encode_text.py

**Descrizione:** Questo script codifica un messaggio di testo all'interno di un altro testo utilizzando spaziature (spazi singoli e doppi).

```python
# encode_text.py

def encode_text(message, cover_text):
    binary_message = ''.join([format(ord(i), '08b') for i in message])
    encoded_text = ''
    index = 0
    for char in cover_text:
        if char == ' ' and index < len(binary_message):
            if binary_message[index] == '1':
                encoded_text += '  '  # Due spazi per '1'
            else:
                encoded_text += ' '   # Uno spazio per '0'
            index += 1
        else:
            encoded_text += char
    print("✅ Testo con messaggio nascosto creato.")
    return encoded_text

# Esempio di utilizzo
# cover = "Questo è un testo di copertura per la steganografia."
# stego = encode_text('Ciao', cover)
# print(stego)
```

### decode_text.py

**Descrizione:** Questo script estrae un messaggio nascosto all'interno di un testo utilizzando le spaziature.

```python
# decode_text.py

def decode_text(stego_text):
    binary_message = ''
    i = 0
    while i < len(stego_text):
        if stego_text[i] == ' ':
            space_count = 1
            while i + 1 < len(stego_text) and stego_text[i + 1] == ' ':
                space_count += 1
                i += 1
            if space_count == 1:
                binary_message += '0'
            elif space_count == 2:
                binary_message += '1'
        i += 1

    message = ''
    for j in range(0, len(binary_message), 8):
        byte = binary_message[j:j+8]
        if len(byte) == 8:
            message += chr(int(byte, 2))
    print(f"📝 Messaggio estratto: {message}")
    return message

# Esempio di utilizzo
# stego = "Testo  di  esempio con  spazi  doppi."
# decode_text(stego)
```

---

## Considerazioni Etiche

⚠️ **Avvertenza Etica:** La steganografia è uno strumento potente che può essere utilizzato sia per proteggere la privacy sia per scopi illeciti. È fondamentale utilizzare queste tecniche in modo responsabile e legale, rispettando le normative vigenti e i diritti degli altri. L'autore non si assume alcuna responsabilità per un uso improprio di questi script.

---

## Conclusione

Congratulazioni, **cavalieri**! 🛡️ Avete esplorato le profondità della steganografia, apprendendo come nascondere e rivelare messaggi segreti attraverso diversi media. Che queste conoscenze vi guidino nel vostro percorso nel mondo della **cybersecurity**.

**Che l'intuizione sia la vostra bussola e il sapere la vostra armatura!** 🗡️

---

## Riferimenti

1. **"Cryptography and Network Security"** - William Stallings 📚
2. **Pillow Documentation** - [Pillow Docs](https://pillow.readthedocs.io/)
3. **Wave Module Documentation** - [Wave Module](https://docs.python.org/3/library/wave.html)
4. **Steghide** - [Steghide Project](http://steghide.sourceforge.net/)
5. **OpenPuff** - [OpenPuff Steganography](https://embeddedsw.net/OpenPuff_Steganography_Home.html)

---

# 📁 File del Progetto

## encode_lsb.py

[Visualizza il codice](#encode_lsbpy)

## decode_lsb.py

[Visualizza il codice](#decode_lsbpy)

## encode_audio.py

[Visualizza il codice](#encode_audiopy)

## decode_audio.py

[Visualizza il codice](#decode_audiopy)

## encode_text.py

[Visualizza il codice](#encode_textpy)

## decode_text.py

[Visualizza il codice](#decode_textpy)

---