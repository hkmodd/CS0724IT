
# 📝 Consegna S6/L1
# Progetto: Shell PHP per Controllo Remoto su Metasploitable

---

**🎯 Obiettivo**: Creare e utilizzare una shell PHP per ottenere il controllo remoto completo della macchina Metasploitable, intercettare poi le richieste mediante BurpSuite.

---

## **📚 Introduzione**
Questo progetto dimostra come una shell PHP possa essere utilizzata per acquisire il controllo completo di un sistema vulnerabile. La shell caricata consente di:
- ✅ Eseguire comandi remoti come se si stesse interagendo direttamente dal terminale della macchina.
- ✅ Navigare liberamente nel file system.
- ✅ Caricare e scaricare file.
- ✅ Interagire con strumenti terminali, come editor di testo (`nano`).

---

## **⚙️ Requisiti**
- **Macchine Virtuali**:
  - Kali Linux: `192.168.50.2`
  - Metasploitable: `192.168.60.2`
- **Strumenti**:
  - PHP preinstallato su Metasploitable.
  - Browser web su Kali Linux.
  - BurpSuite per analisi delle richieste HTTP.
- **File richiesto**:
  - `shell.php` (incluso nel progetto).

---

## **📂 Passaggi eseguiti**

### **1️⃣ Configurazione dell'ambiente**
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
   - Il livello di sicurezza è stato impostato su **Low** per consentire l'upload della shell.

---

### **2️⃣ Caricamento della Shell**
1. **🖋️ Creazione della shell `shell.php`**:
   - La shell PHP include funzionalità avanzate:
     - Esecuzione comandi remoti.
     - Navigazione persistente nel file system.
     - Interfaccia interattiva con output dinamico tramite AJAX.
   - 📜 Codice completo fornito in appendice.

2. **📤 Upload della shell su DVWA**:
   - File caricato tramite la sezione **File Upload**.
   - Test di caricamento riuscito con accesso al file tramite browser:
     ```
     http://192.168.60.2/dvwa/hackable/uploads/shell.php?key=mysecretkey
     ```

3. **🔑 Accesso protetto alla shell**:
   - La chiave `mysecretkey` è obbligatoria per accedere alla shell. Questo garantisce che solo chi conosce la chiave possa utilizzarla.

---

### **3️⃣ Utilizzo della Shell**
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
   - Caricato un file su Metasploitable:
     ```bash
     curl -F "file=@example.txt" "http://192.168.60.2/dvwa/hackable/uploads/shell.php?key=mysecretkey"
     ```
   - Scaricato un file dalla macchina:
     ```bash
     curl "http://192.168.60.2/dvwa/hackable/uploads/shell.php?key=mysecretkey&action=download&file=/etc/passwd" -o passwd.txt
     ```

---

### **4️⃣ Intercettazioni con BurpSuite**
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
   - Analisi dettagliata inclusa con screenshot.

---

## **🔧 Come la Shell Fornisce Controllo Completo**
1. **Esecuzione Comandi**:
   - Ogni comando viene inviato tramite HTTP POST e processato direttamente dalla macchina Metasploitable usando `shell_exec`. L'output viene restituito come risposta HTTP, visibile nel terminale integrato.

2. **Persistenza delle directory**:
   - La shell utilizza variabili di sessione per mantenere lo stato della directory corrente, replicando un'esperienza simile al terminale.

3. **Interfaccia Interattiva**:
   - Utilizzando AJAX, l'interfaccia aggiorna dinamicamente il terminale senza necessità di ricaricare la pagina.

4. **Interazione con strumenti avanzati**:
   - La shell supporta strumenti terminali (`nano`, `vi`, `tree`, ecc.), fornendo un accesso completo e interattivo.

---

## **🖼️ Screenshot**
### **📸 Shell in azione**
![Shell in azione](./ShellPreview.png)

### **📸 Intercettazioni BurpSuite**
![Intercettazione BurpSuite](inserire-percorso-immagine)

---

## **📌 Conclusione**
La shell PHP caricata consente un controllo remoto completo della macchina Metasploitable. L'esperimento dimostra come vulnerabilità come l'upload di file non protetti possano esporre una macchina a rischi significativi. Attraverso questa shell è stato possibile eseguire comandi, navigare nel file system e interagire con strumenti di sistema senza restrizioni.

---



### **4️⃣ Intercettazioni con BurpSuite**

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
   - Inserire uno screenshot della schermata di BurpSuite con l'intercettazione della richiesta POST.
   ![Intercettazione Upload](./Upload.png)
