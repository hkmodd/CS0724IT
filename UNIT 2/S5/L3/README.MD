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

## Analisi del Report Dettagliato

Dai risultati della scansione, sono state identificate diverse vulnerabilità critiche e ad alto rischio che evidenziano le potenziali debolezze del sistema:

---

### **Vulnerabilità Critiche**

1. **Apache Tomcat AJP Connector Request Injection (Ghostcat)**
   - **Porta:** TCP/8009
   - **Descrizione:** Una vulnerabilità nel connettore AJP di Apache Tomcat consente agli attaccanti di accedere a file arbitrari sul server o di eseguire codice arbitrario.
   - **Soluzione simulata:** Disabilitare il connettore AJP o configurarlo per accettare richieste solo da indirizzi IP fidati.

2. **Debian OpenSSH/OpenSSL Package Random Number Generator Weakness**
   - **Porta:** TCP/22 (SSH)
   - **Descrizione:** Un difetto nel generatore di numeri casuali di OpenSSL su alcune versioni di Debian rende le chiavi crittografiche deboli e facilmente prevedibili.
   - **Soluzione simulata:** Rigenerare tutte le chiavi SSH e SSL e aggiornare OpenSSL.

3. **SSL Version 2 and 3 Protocol Detection**
   - **Porta:** TCP/25 (SMTP)
   - **Descrizione:** SSLv2 e SSLv3 sono protocolli deprecati con vulnerabilità note, come attacchi di tipo Man-in-the-Middle.
   - **Soluzione simulata:** Disabilitare SSLv2 e SSLv3, abilitando solo TLS 1.2 o versioni successive.

4. **VNC Server 'password' Password**
   - **Porta:** TCP/5900
   - **Descrizione:** Il server VNC utilizza una password debole o predefinita, consentendo accessi non autorizzati.
   - **Soluzione simulata:** Configurare una password sicura e abilitare l'autenticazione a due fattori.

---

### **Vulnerabilità di Alto Rischio**

1. **Samba Badlock Vulnerability**
   - **Porta:** TCP/445 (SMB)
   - **Descrizione:** Una debolezza nei protocolli SAM e LSAD consente attacchi di tipo Man-in-the-Middle che possono compromettere dati sensibili.
   - **Soluzione simulata:** Aggiornare Samba alla versione 4.4.2 o successive.

2. **SSL Medium Strength Cipher Suites Supported (SWEET32)**
   - **Porta:** TCP/443 (HTTPS)
   - **Descrizione:** L'uso di cifrature di media forza, come 3DES, può esporre il sistema ad attacchi crittografici.
   - **Soluzione simulata:** Disabilitare le cifrature 3DES e configurare il server per utilizzare solo algoritmi di crittografia moderni.

3. **NFS Shares World Readable**
   - **Porta:** TCP/2049
   - **Descrizione:** Condivisioni NFS configurate in modo insicuro permettono l'accesso a file sensibili da parte di utenti non autorizzati.
   - **Soluzione simulata:** Limitare l'accesso NFS a host fidati e configurare i permessi di accesso correttamente.

4. **Telnet Server Detection**
   - **Porta:** TCP/23
   - **Descrizione:** Il server Telnet consente connessioni non crittografate, esponendo credenziali e dati a intercettazioni.
   - **Soluzione simulata:** Disabilitare Telnet e utilizzare SSH per le connessioni remote.

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
