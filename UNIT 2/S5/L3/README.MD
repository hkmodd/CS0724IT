# 📝 Consegna S5/L3
# Vulnerability Scanning mediante Nessus 🚀

## Obiettivo
L’obiettivo di questo esercizio era mettermi alla prova installando ed eseguendo Nessus sulla VM Kali per lanciare una scansione delle vulnerabilità sulla macchina virtuale **Metasploitable**. 
Il risultato? Identificare le vulnerabilità presenti, analizzarne i dettagli e riflettere sulle loro implicazioni per la sicurezza. 🛡️

---

## Configurazione della Rete
📍 **Ambiente configurato per la simulazione**:  
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
- **Ghostcat**: Una vulnerabilità nel connettore AJP di Apache Tomcat (CVSS 9.8).  
- **Bind Shell Backdoor**: Una backdoor attiva rilevata sulla macchina (CVSS 9.8).  
- **SSL Version 2 e 3 Detection**: Protocollo obsoleto e insicuro (CVSS 9.8).  
- **Debian OpenSSH/OpenSSL Weakness**: Chiavi crittografiche deboli (CVSS 10.0).

---

## Risultati e Mitigazioni

### Vulnerabilità Critiche Analizzate  
1️⃣ **Ghostcat**  
- **Cosa fa**: Permette accessi non autorizzati tramite il connettore AJP.  
- **Soluzione**: Aggiornare Apache Tomcat e disabilitare il connettore AJP, se non necessario.  

2️⃣ **SSL Version 2 e 3 Detection**  
- **Cosa fa**: Espone il sistema a possibili attacchi sfruttando protocolli non sicuri.  
- **Soluzione**: Disabilitare SSLv2 e SSLv3, mantenendo attivi solo TLS 1.2 e successivi.  

3️⃣ **Bind Shell Backdoor**  
- **Cosa fa**: Consente a un attaccante di avere accesso remoto tramite una shell bind.  
- **Soluzione**: Analizzare i processi sospetti e rimuovere la backdoor.  

---

## Raccomandazioni Generali  
🔒 Aggiornare pacchetti e software vulnerabili.  
🛑 Disabilitare protocolli e servizi non essenziali.  
🔐 Implementare crittografia moderna per SSL/TLS.

---

## Conclusioni
Questa esperienza mi ha permesso di esplorare le potenzialità di Nessus e di approfondire le modalità per identificare e gestire vulnerabilità critiche. Ho trovato il processo stimolante e utile per comprendere come affrontare i problemi di sicurezza nel mondo reale. 📊

## Documentazione
Il report dettagliato della scansione è stato salvato in formato PDF per una futura consultazione.  

👉 **Il prossimo step? Approfondire l’implementazione delle mitigazioni e affinare le strategie di scansione.** 💡
