# Consegna S5/L3 - Vulnerability Scanning con Nessus

## Obiettivo
L'obiettivo di questo esercizio è stato eseguire una scansione delle vulnerabilità utilizzando Nessus sulla macchina virtuale Metasploitable, identificando le vulnerabilità presenti e analizzando i risultati per comprendere le loro implicazioni.

## Configurazione della Rete
- **Macchine virtuali**:
  - Kali Linux: `192.168.50.2`
  - Metasploitable: `192.168.60.2`
- **Firewall**: Le due macchine comunicano tramite PfSense.
- **Target della scansione**: `192.168.60.2`

## Passaggi Eseguiti

### 1. Installazione di Nessus
- Scaricato e installato Nessus Essentials su Kali Linux.
- Avviato il servizio Nessus e configurato tramite interfaccia web su `https://127.0.0.1:8834`.

### 2. Configurazione della Scansione
- Tipo di scansione: **Basic Network Scan**.
- **Target IP**: `192.168.60.2`.
- **Range di porte**: Solo porte comuni (21, 22, 23, 25, 80, 110, 139, 443, 445, 3389).
- Configurazione avviata tramite interfaccia Nessus.

### 3. Esecuzione della Scansione
- La scansione è durata circa 10 minuti e ha generato un report dettagliato contenente 108 vulnerabilità rilevate, suddivise per gravità:
  - **Critical**: 9
  - **High**: 7
  - **Medium**: 23
  - **Low**: 6
  - **Info**: 63

### 4. Analisi del Report
- Esaminati i dettagli delle vulnerabilità critiche e alte. Alcune delle vulnerabilità principali identificate:
  - **Ghostcat (Apache Tomcat AJP Connector Request Injection)** - CVSS: 9.8
  - **Bind Shell Backdoor Detection** - CVSS: 9.8
  - **SSL Version 2 and 3 Protocol Detection** - CVSS: 9.8
  - **Debian OpenSSH/OpenSSL Package Weakness** - CVSS: 10.0

## Risultati e Mitigazioni
### Vulnerabilità Critiche Analizzate:
1. **Ghostcat**:
   - **Descrizione**: Vulnerabilità nel connettore AJP di Apache Tomcat che consente l'accesso non autorizzato.
   - **Mitigazione**: Aggiornamento di Apache Tomcat e disabilitazione del connettore AJP, se non necessario.

2. **SSL Version 2 and 3 Protocol Detection**:
   - **Descrizione**: Protocollo SSL obsoleto e insicuro.
   - **Mitigazione**: Disabilitare SSLv2 e SSLv3, abilitando solo TLS 1.2 e successivi.

3. **Bind Shell Backdoor**:
   - **Descrizione**: Backdoor rilevata tramite una shell bind.
   - **Mitigazione**: Esaminare i processi sospetti e rimuovere la backdoor.

### Raccomandazioni Generali
- Aggiornare i pacchetti vulnerabili.
- Disabilitare protocolli e servizi non necessari.
- Implementare crittografia moderna per le connessioni SSL/TLS.

## Conclusioni
La scansione ha evidenziato diverse vulnerabilità critiche che richiedono interventi urgenti. Questo esercizio è stato utile per familiarizzare con lo strumento Nessus e comprendere come identificare e analizzare le vulnerabilità nei sistemi.

## Report
Il report dettagliato della scansione è stato esportato in formato PDF per documentazione e revisione futura.
