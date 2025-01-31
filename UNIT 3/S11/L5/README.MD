
# 📐 Progetto S10/L5 📐
#  Cyber Security & Ethical Hacking 🚀
## 📌 Descrizione del Progetto
Questo progetto raccoglie e documenta le attività svolte nei laboratori di **Cyber Security & Ethical Hacking** incentrati su Windows PowerShell, Wireshark, Nmap e attacchi a database MySQL.

Le attività includono:
1. **Utilizzo di Windows PowerShell** 🖥️
2. **Analisi del traffico HTTP e HTTPS con Wireshark** 🌐
3. **Esplorazione di Nmap per la scansione delle porte** 🔍
4. **Attacco a un database MySQL e analisi dei pacchetti PCAP** 📊

Il documento segue una struttura dettagliata con spiegazioni, comandi e riflessioni finali.

---

## 📂 1. Utilizzo di Windows PowerShell 🖥️

PowerShell è un ambiente di scripting avanzato per Windows che consente di automatizzare attività amministrative. Durante questo laboratorio, sono stati esplorati i seguenti punti:

### **1.1 Accesso alla console PowerShell**
- Aperto **PowerShell** tramite la ricerca di Windows.
- Controllato la versione di PowerShell con:
  ```powershell
  $PSVersionTable
  ```

### **1.2 Comandi Base**
- Utilizzato `dir` per visualizzare file e cartelle.
- Provato `ping`, `ipconfig`, `cd` e `netstat`.

### **1.3 Esplorazione dei Cmdlets**
- Eseguito `Get-Command` per elencare tutti i cmdlet disponibili.
- Utilizzato `Get-Help Get-Process` per ottenere dettagli su un comando.
- Avviato un processo e terminato con:
  ```powershell
  Start-Process notepad.exe
  Stop-Process -Name notepad
  ```

### **1.4 Netstat in PowerShell**
- Visualizzate le connessioni di rete con:
  ```powershell
  netstat -ano
  ```

### **1.5 Svuotare il Cestino con PowerShell**
- Usato il comando:
  ```powershell
  Clear-RecycleBin -Confirm:$false
  ```

✅ **Risultati:** PowerShell si è rivelato uno strumento potente per amministrare Windows in modo automatizzato.

---

## 🌐 2. Analisi del traffico HTTP e HTTPS con Wireshark

Wireshark è un potente strumento per catturare e analizzare il traffico di rete.

### **2.1 Acquisizione del traffico HTTP**
- Avviato **Wireshark** e selezionata l'interfaccia di rete.
- Filtrato il traffico con il filtro `http`.
- Navigato su un sito web HTTP per osservare le richieste GET e POST.

### **2.2 Acquisizione del traffico HTTPS**
- Ripetuto il test accedendo a un sito HTTPS.
- Notato che i pacchetti risultano criptati.
- Identificato il **TLS Handshake**.

### **2.3 Considerazioni di Sicurezza**
- HTTP è **non sicuro** e i dati possono essere intercettati.
- HTTPS utilizza la crittografia per proteggere le informazioni.

✅ **Risultati:** Wireshark ha permesso di identificare le differenze tra traffico HTTP e HTTPS e di comprendere l'importanza della crittografia.

---

## 🔍 3. Esplorazione di Nmap

Nmap è uno strumento essenziale per la scansione delle reti e la sicurezza informatica.

### **3.1 Installazione e Verifica**
- Eseguito il comando:
  ```bash
  nmap --version
  ```
- Confermata la corretta installazione.

### **3.2 Scansione di Base**
- Scansionata una macchina con:
  ```bash
  nmap -sV -p 80,443 <IP_TARGET>
  ```
- Identificato il server web e il certificato TLS.

### **3.3 Scansione Avanzata**
- Usato:
  ```bash
  nmap -A -T4 <IP_TARGET>
  ```
- Rilevato il sistema operativo, i servizi attivi e possibili vulnerabilità.

✅ **Risultati:** Nmap ha evidenziato dettagli utili per un'analisi di sicurezza di una rete target.

---

## 📊 4. Attacco a un database MySQL (Analisi PCAP)

### **4.1 Apertura del file PCAP**
- Caricato il file **SQL_Lab.pcap** in Wireshark.
- Applicato il filtro `mysql` per isolare il traffico SQL.

### **4.2 Identificazione di un attacco SQL Injection**
- Identificati pacchetti con query sospette:
  ```sql
  SELECT * FROM users WHERE username='admin' -- ';
  ```
- Osservato il furto di credenziali dal database.

### **4.3 Analisi dei Dati Estratti**
- L'attacco ha rivelato tabelle come `users` e `payments`.
- Dimostrata l'importanza di proteggere i database con **prepared statements** e **firewall applicativi**.

✅ **Risultati:** L'analisi ha evidenziato i rischi di un database non protetto e l'importanza di prevenire SQL Injection.

---

## 🎯 Conclusioni

Questo progetto ha permesso di esplorare strumenti essenziali per la sicurezza informatica:
1. **PowerShell** per la gestione avanzata dei sistemi Windows.
2. **Wireshark** per il monitoraggio e l'analisi del traffico di rete.
3. **Nmap** per la scansione delle porte e dei servizi di rete.
4. **Analisi dei database SQL** per comprendere gli attacchi e le contromisure.

🔒 **Lezione appresa:** La sicurezza informatica è un campo critico che richiede una costante vigilanza e l'uso di strumenti adeguati.
