
# 🔐 Extra S3/L3: Criptazione e Firmatura con OpenSSL e Python

## 📜 Obiettivo
L'esercizio richiede di:
1. **Generare chiavi RSA** utilizzando OpenSSL.
2. **Estrarre la chiave pubblica** dalla chiave privata.
3. **Criptare e decriptare un messaggio** semplice con le chiavi generate.
4. **Firmare e verificare un messaggio** per garantire la sicurezza e l'integrità.

---

## 🚀 Passaggi principali

### 🛠️ 1. Generazione delle chiavi RSA
- Utilizzando OpenSSL, generiamo una chiave privata e la salviamo in un file chiamato `private_key.pem`.
  ```bash
  openssl genrsa -out private_key.pem 2048
  ```
- Estraiamo la chiave pubblica da quella privata e la salviamo in `public_key.pem`:
  ```bash
  openssl rsa -in private_key.pem -pubout -out public_key.pem
  ```

### 🔒 2. Criptazione di un messaggio
- Scriviamo uno script Python chiamato `encdec.py` per criptare un messaggio (`"Evviva la crittografia boyy!"`) usando la chiave pubblica.
- Utilizziamo la libreria **cryptography** per implementare il padding e gestire i file delle chiavi.

### 🔑 3. Decriptazione del messaggio
- Decifriamo il messaggio criptato utilizzando la chiave privata.
- Lo script `encdec.py` gestisce sia la crittografia che la decrittografia.

### ✍️ 4. Firmatura e verifica del messaggio
- Creiamo uno script Python chiamato `firma.py` per:
  1. **Firmare** il messaggio con la chiave privata.
  2. **Verificare** la firma con la chiave pubblica per garantire che non sia stata manomessa.

---

## 📂 Dettaglio degli script

### `encdec.py`
Questo script implementa:
- **Caricamento delle chiavi**: Utilizza `serialization` per leggere i file `.pem`.
- **Criptazione**: Applica il padding `PKCS1v15` per crittografare il messaggio con la chiave pubblica.
- **Decriptazione**: Utilizza la chiave privata per decifrare il messaggio.

### `firma.py`
Questo script implementa:
- **Firma**: Genera una firma digitale del messaggio usando `SHA256` e la chiave privata.
- **Verifica**: Controlla che la firma sia valida con la chiave pubblica.

---

## 💡 Ragionamenti effettuati
1. La **cripto-asimmetrica** (RSA) è ideale per garantire sicurezza, grazie alla separazione tra chiavi pubbliche e private.
2. Il **padding** (PKCS1v15) è necessario per gestire correttamente i blocchi di dati durante la crittografia.
3. La **firma digitale** verifica l'integrità e l'autenticità del messaggio, garantendo che non sia stato alterato.

---

## 📈 Risultati finali
### Esecuzione di `encdec.py`:
```plaintext
Messaggio originale: Evviva la crittografia boyy!
Messaggio criptato: rBpx8RU9bCuaRZNIUH...
Messaggio decriptato: Evviva la crittografia boyy!
```

### Esecuzione di `firma.py`:
```plaintext
Base64 della firma: JSFBG0t0Fc...
Messaggio originale da confrontare: Evviva la crittografia boyy!
La firma è valida.
```

---

## ⚠️ Note importanti
1. Assicurarsi di eseguire gli script nella stessa directory dei file `.pem`.
2. Il messaggio criptato viene convertito in Base64 per facilitarne la visualizzazione.

---

## 🔧 Strumenti utilizzati
- **OpenSSL**: Per generare le chiavi RSA.
- **Python + cryptography**: Per la crittografia, decrittografia, firma e verifica.

---

💪 **Conclusione**: Con questo esercizio, abbiamo dimostrato come utilizzare la crittografia asimmetrica per garantire sicurezza e autenticità nei messaggi!
