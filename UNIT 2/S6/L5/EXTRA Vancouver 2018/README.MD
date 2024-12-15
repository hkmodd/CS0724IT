# 🛡️ Relazione sul Progetto di Penetration Testing

## 📋 **Descrizione Generale**
Questa relazione descrive i passi eseguiti durante l'analisi e l'attacco alla macchina virtuale (VM) fornita dal professore. Abbiamo ottenuto accesso root tramite un approccio metodico utilizzando diverse tecniche di enumerazione e attacco.

---

## ⚙️ **Configurazione dell'Ambiente**
1. **Importazione della VM**: 
   - Abbiamo importato l'OVA fornitaci dal professore.
   - La VM è stata avviata correttamente su VirtualBox/VMware.

2. **Scansione dell'indirizzo IP**:
   - Per identificare l'IP della VM assegnato dal router di casa, abbiamo utilizzato **Nmap**:
     ```bash
     nmap -sn 192.168.1.0/24
     ```
   - L'IP rilevato della VM target è **192.168.1.170**.

---

## 🔍 **Fase di Scansione e Enumerazione**
### 1️⃣ **Scansione delle Porte**
- Abbiamo eseguito una scansione con Nmap per identificare i servizi attivi:
  ```bash
  nmap -sV -p- 192.168.1.170
  ```
- **Risultato**: Porta **FTP** attiva.

### 2️⃣ **Accesso FTP Anonimo**
- Dopo aver rilevato il servizio FTP, abbiamo provato un accesso anonimo:
  ```bash
  ftp 192.168.1.170
  ```
- L'accesso è stato consentito come utente anonimo.
- Nella directory `public`, abbiamo trovato il file **users.txt.bk**, contenente una lista di nomi utente.

---

## 🔐 **Tentativi di Accesso ai Servizi**
### 3️⃣ **Enumerazione con WordPress**
- Dopo aver testato i nomi utente sui servizi attivi, abbiamo scoperto delle credenziali valide per **WordPress**.
- Successivamente, abbiamo provato a caricare una **reverse shell PHP** riuscendo ad ottenerla, ma ci siamo ritrovati limitati all'utente **www-data**.

### 4️⃣ **Attacco Dizionario con Hydra su SSH** 🚀
Per bypassare le limitazioni, abbiamo deciso di effettuare un attacco di dizionario con **Hydra** sul servizio SSH, utilizzando il file `rockyou.txt`.

**Comando utilizzato**:
```bash
hydra -l anne -P /usr/share/wordlists/rockyou.txt -t 64 -V ssh://192.168.1.170
```

- **Risultato**: Abbiamo trovato la combinazione:
  - **Username**: `anne`
  - **Password**: `princess`

---

## 🏆 **Accesso Root**
1. Dopo aver ottenuto le credenziali, abbiamo eseguito il login SSH:
   ```bash
   ssh anne@192.168.1.170
   ```
2. Abbiamo verificato se l'utente aveva privilegi sudo:
   ```bash
   sudo su
   ```
3. Inserendo nuovamente la password, siamo diventati **root**.

### 📌 **Verifica Utente Root**
Per confermare l'accesso root, abbiamo utilizzato i seguenti comandi:
```bash
whoami
id
```
- **Output**: `root` ✅

---

## 🎯 **Conclusione**
Abbiamo ottenuto accesso completo alla macchina target partendo da una fase di **enumerazione** fino all'ottenimento dei privilegi **root**. La metodologia seguita è stata:

1. Identificazione dei servizi attivi con Nmap.
2. Accesso anonimo FTP e raccolta di informazioni.
3. Test dei servizi con le credenziali trovate.
4. Attacco SSH con **Hydra** utilizzando la potenza bruta del nostro hardware.
5. Escalation di privilegi per ottenere **root access**.

🚀 **Missione completata con successo!**
