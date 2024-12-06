# 📝 Consegna S5/L4
# <h1 align="center">🕵️‍♂️ Social Engineering e Tecniche di difesa 🛡️</h1>


Questo repository contiene la documentazione e i risultati degli esercizi svolti relativi al Social Engineering, alle tecniche di difesa e all'esplorazione delle vulnerabilità CVE. Ogni attività è stata completata utilizzando prompt ben strutturati per garantire risposte dettagliate e mirate.

# 🌟 Introduzione

La sicurezza informatica rappresenta una delle sfide più complesse del nostro tempo. In questo repository, vengono affrontati alcuni aspetti fondamentali legati al Social Engineering, alle tecniche di difesa e all'analisi delle vulnerabilità attraverso i CVE (Common Vulnerabilities and Exposures). Gli esercizi mirano a fornire una comprensione pratica e teorica di questi concetti, utilizzando prompt altamente strutturati per raccogliere risposte dettagliate e mirate.

Il Social Engineering è una delle metodologie più insidiose nel panorama degli attacchi informatici, sfruttando le debolezze umane per aggirare misure di sicurezza tecnologiche. Comprendere le sue tecniche e implementare strategie difensive è essenziale per proteggere informazioni sensibili. Inoltre, l'analisi delle vulnerabilità tramite i CVE consente di identificare criticità nei sistemi e mitigare rischi concreti, contribuendo a costruire infrastrutture più resilienti e sicure.

---

# <h1 align="center">🕵️‍♂️ Esercizio 1: Social Engineering</h1>

## 🎯 Obiettivo
Esplorare le tecniche di Social Engineering e imparare come difendersi da attacchi di questo tipo.

## 💡 Prompt utilizzato
```text
ChatGPT, potresti fornire una definizione dettagliata di Social Engineering e analizzare le tecniche più comuni utilizzate dagli attaccanti? Fornisci almeno tre esempi di attacchi reali documentati, spiegando il contesto e l'impatto di ciascuno.
```

## 📊 Risultati

### **🐟 Phishing**
**Descrizione:**  
Il phishing è un attacco in cui gli aggressori inviano comunicazioni (spesso email, messaggi SMS o attraverso social media) che sembrano provenire da una fonte legittima per indurre la vittima a fornire informazioni sensibili come credenziali di accesso, dati bancari o informazioni personali.

**Struttura dell'attacco:**
1. **📧 Preparazione:**  
   - L'attaccante crea un'email/messaggio con un layout che imita un'azienda o un'organizzazione legittima, come una banca, un provider di servizi online o un ente governativo.
   - Inserisce link che reindirizzano a siti web fasulli, molto simili a quelli ufficiali.

2. **⚠️ Esecuzione:**  
   - L'email/messaggio contiene un'esca, come un avviso urgente (es. "Il tuo account sarà sospeso se non confermi la tua identità").
   - La vittima clicca sul link e inserisce i propri dati personali sulla pagina fasulla.

3. **🔑 Conclusione:**  
   - L'attaccante utilizza le informazioni per accedere a sistemi o rubare denaro.

**Esempio pratico:**
- **Caso PayPal (2014):**  
  Un'email falsa, apparentemente inviata da PayPal, avvisava gli utenti di "attività sospette" sui loro account. I destinatari erano invitati a cliccare su un link e fornire le loro credenziali. Milioni di utenti caddero nella trappola, causando perdite finanziarie significative.
- **Come mitigare:**  
  - Verificare sempre il mittente dell'email.  
  - Non cliccare su link sospetti; digitare manualmente l'URL dell'organizzazione.  
  - Implementare un filtro antiphishing nei sistemi di posta elettronica.

---

### **🎣 Baiting**
**Descrizione:**  
Il baiting sfrutta la curiosità delle vittime, inducendole a interagire con dispositivi o file compromessi.

