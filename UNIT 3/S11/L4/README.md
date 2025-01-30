# 📝 Consegna S11/L3
# 🔥 Cisco CyberOps - 2
## 🛡️ Analisi del Traffico DNS con Wireshark

## 📌 Introduzione
Questo documento descrive dettagliatamente l'analisi del traffico **DNS** utilizzando **Wireshark**, con un focus sulle query e sulle risposte DNS. L'obiettivo è comprendere come i dispositivi comunicano con i server DNS per risolvere i nomi di dominio e identificare eventuali vulnerabilità nel protocollo.

## 🎯 Obiettivi
1. **Catturare il traffico DNS** 🔍
2. **Esplorare il traffico delle query DNS** 📡
3. **Esplorare il traffico delle risposte DNS** 📬

---

## 📥 Prerequisiti
- Un PC con **Wireshark** installato 🖥️
- Accesso a Internet 🌐
- Permessi di amministratore per catturare i pacchetti di rete ⚙️

---

## 🕵️‍♂️ 1. Cattura del Traffico DNS

### 📥 Installazione di Wireshark
Se non hai già Wireshark installato:
1. Scarica l'ultima versione da [Wireshark.org](https://www.wireshark.org/).
2. Installa il software seguendo le istruzioni a schermo. **(NB: Non installare USBPcap se non necessario).**
3. Avvia **Wireshark**.

### 🎥 Avvio della Cattura del Traffico
1. **Seleziona un'interfaccia di rete attiva** (es. Ethernet o Wi-Fi).
2. **Svuota la cache DNS** per evitare che i risultati siano già risolti:
   - Su **Windows**: Apri il prompt dei comandi e digita:
     ```sh
     ipconfig /flushdns
     ```
   - Su **Linux** (dipende dal servizio in uso):
     ```sh
     sudo systemd-resolve --flush-caches
     ```
   - Su **macOS**:
     ```sh
     sudo killall -HUP mDNSResponder
     ```
3. **Avvia la cattura** su Wireshark e visita alcuni siti web per generare traffico DNS.

---

## 🔎 2. Analisi delle Query DNS

### 📌 Filtraggio dei Pacchetti
Dopo aver catturato il traffico, filtriamo solo le richieste DNS:
```sh
udp.port == 53
```
Ciò ci consente di isolare solo il traffico DNS (che utilizza la porta 53 su UDP).

### 📊 Interpretazione dei Pacchetti di Query
Un tipico pacchetto DNS di query include:
- **Transaction ID**: un identificatore univoco per la richiesta.
- **Flags**: campo che indica il tipo di richiesta.
- **Query Name**: il nome del dominio richiesto (es. `www.google.com`).
- **Query Type**: indica se è una richiesta **A** (IPv4) o **AAAA** (IPv6).

### 📜 Esempio di Query DNS
Analizzando i dettagli di una query in Wireshark, potremmo vedere:
```
Frame 1: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
Ethernet II, Src: 00:1a:2b:3c:4d:5e, Dst: ff:ff:ff:ff:ff:ff
Internet Protocol Version 4, Src: 192.168.1.10, Dst: 8.8.8.8
User Datagram Protocol, Src Port: 49152, Dst Port: 53
Domain Name System (query)
    Transaction ID: 0x1234
    Flags: 0x0100 (Standard query)
    Queries: 1
    Query Name: www.google.com
    Query Type: A (Host Address)
```

**📌 Osservazioni**
- La richiesta proviene dall'IP **192.168.1.10** e viene inviata al DNS **8.8.8.8** (Google DNS).
- Viene effettuata una richiesta di tipo **A**, ovvero un indirizzo IPv4.

---

## 📩 3. Analisi delle Risposte DNS

### 🎯 Filtraggio delle Risposte
Per isolare le risposte DNS, utilizziamo il filtro:
```sh
dns.flags.response == 1
```

### 📜 Esempio di Risposta DNS
Ecco un esempio di risposta DNS a una query:
```
Frame 2: 98 bytes on wire (784 bits), 98 bytes captured (784 bits)
Ethernet II, Src: 8.8.8.8, Dst: 192.168.1.10
Internet Protocol Version 4, Src: 8.8.8.8, Dst: 192.168.1.10
User Datagram Protocol, Src Port: 53, Dst Port: 49152
Domain Name System (response)
    Transaction ID: 0x1234
    Flags: 0x8180 (Standard query response, No error)
    Questions: 1
    Answer RRs: 1
    Queries:
        Query Name: www.google.com
    Answers:
        Name: www.google.com
        Type: A (Host Address)
        Address: 142.250.184.100
```

### 📌 Osservazioni
- Il server DNS **8.8.8.8** ha risposto fornendo l'indirizzo **142.250.184.100** per `www.google.com`.
- Il campo `Flags: 0x8180` indica che la richiesta è stata processata con successo.

---

## 📌 Conclusione
L'analisi del traffico DNS con Wireshark è uno strumento potente per comprendere il funzionamento del protocollo, identificare anomalie e rilevare eventuali attacchi. 🚀
 
🔍 **Strumenti Utilizzati:** Wireshark, nslookup, dig  
📅 **Data di Creazione:** 30 gennaio 2025  
📌 **Scopo:** Analisi avanzata del traffico DNS e identificazione delle minacce 🚀  

---

💡 _"Conoscere il traffico di rete è il primo passo per proteggere la propria infrastruttura!"_ 🔐
