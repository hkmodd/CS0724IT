# 📝 Consegna S9/L4
# **Gestione e Analisi dei Log di Sicurezza** 🛡️🖥️

In questa pratica, ci concentriamo sulla configurazione, gestione e analisi dei file di log di sicurezza di Windows utilizzando il **Visualizzatore Eventi**. L'obiettivo è identificare eventi critici come tentativi di accesso, modifiche ai privilegi e attività sospette.

---

## 📝 **Obiettivo**
Comprendere come:
1. Configurare i log di sicurezza per monitorare eventi specifici.
2. Generare eventi di test e analizzarli.
3. Esportare i log per una revisione e documentazione collaborativa.

---

## ⚙️ **Passaggi per completare la pratica**

### **1️⃣ Abilitare la registrazione degli eventi di sicurezza**
1. Accedi come amministratore al sistema Windows.
2. Apri il **Visualizzatore Eventi**:
   - Premi `Win + R`, digita `eventvwr` e premi Invio.
3. Espandi il nodo **Registri di Windows** > **Sicurezza**.
4. Configura i criteri di registrazione:
   - Apri **Criteri di sicurezza locali**:
     - Premi `Win + R`, digita `secpol.msc` e premi Invio.
   - Vai su **Criteri locali** > **Criteri di controllo**.
   - Attiva i seguenti criteri (imposta "Successo e Insuccesso"):
     - **Accesso agli account**.
     - **Modifiche ai privilegi degli account**.
     - **Accesso al sistema**.
     - **Eventi del log di sicurezza**.

---

### **2️⃣ Generare eventi di sicurezza**
Esegui attività per generare eventi specifici:
- Esegui un **accesso riuscito** e uno **fallito**.
- Modifica i privilegi di un utente (es. aggiungilo a un gruppo).
- Accedi a una risorsa condivisa (es. una cartella di rete).

---

### **3️⃣ Analizzare i log**
1. Torna al **Visualizzatore Eventi** e apri il registro **Sicurezza**.
2. Cerca eventi specifici:
   - **ID Evento** di riferimento:
     - **4624**: Accesso riuscito.
     - **4625**: Tentativo di accesso fallito.
     - **4670**: Modifica a un oggetto.
     - **4697**: Installazione di un servizio.
   - Usa i filtri:
     - Clicca su **Filtra registro corrente** nel pannello di destra.
     - Inserisci gli ID evento di interesse.

---

### **4️⃣ Esportare i log**
1. Esporta i log per documentazione:
   - Clicca su **Salva registro con nome**.
   - Salva in formato `.evtx`.
2. Condividi il file con il team per un'analisi collaborativa.

---

## 📚 **Strumenti Utilizzati**
- **Visualizzatore Eventi di Windows**: Per analizzare e gestire i log.
- **Criteri di sicurezza locali**: Per configurare le policy di registrazione.

---

## 📊 **Risultati Attesi**
- Identificazione di eventi chiave, come accessi non autorizzati e modifiche ai privilegi.
- Log esportati per un'analisi successiva.

---

## 🛠️ **Suggerimenti e Best Practice**
- **Automazione**:
  - Configura avvisi automatici per eventi specifici usando **Task Scheduler**.
- **Analisi avanzata**:
  - Integra i log con strumenti come **Splunk** o **ELK Stack** per una revisione su larga scala.

---
