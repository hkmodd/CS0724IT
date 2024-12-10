
# 📝 Consegna S6/L1
## <h1 align="center">Exploit File Upload</h1>
## **🎯 Obiettivo**: Creare e utilizzare una shell PHP per ottenere il controllo remoto completo della macchina Metasploitable, intercettare poi le richieste mediante BurpSuite, familiarizzare con gli ambienti e i tool.

---

## <h1 align="center">1️⃣ Creazione dell'ambiente</h1>
1. **🌐 Connessione tra Kali e Metasploitable**:
   - Le macchine sono configurate per comunicare tra loro.
   - Test di connettività eseguito con:
     ```bash
     ping 192.168.60.2
     ```
   - 🔄 Risultato: connettività confermata.

2. **🔒 Accesso alla DVWA su Metasploitable**:
   - L'applicazione web vulnerabile è stata raggiunta tramite:
     ```
     http://192.168.60.2/dvwa
     ```
   - Il livello di sicurezza è stato impostato inizialmente su **Low** per consentire l'upload della shell.
3. **🖋️ Creazione della shell `shell.php`**:
   - La shell PHP include funzionalità avanzate:
     - Esecuzione comandi remoti.
     - Navigazione persistente nel file system.
     - Interfaccia interattiva con output dinamico tramite AJAX.

---

## <h1 align="center">2️⃣ Caricamento della Shell</h1>
 **📤 Upload della shell su DVWA**:
   - File caricato tramite la sezione **File Upload**.
![Upload section](./UploadDVWA.png)

 **🔑 Accesso protetto alla shell**:
   - La chiave `mysecretkey` è obbligatoria per accedere alla shell. Questo garantisce che solo chi conosce la chiave possa utilizzarla.
   - Test di caricamento riuscito con accesso al file tramite browser:
     ```
     http://192.168.60.2/dvwa/hackable/uploads/shell.php?key=mysecretkey
     ```

---

## <h1 align="center">3️⃣ Intercettazione Upload con BurpSuite</h1>

1. **🛠️ Configurazione**:
   - Configurato BurpSuite per intercettare il traffico HTTP durante l'upload della shell `shell.php`.

2. **🔎 Intercettazione delle richieste HTTP**:
   - Durante il caricamento della shell tramite la sezione **File Upload** di DVWA, BurpSuite ha intercettato la seguente richiesta POST:
     ```
     POST /dvwa/vulnerabilities/upload/ HTTP/1.1
     Host: 192.168.60.2
     Content-Length: 3976
     Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryIYDDPameSV45LPyo
     ...
     ------WebKitFormBoundaryIYDDPameSV45LPyo
     Content-Disposition: form-data; name="uploaded"; filename="shell.php"
     Content-Type: application/x-php
     ...
     ```

   - Dall'intercettazione, è evidente che il file caricato è uno script PHP malevolo, ovvero una shell remota progettata per ottenere il controllo della macchina target. Questo dimostra come un'implementazione scorretta della gestione dei file caricati possa esporre il sistema a gravi rischi di compromissione.

   - La shell, una volta caricata, è stata localizzata nella directory specificata:  
     ```
     http://192.168.60.2/dvwa/hackable/uploads/shell.php?key=mysecretkey
     ```

3. **🔍 Analisi**:
   - La richiesta includeva il payload PHP della shell, che è stato elaborato dal server, consentendo così l'accesso remoto.
   - La chiave segreta `mysecretkey` ha fornito un ulteriore livello di autenticazione, assicurando che solo gli utenti autorizzati potessero interagire con la shell.

4. **📸 Screenshot Intercettazione**:
   ![Intercettazione Upload](./Upload.png)

---

## <h1 align="center">4️⃣ Utilizzo della Shell "sofisticata" ;)</h1>
1. **⚡ Esecuzione comandi remoti**:
   - Eseguiti comandi come:
     - `ls` - Per elencare file e directory.
     - `whoami` - Per identificare l'utente corrente.

2. **🗂️ Navigazione del file system**:
   - Comandi `cd` per cambiare directory:
     - Esempio: `cd /var/www/html`
   - 🔄 Navigazione persistente grazie alla gestione delle sessioni.

3. **🛠️ Interazione con strumenti**:
   - Eseguito `nano` per modificare file in modalità interattiva:
     - Esempio: `nano test.txt`
   - La shell fornisce una vera esperienza terminale.

4. **📁 Caricamento e download file**:
   - Caricare un file su Metasploitable:
     ```bash
     curl -F "file=@example.txt" "http://192.168.60.2/dvwa/hackable/uploads/shell.php?key=mysecretkey"
     ```
   - Scaricare un file da Metasploitable:
     ```bash
     curl "http://192.168.60.2/dvwa/hackable/uploads/shell.php?key=mysecretkey&action=download&file=/etc/passwd" -o passwd.txt
     ```
![Shell in azione](./ShellPreview.png)

## 🔧 Come la Shell Fornisce Controllo Completo
1. **Esecuzione Comandi**:
   - Ogni comando viene inviato tramite HTTP POST e processato direttamente dalla macchina Metasploitable usando `shell_exec`. L'output viene restituito come risposta HTTP, visibile nel terminale integrato.

2. **Persistenza delle directory**:
   - La shell utilizza variabili di sessione per mantenere lo stato della directory corrente, replicando un'esperienza simile al terminale.

3. **Interfaccia Interattiva**:
   - Utilizzando AJAX, l'interfaccia aggiorna dinamicamente il terminale senza necessità di ricaricare la pagina.

4. **Interazione con strumenti avanzati**:
   - La shell supporta strumenti terminali ad esempio `nano` fornendo un accesso completo e interattivo.

---

