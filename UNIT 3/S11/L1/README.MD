# 📝 Consegna S11/L1
# 🌐 Remediation e Mitigazione

Benvenuto! Questo documento ti guiderà attraverso il processo di remediation e mitigazione per affrontare le minacce di **Phishing** e **DoS (Denial of Service)**. 🚀

---

## Introduzione

L'obiettivo di questa esercitazione è analizzare e risolvere le minacce seguendo due approcci fondamentali:
- **Remediation**: Risolvere completamente le vulnerabilità con azioni mirate e approfondite.
- **Mitigazione**: Ridurre il rischio e l'impatto delle vulnerabilità fino a quando non si implementano soluzioni definitive.

---

## **Parte 1: Minaccia di Phishing**

### 📌 **Cos'è il phishing?**
La minaccia del phishing rappresenta una delle tecniche di attacco più diffuse e insidiose. Attraverso email fraudolente, siti web fasulli o tecniche di social engineering, gli attaccanti cercano di ingannare gli utenti per ottenere informazioni sensibili o indurre azioni dannose.

Spesso, queste email imitano comunicazioni ufficiali di enti affidabili, come banche o colleghi.

### 🔍 **Analisi del rischio**
#### **Impatto potenziale**:
- **Compromissione di account aziendali**: accesso non autorizzato a risorse e sistemi critiche/i.
- **Diffusione di malware**: ransomware o spyware che rappresentano una seria minaccia per l'azienda.
- **Danni reputazionali**: perdita di fiducia da parte di clienti e partner.

#### **Risorse a rischio**:
- Account email aziendali.
- Database contenenti dati sensibili.
- Credenziali di accesso ai sistemi gestionali e finanziari.

### 🛠 **Piano di remediation**

- Per affrontare efficacemente un attacco di phishing è necessario:

1. Bloccare immediatamente le email sospette configurando filtri anti-phishing.
2. Informare tempestivamente i dipendenti sull'attacco in corso.
3. Monitorare i sistemi aziendali per individuare eventuali attività anomale.

#### **1. Identificazione e blocco delle email sospette**
- Configurare filtri avanzati anti-phishing utilizzando strumenti come:
  - **Microsoft Defender for Office 365** o **Proofpoint**.
- Abilitare e configurare i protocolli SPF, DKIM e DMARC per prevenire spoofing dei domini aziendali.
- Creare regole personalizzate per individuare pattern comuni nelle email fraudolente.

#### **2. Formazione e sensibilizzazione dei dipendenti**
- Organizzare workshop regolari per insegnare ai dipendenti a riconoscere email sospette.
- Fornire linee guida dettagliate su come segnalare un tentativo di phishing.
- Eseguire simulazioni periodiche di phishing per valutare la consapevolezza dei dipendenti.

#### **3. Monitoraggio continuo dei sistemi**
- Implementare un **SIEM (Security Information and Event Management)** per analizzare i log di accesso e individuare attività anomale.
- Integrare strumenti di rilevamento delle minacce come **CrowdStrike** o **Carbon Black** per identificare compromissioni in tempo reale.

#### **4. Pulizia e recupero**
- Revocare immediatamente le credenziali compromesse.
- Eseguire scansioni di sicurezza approfondite su endpoint e server per rilevare eventuali malware installati.
- Applicare patch di sicurezza a tutti i sistemi vulnerabili.

### 🌐 **Mitigazione dei rischi residui**
- Implementare **autenticazione a due fattori (2FA)** su tutti gli account critici per ridurre il rischio di accessi non autorizzati. 🔒
- Effettuare **backup regolari** dei dati sensibili, assicurandosi che siano crittografati e conservati offline.
- Condurre test periodici di simulazioni phishing per verificare la prontezza dei dipendenti.

---

## **Parte 2: Attacco DoS (Denial of Service)**

### 📌 **Cos'è un attacco DoS?**
Un attacco DoS mira a rendere indisponibili i servizi di un'azienda sovraccaricando i server con traffico eccessivo. Questo può includere:
- Saturazione della larghezza di banda.
- Esaurimento delle risorse hardware come CPU e RAM.

In caso di attacco DDoS, una botnet distribuita amplifica l'effetto, rendendo più difficile la mitigazione.

### 🔍 **Analisi del rischio**

Un attacco DoS funziona saturando le risorse di rete o i server, provocandone l'inaccessibilità per gli utenti legittimi. Talvolta, gli attacchi sono distribuiti (DDoS) e sfruttano una botnet per amplificare l'impatto.

#### **Impatto potenziale**:
- **Interruzione dei servizi critici**: impossibilità per i clienti di accedere a portali e applicazioni aziendali.
- **Danni economici**: perdita di entrate e costi di ripristino.
- **Danni reputazionali**: disservizi che minano la fiducia dei clienti.

#### **Servizi vulnerabili**:
- Server web.
- Sistemi di pagamento online.
- Applicazioni interne o esterne critiche.
- Database aziendali.

### 🛠 **Piano di remediation**

Per contrastare un attacco DoS:

1. Identificare le fonti del traffico malevolo analizzando i log di rete.
2. Mitigare il traffico malevolo configurando regole firewall.
3. Collaborare con il provider di rete per attivare servizi anti-DDoS come Cloudflare o Akamai.

#### **1. Identificazione delle fonti dell'attacco**
- Analizzare i log di rete utilizzando strumenti come **Wireshark** o **Zeek** per identificare IP malevoli.
- Isolare e bloccare le sorgenti di traffico sospetto tramite regole di firewall dinamiche.
- Contattare il provider di rete per ottenere supporto nella mitigazione del traffico dannoso.

#### **2. Mitigazione del traffico malevolo**
- Configurare un **Web Application Firewall (WAF)** per filtrare le richieste anomale e proteggere le applicazioni web.
- Utilizzare soluzioni anti-DDoS fornite da terze parti, come **Cloudflare** o **AWS Shield**.
- Implementare blackhole routing per reindirizzare il traffico sospetto lontano dai server principali.

#### **3. Distribuzione del carico e resilienza**
- Implementare un **load balancer** (es. HAProxy) per distribuire uniformemente il traffico legittimo.
- Utilizzare una **Content Delivery Network (CDN)** per ridurre il carico sui server principali e migliorare le prestazioni.
- Aumentare la capacità dei server per gestire picchi di traffico improvvisi.

#### **4. Recupero e miglioramento**
- Ripristinare i servizi critici utilizzando backup recenti.
- Aggiornare costantemente le regole di firewall e le configurazioni di rete per prevenire attacchi futuri.
- Condurre un'analisi post-incidente per identificare punti deboli e migliorare le difese.

### 🌐 **Mitigazione dei rischi residui**
- Monitorare continuamente il traffico di rete con strumenti di analisi avanzati. 📊
- Organizzare test periodici di simulazione DoS per valutare l'efficacia delle misure di mitigazione.
- Creare piani di emergenza dettagliati per garantire la continuità operativa durante attacchi futuri.

---

## **Conclusioni**

Le minacce di phishing e DoS rappresentano rischi significativi per le aziende moderne. Attraverso una combinazione di **formazione**, **strumenti tecnologici avanzati** e **strategie di monitoraggio continuo**, è possibile mitigare efficacemente tali rischi e proteggere le infrastrutture aziendali.

### **Punti chiave**
1. **Phishing**: La prevenzione è basata su formazione, filtri avanzati e autenticazione forte.
2. **DoS**: La resilienza si costruisce con soluzioni scalabili come load balancer, CDN e firewall avanzati.

Adottando queste strategie, le aziende possono garantire una maggiore continuità operativa e una difesa proattiva contro le minacce future. 🔐