**Struttura dell'attacco:**
1. **🛠️ Preparazione:**  
   - L'attaccante lascia un dispositivo (es. una chiavetta USB infetta) in un luogo pubblico.
   - Il dispositivo ha un'etichetta intrigante, come "Confidenziale" o "Salari aziendali".

2. **🖱️ Esecuzione:**  
   - La vittima raccoglie il dispositivo e lo collega al proprio computer per curiosità.
   - Il dispositivo installa malware che consente agli aggressori di accedere al sistema.

3. **🕵️‍♂️ Conclusione:**  
   - Gli attaccanti accedono ai dati aziendali o controllano il sistema.

**Esempio pratico:**
- **Caso di un'azienda americana (2016):**  
  Chiavette USB infette furono lasciate nel parcheggio dell'azienda. Diversi dipendenti le inserirono nei computer aziendali, installando involontariamente malware che rubava dati sensibili.
- **Come mitigare:**  
  - Vietare ai dipendenti di collegare dispositivi non autorizzati.  
  - Implementare software di controllo su porte USB.  

---

### **🎭 Pretexting**
**Descrizione:**  
Nel pretexting, gli attaccanti creano un contesto credibile (o "pretesto") per ottenere informazioni sensibili dalla vittima.

**Struttura dell'attacco:**
1. **📋 Preparazione:**  
   - L'attaccante raccoglie informazioni sulla vittima (es. nome, posizione lavorativa, relazioni personali).
   - Costruisce un pretesto, come fingere di essere un tecnico IT o un rappresentante bancario.

2. **📞 Esecuzione:**  
   - Contatta la vittima via telefono, email o di persona.
   - Con un approccio amichevole e professionale, induce la vittima a rivelare informazioni sensibili.

3. **🔓 Conclusione:**  
   - Gli attaccanti utilizzano le informazioni per accedere a sistemi o compiere frodi.

**Esempio pratico:**
- **Caso di Verizon (2016):**  
  Un attaccante si finse un consulente IT e convinse un dipendente a fornire le credenziali di accesso aziendali. Questo portò a una violazione dei dati di milioni di clienti.
- **Come mitigare:**  
  - Educare i dipendenti a verificare sempre l'identità del richiedente.  
  - Implementare una policy aziendale che vieti di condividere credenziali via telefono o email.

---

### **🚪 Tailgating**
**Descrizione:**  
Il tailgating si verifica quando un attaccante si intrufola in un'area riservata seguendo una persona autorizzata.

**Struttura dell'attacco:**
1. **📍 Preparazione:**  
   - L'attaccante osserva l'ingresso di un edificio o di un'area protetta.
   - Identifica una vittima ignara, come un dipendente o un visitatore.

2. **🚶‍♂️ Esecuzione:**  
   - Si avvicina alla vittima, fingendo di aver dimenticato il badge o di essere un collaboratore esterno.
   - Segue la vittima attraverso l'accesso, sfruttando la cortesia delle persone.

3. **📂 Conclusione:**  
   - Una volta dentro, l'attaccante può rubare documenti, accedere a computer o compromettere l'infrastruttura.

**Esempio pratico:**
- **Caso RSA Security (2011):**  
  Un attaccante utilizzò il tailgating per accedere fisicamente a un edificio RSA. Questo contribuì al furto di dati crittografici sensibili.
- **Come mitigare:**  
  - Installare tornelli o porte con badge magnetici.  
  - Educare il personale a non lasciare entrare nessuno senza identificazione.

---


# <h1 align="center">🛡️ Esercizio 2: Strategie di Difesa</h1>

### 🎯 Obiettivo
Identificare e implementare strategie pratiche ed efficaci per mitigare i rischi derivanti dagli attacchi di Social Engineering, combinando misure tecnologiche avanzate e buone pratiche comportamentali.

### 💡 Prompt utilizzato
```text
ChatGPT, potresti elencare le strategie di difesa più efficaci contro gli attacchi di Social Engineering? Includi consigli tecnici e comportamentali, esempi di policy aziendali utili e strumenti tecnologici che possono essere implementati.
```