## <h1 align="center">4️⃣ Intercettazioni comandi Shell con BurpSuite</h1>
1. **🛠️ Configurazione**:
   - Configurato BurpSuite per intercettare il traffico HTTP.

2. **🔎 Intercettazione delle richieste HTTP**:
   - Esempio di richiesta intercettata:
     ```
     GET /dvwa/hackable/uploads/shell.php?key=mysecretkey&action=ls
     ```
   - Catturato il comando POST per eseguire `whoami`:
     ```
     POST /dvwa/hackable/uploads/shell.php?key=mysecretkey
     Body: cmd=whoami
     ```
![Intercettazione BurpSuite](./POST.png)

---

## <h1 align="center">5️⃣ Extra: Bypass della Sicurezza High su DVWA

1. **🔧 Configurazione della Sicurezza High**:
   - La sicurezza della DVWA è stata in seguito configurata su **High**, implementando restrizioni "più rigide" per il caricamento dei file.

2. **🔎 Metodo di Elusione**:
   - Nonostante la configurazione avanzata, è stato possibile caricare la shell `shell.php` rinominata in `.jpg`. Questo ha eluso il sistema di controllo che permette l'upload di file `.jpg` solo se:
     - Il file è lungo almeno **100000 byte**.
   - La shell è stata scritta in modo tale da rispettare la lunghezza minima richiesta, aggirando efficacemente le restrizioni.

3. **📤 Dettagli Tecnici**:
   - Il file è stato caricato tramite la sezione **File Upload**, ed è stato possibile eseguirlo come script PHP nonostante l'estensione `.jpg`.

4. **📸 Screenshot dell'Intercettazione**:
![Intercettazione BurpSuite](./BurpSuite.png)

---

# <h1 align="center">📌 Conclusioni</h1>

## **1️⃣ Importanza della Configurazione dell'Ambiente**
L'esperimento ha evidenziato l'importanza di configurare correttamente e testare gli ambienti prima di effettuare attività pratiche di exploit. La comunicazione stabile tra Kali e Metasploitable, unita alla configurazione adeguata di strumenti come DVWA e BurpSuite, è stata cruciale per il successo delle attività.

---

## **2️⃣ Impatto delle Vulnerabilità di Upload**
La vulnerabilità dell'upload di file malintenzionati in DVWA ha mostrato quanto un controllo superficiale sui file caricati possa compromettere un sistema. Nonostante le restrizioni impostate in modalità "High Security", è stato possibile:
- Eseguire codice malevolo.
- Superare restrizioni utilizzando tecniche di bypass, come il caricamento di file `.php` con estensioni non standard (es. `.jpg`) e la modifica dei payload per rispettare i requisiti.

Questo dimostra che le contromisure di sicurezza insufficienti o implementate in modo errato non prevengono attacchi sofisticati.

---

## **3️⃣ Potenzialità della Shell PHP**
La shell PHP caricata ha fornito un controllo remoto completo, con funzionalità quali:
- **Esecuzione di comandi remoti:** Gli attaccanti possono controllare il sistema senza restrizioni.
- **Navigazione persistente nel file system:** Grazie alla gestione delle sessioni, l'attività è stata continua senza necessità di ripetere configurazioni.
- **Interfaccia interattiva:** L'utilizzo di AJAX ha migliorato l'efficienza del controllo remoto, aggiornando il terminale in tempo reale.
- **Caricamento e download di file:** Questo ha permesso di manipolare direttamente file critici sulla macchina bersaglio, dimostrando il rischio di una compromissione totale.

---

## **4️⃣ Ruolo di BurpSuite nell'Intercettazione**
L'intercettazione delle richieste HTTP con BurpSuite è stata fondamentale per analizzare il traffico e comprendere come l'attacco sia stato condotto. Attraverso BurpSuite è stato possibile:
- **Identificare il payload PHP malevolo** caricato sulla macchina target.
- Analizzare richieste critiche, come `POST` per l'upload e `GET` per l'esecuzione.
- Verificare la trasmissione dei comandi remoti e gli output generati.

BurpSuite si è rivelato uno strumento essenziale per rilevare, analizzare e mitigare potenziali minacce di questo tipo.

---

## **5️⃣ Lezioni Imparate**
1. **L'importanza della sicurezza preventiva:** Implementare controlli rigorosi sui file caricati, come l'ispezione del contenuto effettivo e restrizioni per evitare l'esecuzione di script malevoli.
2. **Utilizzo delle chiavi di accesso:** L'uso di una chiave di autenticazione nella shell (`mysecretkey`) ha dimostrato come piccole aggiunte possano aumentare la sicurezza di uno script.
3. **Analisi e prevenzione:** Strumenti come BurpSuite sono indispensabili non solo per l'attacco, ma anche per la difesa, consentendo ai team di sicurezza di intercettare e bloccare traffico sospetto.
4. **Le restrizioni di sicurezza non sono infallibili:** Anche con impostazioni elevate, DVWA è stata compromessa, evidenziando la necessità di aggiornamenti regolari e implementazioni robuste.

---

## **6️⃣ Implicazioni per la Cybersecurity**
Questo esercizio evidenzia la fragilità di molte applicazioni web vulnerabili e la facilità con cui un attaccante esperto può sfruttarle. In un contesto reale, tali vulnerabilità potrebbero:
- Consentire il furto di dati sensibili.
- Trasformare un sistema compromesso in un punto di partenza per ulteriori attacchi.
- Comportare gravi conseguenze legali e finanziarie per le organizzazioni.

---

# <h1 align="center">**🚀 Conclusione generale**: L'attività non solo ha permesso di comprendere i rischi legati a vulnerabilità comuni, ma ha fornito una solida base per sviluppare competenze nell'uso di strumenti essenziali come BurpSuite e nell'analisi delle vulnerabilità, fondamentali per un ethical hacker.</h1>







