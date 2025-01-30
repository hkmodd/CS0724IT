# 📝 Consegna S11/L3

# 🔥 Cisco CyberOps - 2

## 🛠️ Introduzione
Questo documento contiene lo svolgimento dettagliato del laboratorio "Utilizzo di Wireshark per Osservare la Stretta di Mano TCP a 3 Vie" e del laboratorio bonus "Utilizzo di Wireshark per Esaminare le Catture TCP e UDP". Verranno eseguite tutte le operazioni richieste, con particolare attenzione all'analisi dei pacchetti di rete per comprendere le dinamiche delle comunicazioni TCP e UDP.

---

## 🏆 Obiettivi del Laboratorio

### **Lab 1: Analisi della Stretta di Mano TCP a Tre Vie**
✅ Preparare gli host per catturare il traffico di rete
✅ Analizzare i pacchetti utilizzando Wireshark
✅ Visualizzare i pacchetti utilizzando tcpdump

### **Lab 2 (Bonus): Esaminazione delle Catture TCP e UDP**
✅ Identificare i campi dell'intestazione TCP e il funzionamento utilizzando una cattura di sessione FTP in Wireshark
✅ Identificare i campi dell'intestazione UDP e il funzionamento utilizzando una cattura di sessione TFTP in Wireshark

---

## 📡 **Lab 1: Analisi della Stretta di Mano TCP a Tre Vie**

### 🔹 **Parte 1: Preparazione degli Host per la Cattura del Traffico**
1. **Installazione di Wireshark**
   - Se non installato, scaricare Wireshark da [qui](https://www.wireshark.org/download.html) e installarlo.
   - Avviare Wireshark e selezionare l'interfaccia di rete attiva.

2. **Avvio della Cattura del Traffico**
   - Aprire il browser e visitare un sito web (ad esempio, `http://example.com`).
   - Wireshark inizierà a catturare i pacchetti generati dalla richiesta HTTP.

### 🔹 **Parte 2: Analisi dei Pacchetti con Wireshark**
1. **Filtrare i Pacchetti TCP**
   - Nel campo di ricerca dei filtri di Wireshark, digitare `tcp` per isolare i pacchetti TCP.
   - Individuare la sequenza di handshake TCP (SYN, SYN-ACK, ACK).

2. **Analizzare i Pacchetti**
   - **SYN**: Il client invia un pacchetto di sincronizzazione per avviare la connessione.
   - **SYN-ACK**: Il server risponde confermando la richiesta.
   - **ACK**: Il client conferma la connessione stabilita.

3. **Salvataggio della Cattura**
   - Esportare i pacchetti in un file `.pcap` per ulteriori analisi o documentazione.

### 🔹 **Parte 3: Visualizzazione con tcpdump**
1. **Eseguire tcpdump**
   - Aprire il terminale e digitare:
     ```bash
     sudo tcpdump -i eth0 -n port 80
     ```
   - Questo comando cattura il traffico HTTP sulla porta 80.

2. **Analizzare il Log di tcpdump**
   - I pacchetti catturati mostreranno il processo di handshake TCP con dettagli sulle porte e sugli IP coinvolti.

---

## 🎯 **Lab 2: Esaminazione delle Catture TCP e UDP**

### 🔸 **Parte 1: Analisi di una Sessione FTP (TCP)**
1. **Avviare la Connessione FTP**
   - Connettersi a un server FTP tramite terminale:
     ```bash
     ftp ftp.example.com
     ```
   - Effettuare il login e scaricare un file di test.

2. **Catturare il Traffico FTP con Wireshark**
   - Applicare il filtro `tcp.port == 21` per isolare i pacchetti FTP.
   - Osservare i pacchetti che trasmettono i comandi di autenticazione e di trasferimento file.

3. **Analizzare i Pacchetti**
   - Identificare la sequenza di handshake e i segmenti dati.
   - Esaminare i flag TCP utilizzati per la trasmissione affidabile dei dati.

### 🔸 **Parte 2: Analisi di una Sessione TFTP (UDP)**
1. **Avviare un Server TFTP**
   - Installare un server TFTP e avviare la condivisione di file:
     ```bash
     sudo apt install tftpd-hpa
     ```
   - Avviare la connessione da un client con:
     ```bash
     tftp 192.168.1.100
     get file.txt
     ```

2. **Catturare il Traffico TFTP con Wireshark**
   - Applicare il filtro `udp.port == 69` per isolare il traffico TFTP.
   - Osservare la sequenza di pacchetti di richiesta e risposta.

3. **Analizzare i Pacchetti**
   - Notare l'assenza di handshake e controllo di errore tipici del protocollo UDP.
   - Esaminare il trasferimento dati basato su pacchetti senza garanzia di recapito.

---

## 📊 **Risultati e Conclusioni**

- **TCP**: L'handshake a tre vie garantisce l'affidabilità della connessione. Il protocollo utilizza meccanismi di conferma e ritrasmissione per garantire l'integrità dei dati.
- **UDP**: Senza handshake, UDP è più veloce ma meno affidabile. È ideale per applicazioni che tollerano la perdita di pacchetti, come streaming e VoIP.
- **Wireshark & tcpdump**: Entrambi gli strumenti forniscono insight preziosi sulle comunicazioni di rete, essenziali per l'analisi forense e la cybersecurity.

🔹 Questo laboratorio fornisce una comprensione approfondita dei meccanismi di trasporto dati e delle tecniche di cattura del traffico di rete. L'uso di strumenti avanzati come Wireshark e tcpdump è fondamentale per qualsiasi professionista della cybersecurity.
