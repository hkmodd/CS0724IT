# Progetto: Shell PHP per Controllo Remoto su Metasploitable

**Autore**: Sebastiano  
**Data**: [Inserisci la data]  
**Obiettivo**: Caricare e utilizzare una shell PHP per ottenere il controllo remoto della macchina Metasploitable, eseguendo comandi come se fossero lanciati direttamente dal terminale interno.

---

## **Introduzione**
Questo progetto consiste nella creazione e implementazione di una shell PHP che consente:
1. **Controllo completo** della macchina Metasploitable.
2. **Esecuzione di comandi remoti** in modo interattivo.
3. **Navigazione del file system**, caricamento e download di file.
4. **Intercettazione delle richieste HTTP** tramite BurpSuite per analisi e verifica.

---

## **Requisiti**
- **Macchine Virtuali**:
  - Kali Linux
  - Metasploitable
- **Strumenti**:
  - PHP 7.x o superiore (già preinstallato su Metasploitable)
  - Browser web (Firefox/Chromium su Kali)
  - BurpSuite Community o Professional Edition
- **File richiesto**:
  - `shell.php` (il codice PHP fornito nel progetto)

---

## **Passaggi eseguiti**

### **1. Configurazione dell'ambiente**
1. **Connessione tra le macchine virtuali**:
   - Kali Linux e Metasploitable sono state configurate sulla stessa rete NAT.
   - Convalidata la connessione tramite il comando:
     ```bash
     ping 192.168.1.10
     ```
   - Risultato: le macchine si vedono correttamente.

2. **DVWA su Metasploitable**:
   - Accesso alla Web Application DVWA tramite:
     ```
     http://192.168.1.10/dvwa
     ```
   - Livello di sicurezza impostato su **Low** per consentire l'upload della shell.

---

### **2. Caricamento della Shell**
1. Creazione della shell `shell.php`:
   - Codice PHP personalizzato con funzionalità avanzate:
     - Esecuzione comandi remoti.
     - Navigazione persistente del file system.
     - Interfaccia interattiva con AJAX per aggiornamenti in tempo reale.
   - [Inserire il codice completo della shell come esempio].

2. Upload della shell tramite DVWA:
   - Navigato alla sezione **File Upload** su DVWA.
   - Caricato il file `shell.php`.

3. Verifica del caricamento:
   - Accesso al file caricato tramite browser:
     ```
     http://192.168.1.10/dvwa/hackable/uploads/shell.php?key=mysecretkey
     ```
   - Test iniziali con comandi semplici (`ls`, `whoami`).

---

### **3. Intercettazioni con BurpSuite**
1. **Configurazione del Proxy**:
   - Configurato BurpSuite come proxy sul browser di Kali:
     - Proxy: `127.0.0.1:8080`
     - Abilitato il certificato di Burp nel browser.

2. **Intercettazione richieste HTTP**:
   - Catturata la richiesta HTTP inviata durante l'accesso alla shell:
     ```
     GET /dvwa/hackable/uploads/shell.php?key=mysecretkey&action=ls
     ```
   - Analisi della struttura della richiesta e del response.

3. **Intercettazione dei comandi POST**:
   - Inviato comando tramite POST (esempio: `whoami`).
   - Verificato il contenuto del body:
     ```
     POST /dvwa/hackable/uploads/shell.php?key=mysecretkey
     Body: cmd=whoami
     ```

4. **Screenshot BurpSuite**:
   - Allegati screenshot delle richieste intercettate in **Proxy > HTTP History**.

---

### **4. Risultati**
1. **Esecuzione comandi remoti**:
   - Eseguiti comandi come:
     - `ls` - Per elencare file.
     - `cd /var/www/html` - Per cambiare directory.
     - `nano test.txt` - Per modificare file.
   - Tutti eseguiti con successo tramite la shell PHP.

2. **Navigazione completa del file system**:
   - Navigato tra le directory.
   - Visualizzati e scaricati file importanti.

3. **Output delle richieste HTTP**:
   - Verificato che ogni comando viene inviato correttamente e il risultato restituito.

---

## **Screenshot**
### **Shell in azione**
![Shell in azione](inserire-percorso-immagine)

### **Intercettazioni BurpSuite**
![Intercettazione BurpSuite](inserire-percorso-immagine)

---

## **Conclusione**
La shell PHP caricata su Metasploitable consente un controllo remoto completo della macchina. La combinazione con BurpSuite ha permesso di analizzare e verificare il comportamento delle richieste HTTP. Questo esercizio dimostra l'importanza delle protezioni contro vulnerabilità come file upload non sicuri.

---

## **Prossimi Step**
- Implementare una protezione più avanzata per la chiave segreta.
- Migliorare l'interfaccia grafica per un terminale ancora più intuitivo.
- Integrare funzionalità di logging avanzato e gestione file.

---

## **Bonus**
Il progetto include una shell PHP avanzata con:
- Navigazione persistente.
- Interfaccia grafica interattiva con AJAX.
- Funzioni di caricamento e download file.
