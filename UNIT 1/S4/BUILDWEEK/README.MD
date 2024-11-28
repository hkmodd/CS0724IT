# S4 Build Week 1: REPORT OPERATIVO – CYBERCERBERUS

**Periodo:** 25/11/2024 - 29/11/2024  
**Team:** **CyberCerberus**  

## **Introduzione**
Benvenuti al report finale della **Build Week** del team **CyberCerberus**. Durante questa settimana, abbiamo affrontato la sfida di progettare un’infrastruttura IT scalabile, sicura e funzionale per l’azienda **Theta**, combinando simulazioni di rete avanzate, sviluppo software e analisi di sicurezza.  

**Composizione del team:**  
- **Federica Cardinali** – *Team Leader*  
- **Rinat Rustamov**  
- **Sebastiano Gelmetti**  
- **Luca Nietrzeba**  
- **Manuel Izzo**  
- **Francesco Rossi**  
- **Alessandro Ragnino**  
- **Andrea Calcagno**  
- **Antonio Podda**  

### **Obiettivo principale del progetto**
Progettare un’infrastruttura IT in grado di supportare:  
- **6 piani di uffici** con un totale di 120 dispositivi.  
- **Un Web server dedicato**.  
- **Un NAS per la condivisione dati**.  
- **Un Firewall perimetrale** e **3 sistemi IDS/IPS** per la prevenzione delle intrusioni.  
- Analisi e mitigazione delle vulnerabilità rilevate nella rete e nei sistemi.  

La nostra metodologia ha incluso la suddivisione in due gruppi operativi per garantire efficienza:  
- **Gruppo 1:** Sviluppo di un software in Python per il port scanning, le analisi HTTP e la generazione di report.  
- **Gruppo 2:** Simulazione della rete con Cisco Packet Tracer, ricerca hardware e stesura del contratto per Theta.

---

## **Cronologia delle Attività**

### **Giorno 1 – Lunedì 25/11/2024**
**Attività svolte:**  
- **Gruppo 1:**  
  - Analisi dei requisiti del progetto e raccolta della documentazione sui moduli Python utili.  
  - Definizione della struttura iniziale del programma.  
- **Gruppo 2:**  
  - Configurazione preliminare della rete in Cisco Packet Tracer.  
  - Raccolta dati sull’hardware per una futura implementazione reale.  

**Obiettivi raggiunti:**  
- Suddivisione chiara dei ruoli.  
- Avvio delle attività operative.  

---

### **Giorno 2 – Martedì 26/11/2024**
**Attività svolte:**  
- **Gruppo 1:**  
  - Implementazione iniziale del codice Python per il port scanning e analisi HTTP.  
  - Revisione collettiva della struttura del programma.  
- **Gruppo 2:**  
  - Progresso nella configurazione della rete simulata.  
  - Ricerca di switch, router, NAS e IDS/IPS adatti ai requisiti di Theta.  

**Obiettivi raggiunti:**  
- Creazione della base del software e identificazione dei moduli Python necessari.  
- Configurazione iniziale della rete e lista preliminare dei componenti hardware.  

---

### **Giorno 3 – Mercoledì 27/11/2024**
**Attività svolte:**  
- **Gruppo 1:**  
  - Completamento del programma Python “All-In-One”, integrando il port scanner e il sistema di analisi HTTP.  
  - Test pre e post-configurazione Firewall per analizzare l’impatto delle regole.  
- **Gruppo 2:**  
  - Finalizzazione della lista hardware con modelli, costi e specifiche dettagliate.  
  - Stesura del contratto e del preventivo.  

**Obiettivi raggiunti:**  
- Programma Python completamente funzionante, testato e documentato.  
- Preventivo e lista hardware pronti per l'approvazione da parte di Theta.  

---

### **Giorno 4 – Giovedì 28/11/2024**
**Attività svolte:**  
- **Revisione e perfezionamento:**  
  - Ottimizzazione della documentazione tecnica e completamento dei test finali.  
- **Analisi avanzata:**  
  - Identificazione di pattern malevoli in file JavaScript, inclusi elementi di steganografia.  
  - Implementazione di regole Firewall selettive con Squid Proxy e SquidGuard per bloccare accessi specifici senza interrompere servizi critici.  

**Obiettivi raggiunti:**  
- Documentazione finale pronta per la consegna.  
- Analisi delle vulnerabilità e proposte di mitigazione dettagliate.  

---

## **Risultati Ottenuti**
### **Software sviluppato dal Gruppo 1:**
1. **Port Scanner:**  
   - Analisi dettagliata delle porte aperte, identificando criticità su servizi come Telnet e FTP.  
   - Generazione di report in formato CSV per un’analisi completa.  
2. **Analisi HTTP:**  
   - Verifica del comportamento delle pagine web tramite richieste GET, POST, PUT e DELETE.  
   - Identificazione di vulnerabilità, come risposte anomale sulla pagina /phpMyAdmin.  
3. **Sistema di logging e report:**  
   - Registrazione dettagliata delle richieste e creazione di report personalizzati per il cliente.  

### **Infrastruttura simulata dal Gruppo 2:**
1. **Simulazione di rete su Cisco Packet Tracer:**  
   - Configurazione di una rete distribuita su 6 piani con 120 dispositivi.  
   - Test di resilienza e verifica dell’interazione tra router, switch, NAS e IDS/IPS.  
2. **Firewall avanzato:**  
   - Blocco selettivo degli URL tramite Squid Proxy e SquidGuard, garantendo l’operatività dei servizi essenziali.  
3. **Ricerca hardware:**  
   - Lista dettagliata di router, switch e IDS/IPS per l'implementazione reale, con costi e specifiche tecniche.

---

## **Conclusioni**
Il progetto **CyberCerberus** ha dimostrato che la collaborazione e la sinergia tra i membri del team sono fondamentali per affrontare sfide complesse. Abbiamo consegnato soluzioni tecniche robuste, tra cui:  
- **Software Python** per il monitoraggio e la sicurezza della rete.  
- **Simulazione di rete completa**, pronta per essere implementata.  
- **Preventivo realistico** con scelte tecnologiche sostenibili.  

### **Prospettive future**
Il progetto rappresenta una base solida per l’implementazione reale. Il prossimo passo sarà supportare il cliente nella configurazione hardware e nella manutenzione dell’infrastruttura, garantendo che resti sicura, scalabile ed efficiente nel tempo.

Grazie per l’attenzione.  

**Sebastiano Gelmetti**  
*Software Engineer, Exploit tester, CyberCerberus*
