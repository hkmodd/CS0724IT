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

---

## Analisi del Report Dettagliato
Dai risultati della scansione, ho estrapolato le seguenti vulnerabilità critiche e di alto rischio:

### **Vulnerabilità Critiche**
1. **Bind Shell Backdoor Detection**
   - **Porta**: TCP/1524
   - **Descrizione**: Una backdoor che consente connessioni senza autenticazione.
   - **Soluzione simulata**: Verifica dei processi sospetti e reinstallazione del sistema se compromesso.

2. **Debian OpenSSH/OpenSSL Weakness**
   - **Porta**: TCP/22 (SSH)
   - **Descrizione**: Generazione di chiavi deboli su sistemi Debian vulnerabili.
   - **Soluzione simulata**: Rigenerare tutte le chiavi crittografiche e aggiornare OpenSSL.

3. **SSL Version 2 and 3 Detection**
   - **Porte**: TCP/25 (SMTP)
   - **Descrizione**: Uso di protocolli deprecati che espongono a vulnerabilità crittografiche.
   - **Soluzione simulata**: Disabilitare SSLv2/SSLv3 e abilitare TLS 1.2 o superiore.

4. **Samba Badlock Vulnerability**
   - **Porta**: TCP/445
   - **Descrizione**: Problema di negoziazione dell'autenticazione su Samba, che consente attacchi MITM.
   - **Soluzione simulata**: Aggiornare Samba alla versione corretta.

---

## Raccomandazioni Generali  
🔒 **Aggiornare pacchetti e software vulnerabili nei sistemi reali**: mantenere sempre aggiornati i servizi e applicare le patch di sicurezza fornite dai vendor.  
🛑 **Disabilitare protocolli e servizi non essenziali**: ridurre la superficie di attacco eliminando funzionalità non necessarie.  
🔐 **Implementare crittografia moderna per SSL/TLS**: garantire che solo protocolli sicuri (come TLS 1.2 o 1.3) siano abilitati.  
🛡️ **Integrare regole di firewall più severe**: configurare il firewall per limitare l'accesso alle porte e ai servizi vulnerabili solo a IP autorizzati.  
⚙️ **Segmentare la rete**: isolare i sistemi vulnerabili o di test in una VLAN dedicata per limitare i danni in caso di compromissione.  

---

## Nota Importante ⚠️  
**Sappiamo bene che Metasploitable è progettata per essere vulnerabile.**  
Non ha senso quindi correggere le vulnerabilità identificate su questa macchina, perché il suo scopo principale è fungere da ambiente di pratica per la sicurezza informatica. Tuttavia, comprendere i dettagli e le possibili mitigazioni è essenziale per applicare queste conoscenze a sistemi reali.

---

## Conclusioni
Questo esercizio mi ha permesso di esplorare le potenzialità di Nessus e di approfondire la gestione delle vulnerabilità. Metasploitable ha fornito un ambiente sicuro per testare e imparare. 📊

---

## Documentazione
Il report dettagliato della scansione è stato salvato in formato PDF per una futura consultazione.  
