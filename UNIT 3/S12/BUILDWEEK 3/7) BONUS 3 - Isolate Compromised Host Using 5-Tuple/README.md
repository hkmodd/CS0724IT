# 🚀 Isolamento di un Host Compromesso con 5-Tuple 🔒

## 📌 Obiettivo dell'esercizio  
Utilizzare **Security Onion** 🛡️ per investigare un exploit, identificare un host compromesso e isolarlo, sfruttando il concetto delle **5-Tuple** 🔍.

---

## 📖 Concetti chiave  
- **Security Onion** 🏰: piattaforma open-source per il monitoraggio della sicurezza e la risposta agli incidenti.  
- **5-Tuple** 🎯: cinque elementi utilizzati per identificare una sessione di rete:  
  1. **📌 Indirizzo IP sorgente**
  2. **📌 Indirizzo IP destinazione**
  3. **🔢 Porta sorgente**
  4. **🔢 Porta destinazione**
  5. **📡 Protocollo (TCP, UDP, ICMP, ecc.)**  

---

## 🛠 Passaggi dettagliati  

### 🟢 1. Avvio dell’ambiente Security Onion 🏁  
1. **⚡ Accendi la macchina virtuale con Security Onion.**  
2. **🌐 Accedi alla dashboard Security Onion:**
   - Apri il browser 🖥️ e inserisci l’IP della macchina Security Onion (es. `https://<IP-SecurityOnion>`).  
   - Inserisci le credenziali dell'amministratore e accedi 🔑.  

---

### 🟢 2. Esplorazione degli avvisi in Sguil 🚨  
1. **📂 Apri Sguil e accedi:**  
   - Seleziona tutte le interfacce disponibili.  
   - Clicca su **Start Sguil** ▶️.  

2. **🔍 Cerca un avviso sospetto:**  
   - Filtra per `GPL ATTACK_RESPONSE id check returned root` (indica un attacco che ha ottenuto accesso root).  
   - Identifica gli indirizzi IP coinvolti (es. `SRC: 209.165.201.17` → `DST: 209.165.200.235`).  

3. **📝 Esamina il contenuto dell’avviso:**  
   - Abilita **Show Packet Data** e **Show Rule** per ulteriori dettagli.  
   - Clicca con il tasto destro sull’ID dell’avviso e seleziona **Transcript** 📜.  
   - Analizza i comandi eseguiti dall’attaccante (es. `whoami`, `cat /etc/passwd`).  

---

### 🟢 3. Analisi avanzata con Wireshark 🔎  
1. **📡 Apri Wireshark direttamente da Sguil:**  
   - Fai clic con il tasto destro sull’evento e seleziona **Wireshark**.  

2. **📊 Analizza la sessione compromessa:**  
   - Clicca con il tasto destro su un pacchetto → **Follow** → **TCP Stream**.  
   - Osserva il traffico tra attaccante e vittima.  

3. **⚠️ Individua attività sospette:**  
   - Cerca l’uso di `sudo` o `su` per vedere se l’attaccante ha ottenuto privilegi elevati.  
   - Analizza eventuali file scaricati o modificati.  

---

### 🟢 4. Analisi dei log con Kibana 📑  
1. **📂 Accedi a Kibana:**  
   - Apri **Kibana** dalla dashboard di Security Onion.  
   - Vai su **Discover** e seleziona il periodo di tempo corretto.  

2. **📌 Ricerca eventi correlati:**  
   - Inserisci nella barra di ricerca:  
     ```elasticsearch
     event.category: network AND event.type: connection
     ```  
   - Individua connessioni tra gli IP sospetti.  

3. **📊 Esamina i dettagli delle connessioni:**  
   - Filtra per `209.165.201.17` per vedere tutte le attività dell'attaccante.  
   - Controlla i protocolli utilizzati (SSH, HTTP, ecc.).  

---

### 🟢 5. Identificazione delle 5-Tuple dell’attacco 📌  
Dopo aver individuato l’evento compromettente, estrai le **5-Tuple**:  
- **📍 IP sorgente**: `209.165.201.17`  
- **📍 IP destinazione**: `209.165.200.235`  
- **🔢 Porta sorgente**: `45678`  
- **🔢 Porta destinazione**: `22` (SSH)  
- **📡 Protocollo**: `TCP`  

---

### 🟢 6. Isolamento dell’host compromesso 🚫  
Dopo aver confermato che l'host `209.165.201.17` è malevolo, esegui queste azioni per bloccarlo:  
1. **🚧 Blocca l'IP nel firewall:**  
   ```bash
   sudo iptables -A INPUT -s 209.165.201.17 -j DROP
   ```  
   - Questo impedisce qualsiasi comunicazione con l'IP malevolo.  

2. **🛑 Blocca la porta 22 se non necessaria:**  
   ```bash
   sudo iptables -A INPUT -p tcp --dport 22 -j DROP
   ```  

3. **📸 Segnala l’incidente e raccogli prove:**  
   - Cattura screenshot di Sguil, Wireshark e Kibana per documentare l’attacco.  
   - Prepara un report con gli eventi principali.  

---

## ✅ Risultati e Conclusione 🎯  
✔ Identificato un attacco **SSH Root Exploit**.  
✔ Tracciate le azioni dell’attaccante utilizzando **Security Onion**.  
✔ Bloccata la minaccia utilizzando **iptables**.  
