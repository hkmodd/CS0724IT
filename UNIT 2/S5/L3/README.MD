# 📝 Consegna S5/L3
# 🛡️ Vulnerability Scanning mediante Nessus 

## Obiettivo
L’obiettivo di questo esercizio era mettere alla prova le mie competenze eseguendo una scansione delle vulnerabilità con Nessus sulla macchina virtuale **Metasploitable**. Il risultato? Identificare le vulnerabilità presenti, analizzarne i dettagli e riflettere sulle loro implicazioni per la sicurezza. Un esercizio pratico per passare dalla teoria all’azione! 🛡️

---

## Configurazione della Rete
📍 **Ambiente configurato con cura per la simulazione**:  
- **Macchine virtuali**:
  - **Kali Linux**: `192.168.50.2`
  - **Metasploitable**: `192.168.60.2`  
- **Firewall in mezzo**: PfSense per garantire la comunicazione sicura tra le due macchine.  
- **Target della scansione**: L’indirizzo della macchina vulnerabile, `192.168.60.2`.

---

## Passaggi Eseguiti

### 1️⃣ Installazione di Nessus
- Scaricato e installato **Nessus Essentials** su Kali Linux.  
- Configurato il servizio tramite l’interfaccia web su `https://127.0.0.1:8834` (il mio punto di controllo per questa missione 🖥️).  

### 2️⃣ Configurazione della Scansione
- **Tipo di scansione**: Una Basic Network Scan.  
- **Target**: `192.168.60.2`, con un focus su porte comunemente utilizzate (21, 22, 23, 25, 80, ecc.).  
- L’interfaccia di Nessus ha reso il setup intuitivo, permettendomi di lanciare subito l’analisi.  

### 3️⃣ Esecuzione della Scansione
- La scansione ha impiegato circa **10 minuti** per completarsi.  
- Il risultato? **108 vulnerabilità rilevate**, distribuite così:  
  - 🔴 **Critical**: 9  
  - 🟠 **High**: 7  
  - 🟡 **Medium**: 23  
  - 🟢 **Low**: 6  
  - 📄 **Info**: 63  

### 4️⃣ Analisi del Report
Ho esaminato nel dettaglio le vulnerabilità critiche e alte. Tra le principali spiccano:  

#### **Ghostcat**  
- **Cosa fa**: Questa vulnerabilità nel connettore AJP di Apache Tomcat consente l’accesso non autorizzato a risorse interne.  
- **Dettaglio**: Può essere sfruttata per caricare file arbitrari o ottenere accesso remoto.  
- **CVSS**: 9.8  

#### **Bind Shell Backdoor**  
- **Cosa fa**: La presenza di una backdoor consente agli attaccanti di connettersi direttamente alla macchina target senza alcuna autenticazione.  
- **Dettaglio**: Si tratta di un tipo comune di exploit presente in macchine volutamente vulnerabili.  
- **CVSS**: 9.8  

#### **SSL Version 2 e 3 Detection**  
- **Cosa fa**: L’uso di SSLv2 e SSLv3, protocolli deprecati, espone la macchina a vulnerabilità note, inclusi attacchi Man-in-the-Middle.  
- **Dettaglio**: Questi protocolli non supportano moderni standard di sicurezza come Forward Secrecy.  
- **CVSS**: 9.8  

#### **Debian OpenSSH/OpenSSL Weakness**  
- **Cosa fa**: Generazione di chiavi crittografiche deboli che possono essere facilmente compromesse.  
- **Dettaglio**: Questo problema era comune nelle vecchie versioni di Debian.  
- **CVSS**: 10.0  

---

## Nota Importante ⚠️  
**Metasploitable è progettata per essere vulnerabile.**  
Non ha senso correggere le vulnerabilità identificate su questa macchina, perché il suo scopo principale è fungere da ambiente di pratica per la sicurezza informatica. Tuttavia, comprendere i dettagli e le possibili mitigazioni è essenziale per applicare queste conoscenze a sistemi reali.

---

## Risultati e Mitigazioni

### Vulnerabilità Critiche Analizzate  
1️⃣ **Ghostcat**  
- **Soluzione simulata**: Aggiornare Apache Tomcat e disabilitare il connettore AJP, se non necessario.  

2️⃣ **SSL Version 2 e 3 Detection**  
- **Soluzione simulata**: Disabilitare SSLv2 e SSLv3, abilitando solo TLS 1.2 e successivi.  

3️⃣ **Bind Shell Backdoor**  
- **Soluzione simulata**: Analizzare i processi sospetti e rimuovere la backdoor.  

---

## Raccomandazioni Generali  
🔒 Aggiornare pacchetti e software vulnerabili nei sistemi reali.  
🛑 Disabilitare protocolli e servizi non essenziali.  
🔐 Implementare crittografia moderna per SSL/TLS.

---

## Conclusioni
Questo esercizio mi ha permesso di esplorare le potenzialità di Nessus e di approfondire la gestione delle vulnerabilità. Metasploitable ha fornito un ambiente sicuro per testare e imparare, senza il rischio di causare danni in un ambiente reale. 📊

---

## Documentazione
Il report dettagliato della scansione è stato salvato in formato PDF per una futura consultazione.  
