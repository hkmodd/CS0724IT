# EXTRA S6/L5
# 🛡️Vancouver 2018 Exploitation report

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
- Nella directory `public`, ho trovato il file **users.txt.bk**, contenente una lista di nomi utente: `anne`, `john`, e altri.

### 3️⃣ **Scoperta di WordPress**
- Ho notato durante la scansione Nmap che la porta **80** era aperta e ospitava un servizio web HTTP.
- Utilizzando **Gobuster**, ho eseguito una scansione più aggressiva per individuare directory nascoste:
  ```bash
  gobuster dir -u http://192.168.1.170 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt -t 50
  ```
- **Risultato**: La scansione ha rilevato la presenza del file **robots.txt**:
  ```
  /robots.txt           (Status: 200) [Size: 43]
  ```
- Ho scaricato il file **robots.txt** per esaminarlo:
  ```bash
  curl http://192.168.1.170/robots.txt
  ```
- Il contenuto di **robots.txt** ha rivelato la directory nascosta **/backup_wordpress**.
- Ho visitato l'indirizzo `http://192.168.1.170/backup_wordpress` per esaminare il sito.
- Per ulteriore conferma, ho lanciato una scansione mirata con **WPScan**:
  ```bash
  wpscan --url http://192.168.1.170/backup_wordpress --api-token Tc1sdQWKLxFRktkneIXAx6CiY5a98HdnyhYaBr34058 --enumerate u --passwords /usr/share/wordlists/rockyou.txt
  ```
- **Risultato**: Ho trovato la combinazione:
  - **Username**: `john`
  - **Password**: `enigma`

- Utilizzando queste credenziali, mi sono loggato al pannello amministrativo di WordPress.
- Ho caricato un **plugin malevolo** contenente una **reverse shell PHP**, ottenendo una connessione backdoor al sistema.
- Tuttavia, mi sono ritrovato limitato all'utente **www-data**, con privilegi bassi.

---

## 🔐 **Tentativi di Accesso ai Servizi**
### 4️⃣ **Attacco Dizionario con Hydra su SSH** 🚀
- Dalla lista di utenti recuperata dal file `users.txt.bk`, ho deciso di testare ciascun nome utente per verificare quale avesse credenziali valide per accedere tramite SSH, utilizzando **Hydra**.
- Per ciascun utente nella lista, ho effettuato un attacco di dizionario utilizzando il file `rockyou.txt`, eseguendo il test iterativamente.

**Comando utilizzato**:
```bash
hydra -l <username> -P /usr/share/wordlists/rockyou.txt -t 64 -V ssh://192.168.1.170
```

- **Risultato**: Ho trovato la combinazione:
  - **Username**: `anne`
  - **Password**: `princess`

# SUCCESSO!

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

![Success](./RootSuccess.png)

---

## 🎯 **Conclusione**
Ho ottenuto accesso completo alla macchina target partendo da una fase di **enumerazione** fino all'ottenimento dei privilegi **root**. La metodologia seguita è stata:

1. Identificazione dei servizi attivi con Nmap.
2. Accesso anonimo FTP e raccolta di informazioni.
3. Scansione delle directory con **Gobuster** e individuazione del file **robots.txt**.
4. Identificazione della directory **/backup_wordpress** nascosta.
5. Login al pannello WordPress con credenziali **john/enigma** trovate tramite **WPScan**.
6. Caricamento di una **reverse shell** tramite un plugin malevolo.
7. Test mirato di accesso SSH tramite Hydra, utilizzando la lista utenti ottenuta e scoprendo le credenziali valide per `anne`.
8. Escalation di privilegi per ottenere **root access**.

🚀 **Missione completata con successo!**
