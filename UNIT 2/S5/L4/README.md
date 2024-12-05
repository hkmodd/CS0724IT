
# Social Engineering & Cybersecurity Exercises

Questo repository contiene la documentazione e i risultati degli esercizi svolti relativi al Social Engineering, alle tecniche di difesa e all'esplorazione delle vulnerabilità CVE. Ogni attività è stata completata utilizzando prompt ben strutturati per garantire risposte dettagliate e mirate.

## Contenuti

- [Introduzione](#introduzione)
- [Esercizio 1: Social Engineering](#esercizio-1-social-engineering)
- [Esercizio 2: Strategie di Difesa](#esercizio-2-strategie-di-difesa)
- [Esercizio Bonus: Esplorazione dei CVE](#esercizio-bonus-esplorazione-dei-cve)
- [Come usare questo repository](#come-usare-questo-repository)

---

## Introduzione

L'obiettivo degli esercizi è stato quello di esplorare le tecniche di Social Engineering e le relative strategie di difesa, oltre a imparare a identificare e analizzare vulnerabilità utilizzando i CVE (Common Vulnerabilities and Exposures). Attraverso l'uso di prompt ottimizzati, sono state raccolte informazioni chiave per comprendere e affrontare questi scenari.

---


## Esercizio 1: Social Engineering

### Obiettivo
Esplorare le tecniche di Social Engineering e imparare come difendersi da attacchi di questo tipo.

### Prompt utilizzato
```text
ChatGPT, potresti fornire una definizione dettagliata di Social Engineering e analizzare le tecniche più comuni utilizzate dagli attaccanti? Fornisci almeno tre esempi di attacchi reali documentati, spiegando il contesto e l'impatto di ciascuno.
```

### Risultati

#### **Phishing**
**Descrizione:**  
Il phishing è un attacco in cui gli aggressori inviano comunicazioni (spesso email, messaggi SMS o attraverso social media) che sembrano provenire da una fonte legittima per indurre la vittima a fornire informazioni sensibili come credenziali di accesso, dati bancari o informazioni personali.

**Struttura dell'attacco:**
1. **Preparazione:**  
   - L'attaccante crea un'email/messaggio con un layout che imita un'azienda o un'organizzazione legittima, come una banca, un provider di servizi online o un ente governativo.
   - Inserisce link che reindirizzano a siti web fasulli, molto simili a quelli ufficiali.

2. **Esecuzione:**  
   - L'email/messaggio contiene un'esca, come un avviso urgente (es. "Il tuo account sarà sospeso se non confermi la tua identità").
   - La vittima clicca sul link e inserisce i propri dati personali sulla pagina fasulla.

3. **Conclusione:**  
   - L'attaccante utilizza le informazioni per accedere a sistemi o rubare denaro.

**Esempio pratico:**
- **Caso PayPal (2014):**  
  Un'email falsa, apparentemente inviata da PayPal, avvisava gli utenti di "attività sospette" sui loro account. I destinatari erano invitati a cliccare su un link e fornire le loro credenziali. Milioni di utenti caddero nella trappola, causando perdite finanziarie significative.
- **Come mitigare:**  
  - Verificare sempre il mittente dell'email.  
  - Non cliccare su link sospetti; digitare manualmente l'URL dell'organizzazione.  
  - Implementare un filtro antiphishing nei sistemi di posta elettronica.

---

#### **Baiting**
**Descrizione:**  
Il baiting sfrutta la curiosità delle vittime, inducendole a interagire con dispositivi o file compromessi.

**Struttura dell'attacco:**
1. **Preparazione:**  
   - L'attaccante lascia un dispositivo (es. una chiavetta USB infetta) in un luogo pubblico.
   - Il dispositivo ha un'etichetta intrigante, come "Confidenziale" o "Salari aziendali".

2. **Esecuzione:**  
   - La vittima raccoglie il dispositivo e lo collega al proprio computer per curiosità.
   - Il dispositivo installa malware che consente agli aggressori di accedere al sistema.

3. **Conclusione:**  
   - Gli attaccanti accedono ai dati aziendali o controllano il sistema.

**Esempio pratico:**
- **Caso di un'azienda americana (2016):**  
  Chiavette USB infette furono lasciate nel parcheggio dell'azienda. Diversi dipendenti le inserirono nei computer aziendali, installando involontariamente malware che rubava dati sensibili.
- **Come mitigare:**  
  - Vietare ai dipendenti di collegare dispositivi non autorizzati.  
  - Implementare software di controllo su porte USB.  

---

#### **Pretexting**
**Descrizione:**  
Nel pretexting, gli attaccanti creano un contesto credibile (o "pretesto") per ottenere informazioni sensibili dalla vittima.

**Struttura dell'attacco:**
1. **Preparazione:**  
   - L'attaccante raccoglie informazioni sulla vittima (es. nome, posizione lavorativa, relazioni personali).
   - Costruisce un pretesto, come fingere di essere un tecnico IT o un rappresentante bancario.

2. **Esecuzione:**  
   - Contatta la vittima via telefono, email o di persona.
   - Con un approccio amichevole e professionale, induce la vittima a rivelare informazioni sensibili.

3. **Conclusione:**  
   - Gli attaccanti utilizzano le informazioni per accedere a sistemi o compiere frodi.

**Esempio pratico:**
- **Caso di Verizon (2016):**  
  Un attaccante si finse un consulente IT e convinse un dipendente a fornire le credenziali di accesso aziendali. Questo portò a una violazione dei dati di milioni di clienti.
- **Come mitigare:**  
  - Educare i dipendenti a verificare sempre l'identità del richiedente.  
  - Implementare una policy aziendale che vieti di condividere credenziali via telefono o email.

---

#### **Tailgating**
**Descrizione:**  
Il tailgating si verifica quando un attaccante si intrufola in un'area riservata seguendo una persona autorizzata.

**Struttura dell'attacco:**
1. **Preparazione:**  
   - L'attaccante osserva l'ingresso di un edificio o di un'area protetta.
   - Identifica una vittima ignara, come un dipendente o un visitatore.

2. **Esecuzione:**  
   - Si avvicina alla vittima, fingendo di aver dimenticato il badge o di essere un collaboratore esterno.
   - Segue la vittima attraverso l'accesso, sfruttando la cortesia delle persone.

3. **Conclusione:**  
   - Una volta dentro, l'attaccante può rubare documenti, accedere a computer o compromettere l'infrastruttura.

**Esempio pratico:**
- **Caso RSA Security (2011):**  
  Un attaccante utilizzò il tailgating per accedere fisicamente a un edificio RSA. Questo contribuì al furto di dati crittografici sensibili.
- **Come mitigare:**  
  - Installare tornelli o porte con badge magnetici.  
  - Educare il personale a non lasciare entrare nessuno senza identificazione.

---

### Come Mitigare Questi Attacchi

1. **Formazione e sensibilizzazione:**  
   - Educare regolarmente il personale sulle tecniche di Social Engineering e sui segnali di allarme.

2. **Autenticazione e verifica:**  
   - Implementare l'autenticazione a due fattori e verificare sempre l'identità di chiunque richieda informazioni o accesso.

3. **Policy aziendali:**  
   - Creare e far rispettare policy chiare su email, dispositivi USB e accesso fisico.

4. **Monitoraggio e tecnologia:**  
   - Utilizzare software avanzati per rilevare anomalie e tentativi di phishing.  
   - Monitorare accessi fisici e digitali.
   - 
---

## Esercizio 2: Strategie di Difesa

### Obiettivo
Identificare strategie efficaci per difendersi dagli attacchi di Social Engineering.

### Prompt utilizzato
```text
ChatGPT, potresti elencare le strategie di difesa più efficaci contro gli attacchi di Social Engineering? Includi consigli tecnici e comportamentali, esempi di policy aziendali utili e strumenti tecnologici che possono essere implementati.
```

### Risultati
1. **Strategie comportamentali**:
   - Educazione e sensibilizzazione dei dipendenti.
   - Verifica delle identità prima di condividere informazioni sensibili.

2. **Strategie tecniche**:
   - Implementazione dell’autenticazione a due fattori (2FA).
   - Uso di software per il monitoraggio delle attività anomale.

3. **Esempio di policy aziendale**:
   - Creazione di un protocollo standardizzato per gestire richieste via email o telefono.

---

## Esercizio Bonus: Esplorazione dei CVE

### Obiettivo
Esplorare le vulnerabilità note relative a software o sistemi operativi specifici.

### Prompt utilizzato
```text
ChatGPT, potresti fornire una lista di CVE relative a [nome del software o sistema operativo]? Per ogni CVE, includi una breve descrizione della vulnerabilità, il livello di criticità (es. CVSS score) e i metodi di mitigazione consigliati.
```

### Risultati
1. **Software analizzato**: Apache HTTP Server
2. **Esempi di CVE**:
   - **CVE-2021-44228 (Log4Shell)**:
     - Descrizione: Vulnerabilità di esecuzione remota di codice.
     - CVSS Score: 10.0 (Critico).
     - Mitigazione: Aggiornare a una versione sicura di Log4j.
   - **CVE-2022-22719**:
     - Descrizione: Overflow del buffer in mod_sed.
     - CVSS Score: 7.5 (Alto).
     - Mitigazione: Aggiornare Apache alla versione più recente.

---

## Note Finali

Il lavoro documentato in questo repository rappresenta una base solida per comprendere le tecniche di attacco e difesa nella sicurezza informatica. Ogni esercizio è stato completato con un focus particolare sulla qualità e l'efficacia dei prompt utilizzati.

Se hai suggerimenti o vuoi contribuire, sentiti libero di creare una pull request o di aprire una issue.

---

## Autore

Sebastiano

---