## 📊 Risultati

### 🛡️ Come Mitigare Questi Attacchi

1. **📘 Formazione e sensibilizzazione:**  
   - Educare regolarmente il personale sulle tecniche di Social Engineering e sui segnali di allarme.

2. **🔐 Autenticazione e verifica:**  
   - Implementare l'autenticazione a due fattori e verificare sempre l'identità di chiunque richieda informazioni o accesso.

3. **📑 Policy aziendali:**  
   - Creare e far rispettare policy chiare su email, dispositivi USB e accesso fisico.

4. **🖥️ Monitoraggio e tecnologia:**  
   - Utilizzare software avanzati per rilevare anomalie e tentativi di phishing.  
   - Monitorare accessi fisici e digitali.
---


#### **1. Strategie Comportamentali**
Le strategie comportamentali sono fondamentali per creare una cultura aziendale basata sulla consapevolezza della sicurezza. Alcuni approcci chiave includono:

- **📚 Formazione continua**:  
  Organizzare corsi periodici per il personale, focalizzati sul riconoscimento di segnali di allarme come email sospette, richieste urgenti non verificate o comportamenti insoliti.  
  > *Esempio pratico*: Workshop mensili con simulazioni di attacchi di phishing per identificare eventuali lacune nella prontezza dei dipendenti.

- **🔍 Fiducia verificabile**:  
  Promuovere una politica in cui ogni richiesta di informazioni sensibili venga verificata tramite canali separati e ufficiali, evitando di fidarsi ciecamente di email o telefonate.  
  > *Best practice*: Implementare checklist per verificare ogni richiesta fuori dall'ordinario.

- **🎭 Simulazioni realistiche**:  
  Eseguire test interni che simulino scenari di Social Engineering come phishing, pretexting o baiting, valutando le reazioni del personale.  
  > *Risultato atteso*: Miglioramento del tempo di risposta e aumento della sensibilità alle minacce.

---

#### **2. Strategie Tecniche**
L'integrazione di soluzioni tecnologiche all'avanguardia è essenziale per rafforzare la sicurezza contro attacchi di Social Engineering:

- **🤖 Sistemi di rilevamento basati su AI**:  
  Utilizzare piattaforme di intelligenza artificiale per monitorare e analizzare attività sospette in tempo reale.  
  > *Esempio*: Implementazione di sistemi che bloccano email di phishing grazie all'analisi semantica.

- **🔑 Autenticazione biometrica**:  
  Sostituire o affiancare le password con metodi biometrici come impronte digitali o riconoscimento facciale per ridurre i rischi di furto di credenziali.  
  > *Pro*: Aumenta significativamente la sicurezza senza complicare l'accesso per l'utente.

- **🛡️ Crittografia end-to-end**:  
  Garantire che tutte le comunicazioni interne siano criptate per impedire che informazioni sensibili vengano intercettate.  
  > *Esempio*: Utilizzo di strumenti di messaggistica aziendale sicura come Signal o Microsoft Teams.

---

#### **3. Policy Aziendali Esemplari**
Le politiche aziendali ben strutturate sono la base per standardizzare comportamenti sicuri e limitare il rischio:

- **📝 Protocolli di accesso remoto**:  
  Definire regole rigide per il lavoro a distanza, richiedendo autenticazione a più fattori (MFA) e connessioni VPN sicure.  
  > *Esempio*: Obbligo di utilizzo di dispositivi aziendali con configurazioni preimpostate per il telelavoro.

- **📩 Gestione delle email sospette**:  
  Creare un flusso chiaro per segnalare email sospette, con un team dedicato alla revisione tempestiva e alla sensibilizzazione dei dipendenti.  
  > *Strumenti utili*: Plugin di segnalazione diretta nelle caselle email aziendali.

