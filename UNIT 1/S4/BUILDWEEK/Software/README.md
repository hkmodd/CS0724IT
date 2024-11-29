# CerberusAIO - Rapporto di analisi - Azienda Theta 🛡️

Grazie al software progettato in casa CyberCerberus abbiamo stilato il report **CerberusAIO**. Questo documento descrive i risultati ottenuti durante i test, evidenziando le vulnerabilità identificate e fornendo raccomandazioni per migliorare la sicurezza.

---

## 📊 Risultati della scansione delle porte

Il modulo di **Port Scanner** ha individuato le seguenti porte aperte:

| Porta | Protocollo  | Descrizione                               |
|-------|-------------|-------------------------------------------|
| 21    | FTP         | File Transfer Protocol (non cifrato)     |
| 22    | SSH         | Secure Shell                             |
| 23    | Telnet      | Accesso remoto non sicuro                |
| 25    | SMTP        | Simple Mail Transfer Protocol            |
| 53    | DNS         | Domain Name System                       |
| 80    | HTTP        | HyperText Transfer Protocol              |
| 111   | RPC         | Remote Procedure Call                    |
| 139   | NetBIOS     | Network Basic Input/Output System        |
| 445   | SMB         | Server Message Block                     |
| 512, 513, 514 | Rlogin e protocolli remoti | Accesso remoto non sicuro            |

### ⚠️ **Rischi Identificati**
1. **Telnet (Porta 23)** e **FTP (Porta 21)** trasmettono dati in chiaro, rendendoli vulnerabili a intercettazioni e attacchi *man-in-the-middle*.
2. La presenza di **SMB (Porta 445)** e **NetBIOS (Porta 139)** può facilitare attacchi di enumerazione e accesso non autorizzato.
3. **RPC (Porta 111)** e protocolli remoti come **Rlogin (512-514)** sono noti per avere vulnerabilità se non configurati correttamente.

### ✅ **Raccomandazioni**
- **🔒 Disattivare Telnet e FTP**: Sostituirli rispettivamente con **SSH** e **SFTP** per garantire connessioni sicure.
- **🚫 Limitare l'accesso alle porte non necessarie**: Utilizzare un firewall o regole di accesso rigorose.
- **📉 Monitoraggio continuo**: Implementare strumenti di monitoraggio per identificare attività sospette sulle porte.

---

## 🌐 Analisi delle richieste HTTP

Il modulo di **HTTP Request Analyzer** è stato utilizzato per testare il comportamento del server in risposta a vari metodi HTTP. È stata rilevata una vulnerabilità critica sulla pagina **/phpMyAdmin**.

### 🔍 **Osservazioni**
- La pagina **/phpMyAdmin** risponde con lo status code **200 (OK)** a TUTTI i metodi HTTP testati:
  - **GET**, **POST**, **PUT**, **DELETE**.
- Questo comportamento è anomalo e pericoloso, considerando che **phpMyAdmin** è un'interfaccia per la gestione di database.

### ⚠️ **Rischi Identificati**
1. **Accesso non autorizzato**: Rispondendo positivamente a tutti i metodi, potrebbe essere possibile eseguire modifiche o eliminazioni non autorizzate.
2. **Esposizione del database**: La mancanza di restrizioni mette a rischio l'integrità, la disponibilità e la riservatezza dei dati.

### ✅ **Raccomandazioni**
- **🔒 Proteggere /phpMyAdmin**: Limitare l'accesso tramite autenticazione e configurare un'allowlist di IP.
- **⚙️ Limitare i metodi HTTP**: Accettare solo metodi strettamente necessari, come **GET** e **POST**.
- **🔐 Rimuovere l'accesso pubblico a phpMyAdmin**, se non strettamente necessario.

---

## 🧪 Valutazione dello strumento

CerberusAIO ha dimostrato la sua efficacia come strumento per l'identificazione di vulnerabilità:
- **🔍 Port Scanner**: Ha fornito un'analisi dettagliata delle porte aperte, evidenziando configurazioni insicure.
- **🌐 HTTP Request Analyzer**: Ha permesso di individuare comportamenti anomali e vulnerabilità critiche del server.

---

## 📌 Conclusione

CerberusAIO rappresenta un alleato indispensabile per la sicurezza delle reti e dei server web. Le vulnerabilità identificate sottolineano l'importanza di:
- Configurare correttamente i protocolli e le porte.
- Implementare rigide politiche di accesso e monitoraggio continuo.

### 🎯 **Prossimi passi**
- 🛠️ Applicare le raccomandazioni per mitigare i rischi.
- 🚀 Continuare a utilizzare CerberusAIO per verifiche regolari della sicurezza.

---

> 💡 **Nota**: Utilizzare questo strumento nel rispetto delle leggi vigenti e solo su sistemi di cui si possiede autorizzazione. CerberusAIO non si assume alcuna responsabilità per usi impropri.
