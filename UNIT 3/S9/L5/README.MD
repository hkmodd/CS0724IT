# 📐 Progetto S9/L5 📐
# 🛡️ Identificazione e Analisi degli IOC

## 📋 Descrizione
Questo progetto consiste nell'analisi di una cattura di rete per:
1. Identificare e analizzare eventuali **Indicatori di Compromissione (IOC)**.
2. Formulare ipotesi sui vettori di attacco potenzialmente utilizzati.
3. Consigliare azioni per mitigare l'impatto attuale e prevenire futuri attacchi.

Utilizzando **Wireshark**, abbiamo analizzato il traffico di rete e ricavato pattern sospetti che suggeriscono attività malevole.

---

## 🛠️ Procedura

### 1️⃣ Preparazione dell'Ambiente
1. **Installare Wireshark** su un sistema Kali Linux o equivalente.
2. **Caricare il file di cattura** nella directory di lavoro e aprirlo con Wireshark:
   ```bash
   wireshark <file>.pcap
   ```
3. Familiarizzarsi con i filtri base di Wireshark per isolare traffico specifico:
   - Traffico TCP:
     ```bash
     tcp
     ```
   - Traffico HTTP:
     ```bash
     http.request
     ```
   - Indirizzi IP sospetti:
     ```bash
     ip.addr == 192.168.200.150
     ```

---

### 2️⃣ Identificazione e Analisi degli IOC

#### 🛑 **Indicatori di Compromissione Identificati**
- **Traffico TCP RST/ACK ricorrente:**
  - Numerosi pacchetti `RST, ACK` indicano connessioni interrotte o chiuse forzatamente.
  - Questo pattern è spesso associato a **port scanning** o attività di riconoscimento.

- **Attività da/verso 192.168.200.150:**
  - Questo dispositivo interno invia traffico sospetto a `192.168.200.100`.
  - Potenziale indicazione di **compromissione interna** o malware.

- **Utilizzo di porte non standard (es. 4444):**
  - La porta `4444` è spesso utilizzata da exploit o server di comando e controllo (C2).

- **Pattern di traffico ripetitivo:**
  - Pacchetti con gli stessi intervalli temporali e sequenze possono indicare **attacchi brute force** o **esfiltrazione di dati**.

---

### 3️⃣ Ipotesi sui Potenziali Vettori di Attacco
In base agli IOC sopra descritti, i seguenti vettori di attacco sono stati ipotizzati:

1. **Port Scanning:**
   - Gli `RST, ACK` frequenti suggeriscono che un attore malevolo stia cercando porte aperte per identificare servizi vulnerabili.

2. **Exploitation tramite porte non standard:**
   - L'uso della porta `4444` potrebbe indicare l'esecuzione di payload malevoli attraverso strumenti come Metasploit.

3. **Command & Control (C2):**
   - Traffico ripetitivo verso un indirizzo interno compromesso potrebbe essere una comunicazione verso un server remoto di controllo.

4. **Compromissione Interna:**
   - Il dispositivo `192.168.200.150` potrebbe essere stato compromesso e utilizzato come pivot per ulteriori attacchi.

---

### 4️⃣ Azioni per Mitigare l'Impatto e Prevenire Attacchi Futuri

#### ✅ **Impatto Attuale**
1. **Isolare i Dispositivi Coinvolti:**
   - Rimuovere temporaneamente dalla rete i dispositivi `192.168.200.150` e `192.168.200.100` per prevenire ulteriori attività malevole.

2. **Bloccare IP e Porte Sospette:**
   - Configurare il firewall per bloccare il traffico sulle porte sospette:
     ```bash
     ufw deny from 192.168.200.150 to any
     ufw deny 4444
     ```

3. **Scansione dei Dispositivi Compromessi:**
   - Utilizzare strumenti come **ClamAV** o **chkrootkit** per rilevare ed eliminare eventuali malware.

#### 🔒 **Prevenzione Futura**
1. **Implementare un IDS/IPS:**
   - Installare sistemi come **Snort** o **Suricata** per monitorare e bloccare attività sospette in tempo reale.

2. **Aggiornare Regolarmente i Sistemi:**
   - Applicare patch di sicurezza e aggiornamenti per ridurre le vulnerabilità sfruttabili.

3. **Monitoraggio Continuo:**
   - Integrare un sistema SIEM per centralizzare e analizzare i log di rete e rilevare pattern sospetti.

4. **Educazione del Personale:**
   - Formare il personale sulla sicurezza informatica e sui rischi di phishing o attacchi social engineering.

5. **Segmentazione della Rete:**
   - Limitare la comunicazione tra dispositivi sensibili e altri sistemi attraverso VLAN.

---

## 📊 Risultati Attesi
- **IOC Identificati:**
  - Traffico TCP anomalo e utilizzo di porte sospette.
- **Ipotesi sui Vettori:**
  - Port scanning, exploit e Command & Control.
- **Azioni Preventive:**
  - Isolamento dei dispositivi, aggiornamento della sicurezza e monitoraggio continuo.

---