- **🔒 Controllo degli accessi ai dati**:  
  Limitare l'accesso alle informazioni sensibili solo a personale strettamente autorizzato, con audit regolari per verificare conformità.  
  > *Esempio pratico*: Utilizzo di software di gestione delle identità (IAM) per tracciare e limitare le autorizzazioni.


Queste strategie combinano approcci tecnici e comportamentali per mitigare in modo efficace i rischi derivanti dagli attacchi di Social Engineering, costruendo un ambiente aziendale resiliente alle minacce.

---

# <h1 align="center">🛠️ Esercizio Bonus: Esplorazione dei CVE</h1>

## 🎯 Obiettivo
Esplorare le vulnerabilità note relative a software o sistemi operativi specifici.

## 💡 Prompt utilizzato
```text
ChatGPT, potresti fornire una lista di CVE relative a IE di Windows 7? Per ogni CVE, includi una breve descrizione della vulnerabilità, il livello di criticità (es. CVSS score) e i metodi di mitigazione consigliati.
```

## 📊 Risultati
1. **Software analizzato**: Internet Explorer (preinstallato su Windows 7)

2. **Esempi di CVE**:

   - **🛑 CVE-2017-8750**  
     - **Descrizione**: Vulnerabilità di corruzione della memoria che consente l'esecuzione di codice arbitrario nel contesto dell'utente corrente.  
     - **CVSS Score**: 7.6 (Alto)  
     - **Mitigazione**: Applicare le patch di sicurezza fornite da Microsoft e limitare i privilegi dell'utente per ridurre l'impatto di potenziali exploit.  

   - **⚠️ CVE-2017-8749**  
     - **Descrizione**: Problema di corruzione della memoria che permette l'esecuzione di codice arbitrario nel contesto dell'utente corrente.  
     - **CVSS Score**: 7.6 (Alto)  
     - **Mitigazione**: Installare gli aggiornamenti di sicurezza rilasciati da Microsoft e considerare l'utilizzo di browser alternativi più sicuri.  

   - **🌐 CVE-2017-8618**  
     - **Descrizione**: Vulnerabilità nel motore di scripting che potrebbe consentire l'esecuzione di codice arbitrario se un utente visita una pagina web appositamente predisposta.  
     - **CVSS Score**: 7.6 (Alto)  
     - **Mitigazione**: Aggiornare il browser con le ultime patch di sicurezza e disabilitare script non necessari.  

   - **🔍 CVE-2017-8529**  
     - **Descrizione**: Vulnerabilità che consente a un attaccante di rilevare file specifici sul computer dell'utente attraverso una gestione impropria degli oggetti in memoria.  
     - **CVSS Score**: 4.3 (Medio)  
     - **Mitigazione**: Applicare gli aggiornamenti di sicurezza e utilizzare strumenti di sicurezza per monitorare attività sospette.  

   - **🔒 CVE-2017-11790**  
     - **Descrizione**: Vulnerabilità che potrebbe consentire a un attaccante di ottenere informazioni per compromettere ulteriormente il sistema dell'utente.  
     - **CVSS Score**: 4.0 (Medio)  
     - **Mitigazione**: Installare le patch di sicurezza e limitare l'esecuzione di script non attendibili.  

---

# <h1 align="center">📝 Conclusioni</h1>

Il lavoro documentato in questo repository rappresenta una base solida per comprendere le tecniche di attacco e difesa nella sicurezza informatica. Ogni esercizio è stato completato con un focus particolare sulla qualità e l'efficacia dei prompt utilizzati.
L'utilizzo di versioni obsolete di browser, come Internet Explorer su Windows 7, comporta un rischio significativo di esposizione a vulnerabilità critiche. Si consiglia vivamente di aggiornare a sistemi operativi e browser più recenti per garantire una maggiore sicurezza.  
Ogni vulnerabilità documentata in questo esercizio sottolinea l'importanza di mantenere aggiornati software e sistemi operativi per prevenire exploit dannosi.

---

