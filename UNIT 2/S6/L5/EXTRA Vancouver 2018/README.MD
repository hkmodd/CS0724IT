# 🛡️ Relazione sul Progetto di Penetration Testing

## 📋 **Descrizione Generale**
Questa relazione descrive i passi eseguiti durante l'analisi e l'attacco alla macchina virtuale (VM) fornita dal professore. Ho ottenuto accesso root tramite un approccio metodico utilizzando diverse tecniche di enumerazione e attacco.

---

## ⚙️ **Configurazione dell'Ambiente**
1. **Importazione della VM**: 
   - Ho importato l'OVA fornitami dal professore.
   - La VM è stata avviata correttamente su VirtualBox/VMware.

2. **Scansione dell'indirizzo IP**:
   - Per identificare l'IP della VM assegnato dal router di casa, ho utilizzato **Nmap**:
     ```bash
     nmap -sn 192.168.1.0/24
     ```
   - L'IP rilevato della VM target è **192.168.1.170**.

---

## 🔍 **Fase di Scansione e Enumerazione**
### 1️⃣ **Scansione delle Porte**
- Ho eseguito una scansione con Nmap per identificare i servizi attivi:
  ```bash
  nmap -sV -p- 192.168.1.170
  ```
- **Risultato**: Porta **FTP** attiva.

### 2️⃣ **Accesso FTP Anonimo**
- Dopo aver rilevato il servizio FTP, ho provato un accesso anonimo:
  ```bash
  ftp 192.168.1.170
  ```
- L'accesso è stato consentito come utente anonimo.
- Nella directory `public`, ho trovato il file **users.txt.bk**, contenente una lista di nomi utente.

### 3️⃣ **Scoperta di WordPress**
- Ho notato durante la scansione Nmap che la porta **80** era aperta e ospitava un servizio web HTTP.
- Utilizzando **Gobuster**, ho scansionato le directory del server per individuare percorsi nascosti:
  ```bash
  gobuster dir -u http://192.168.1.170 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
  ```
- **Risultato**: La scansione ha rivelato la presenza della directory **/wordpress**, confermando un'installazione WordPress.
- Ho visitato l'indirizzo `http://192.168.1.170/wordpress` per esaminare il sito.
- Per ulteriore conferma, ho lanciato una scansione mirata con **WPScan**:
  ```bash
  wpscan --url http://192.168.1.170/wordpress --api-token Tc1sdQWKLxFRktkneIXAx6CiY5a98HdnyhYaBr34058
  ```
- Il risultato ha confermato la presenza di un'installazione WordPress vulnerabile.

---

## 🔐 **Tentativi di Accesso ai Servizi**
### 4️⃣ **Enumerazione con WordPress**
- Utilizzando **WPScan**, ho eseguito un'analisi del sito WordPress rilevando una **vulnerabilità del software** che mi ha permesso di individuare le credenziali di accesso:
  ```bash
  wpscan --url http://192.168.1.170/wordpress --enumerate u --passwords /usr/share/wordlists/rockyou.txt --api-token Tc1sdQWKLxFRktkneIXAx6CiY5a98HdnyhYaBr34058
  ```
- Dopo aver ottenuto le credenziali di accesso al pannello amministrativo, mi sono loggato su WordPress.
- Ho caricato un **plugin malevolo** contenente una **reverse shell PHP**, ottenendo una connessione backdoor al sistema.
- Tuttavia, mi sono ritrovato limitato all'utente **www-data**, con privilegi bassi. 

### 5️⃣ **Attacco Dizionario con Hydra su SSH** 🚀
Per bypassare le limitazioni, ho deciso di effettuare un attacco di dizionario con **Hydra** sul servizio SSH, utilizzando il file `rockyou.txt`.

**Comando utilizzato**:
```bash
hydra -l anne -P /usr/share/wordlists/rockyou.txt -t 64 -V ssh://192.168.1.170
```

- **Risultato**: Ho trovato la combinazione:
  - **Username**: `anne`
  - **Password**: `princess`

---

## 🏆 **Accesso Root**
1. Dopo aver ottenuto le credenziali, ho eseguito il login SSH:
   ```bash
   ssh anne@192.168.1.170
   ```
2. Ho verificato se l'utente aveva privilegi sudo:
   ```bash
   sudo su
   ```
3. Inserendo nuovamente la password, sono diventato **root**.

### 📌 **Verifica Utente Root**
Per confermare l'accesso root, ho utilizzato i seguenti comandi:
```bash
whoami
id
```
- **Output**: `root` ✅

---

## 🎯 **Conclusione**
Ho ottenuto accesso completo alla macchina target partendo da una fase di **enumerazione** fino all'ottenimento dei privilegi **root**. La metodologia seguita è stata:

1. Identificazione dei servizi attivi con Nmap.
2. Accesso anonimo FTP e raccolta di informazioni.
3. Scoperta e exploit su WordPress con **WPScan** e caricamento di una **reverse shell**.
4. Scansione delle directory con **Gobuster** per individuare percorsi nascosti.
5. Attacco SSH con **Hydra** utilizzando la potenza bruta del mio hardware.
6. Escalation di privilegi per ottenere **root access**.

🚀 **Missione completata con successo!**
