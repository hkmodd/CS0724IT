# CyberCerberus - Build Week 3

## Introduzione
Benvenuti nel repository della Build Week 3 del team **CyberCerberus**. In questo documento descriviamo il lavoro svolto dal team, le metodologie adottate e le conclusioni tratte dalle analisi effettuate.

---

## Attività Svolte

### 1. **Analisi Malware**
- Il team ha scaricato e analizzato il malware **AdwereCleaner.exe** reperito al seguente link:
  [GitHub - The MALWARE Repo](https://github.com/Da2dalus/The-MALWARE-Repo/blob/master/rogues/AdwereCleaner.exe)
- L'analisi ha incluso:
  - Comportamento del file in ambienti isolati (sandboxing)
  - Reverse engineering del codice binario
  - Rilevamento di IOC (Indicators of Compromise)
  - Tecniche di evasione dai sistemi di sicurezza
- **Output**: Un report dettagliato con mitigazioni proposte e classificazione della minaccia.

### 2. **Analisi Anyrun**
- Abbiamo studiato i seguenti report di Any.run:
  - [Threat Analysis 1](https://app.any.run/tasks/371957e1-d960-4b8a-8c68-241ff918517d/)
  - [Threat Analysis 2](https://app.any.run/tasks/f1f20828-2222-46fb-a886-09f77581e67b/)
- Ogni analisi è stata convertita in un report in italiano per un pubblico non tecnico, descrivendo la minaccia e suggerendo le azioni di remediation più appropriate (blacklist, quarantena, eliminazione, ecc.).

### 3. **Navigazione del Filesystem Linux e Gestione dei Permessi**
- Abbiamo completato il laboratorio pratico disponibile su:
  - [Lab Navigating Linux Filesystem](https://itexamanswers.net/4-5-4-lab-navigating-the-linux-filesystem-and-permission-settings-answers.html)
- Abbiamo approfondito:
  - Comandi essenziali (`ls`, `cd`, `chmod`, `chown`, `sudo`, etc.)
  - Struttura dei permessi e loro gestione avanzata

### 4. **Estrazione di un Eseguibile da un File PCAP**
- Analizzato traffico di rete per estrarre un file eseguibile da un dump PCAP:
  - [Lab PCAP Extraction](https://itexamanswers.net/27-2-10-lab-extract-an-executable-from-a-pcap-answers.html)
- Tecniche utilizzate:
  - Wireshark per individuare il payload
  - Foremost e binwalk per il carving dei file

### 5. **Bonus: Un altro link Anyrun**
- Analisi aggiuntiva di un altro caso su Any.run:
  - [Threat Analysis Bonus](https://app.any.run/tasks/9a158718-43fe-45ce-85b3-66203dbc2281/)

### 6. **Bonus: Interpretazione HTTP e DNS Data per Isolare Threat Actor**
- Indagine su SQL Injection e DNS Exfiltration tramite Security Onion:
  - [Lab SQL Injection e DNS](https://itexamanswers.net/27-2-12-lab-interpret-http-and-dns-data-to-isolate-threat-actor-answers.html)

### 7. **Bonus: Isolamento di un Host Compromesso con 5-Tuple**
- Investigazione su un exploit con Security Onion:
  - [Lab 5-Tuple Investigation](https://itexamanswers.net/27-2-14-lab-isolate-compromised-host-using-5-tuple-answers.html)

### 8. **Extra: Analisi del Malware Mydoom**
- Analizzato uno dei worm più distruttivi della storia informatica.
  - Link al codice: [Win32.Mydoom.a](https://github.com/vxunderground/MalwareSourceCode/raw/main/Win32/Win32.Mydoom.a.7z)
- Obiettivi:
  - Analisi del codice sorgente per identificare tecniche di propagazione ed evasione
  - Confronto con varianti più recenti
  - Identificazione di pattern per la detection

### 9. **Extra: Sfruttamento di una Vulnerabilità di Buffer Overflow**
- Obiettivo: Dimostrare l'exploit su una vulnerabilità buffer overflow.
- Passaggi eseguiti:
  1. Creazione di un ambiente di test basato su:
     - [Vulnerable App](https://github.com/akir4d/Buffer-Overflow-Vulnerable-app)
  2. Analisi della vulnerabilità con debugger
  3. Sviluppo di un exploit custom in Python
  4. Test e verifica della compromissione del sistema
  5. Redazione di un report dettagliato con mitigazioni proposte

---

## Conclusioni
Il team **CyberCerberus** ha completato con successo tutte le attività assegnate, producendo report dettagliati e implementando metodologie avanzate di analisi e mitigazione delle minacce. Ogni attività è stata documentata in modo professionale, con l'obiettivo di dimostrare competenze avanzate in **Cyber Security & Ethical Hacking**.

---

## Autori
Team **CyberCerberus** - Epicode Cyber Security Program 2025