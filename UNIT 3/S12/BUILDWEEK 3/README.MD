# 🌐 Build Week 3: **REPORT OPERATIVO – CYBERCERBERUS**

**🗓 Periodo:** 03/02/2025 - 07/02/2025  
**👥 Team:** **CyberCerberus**

## 🗂️ Indice

- ### [🚀 Inizio](#-introduzione)

- ### 📝 Tracce
  - [📌 1: Malware Analysis](#-traccia-1-malware-analysis)
  - [📌 2: Anyrun](#-traccia-2-anyrun)
  - [📌 3: Navigating Linux Filesystem](#-traccia-3-navigating-linux-filesystem)
  - [📌 4: Extract an Exec from a PCAP](#-traccia-4-extract-an-exec-from-a-pcap)
  - [📌 5: Bonus 1 - Un altro link Anyrun](#-bonus-1-un-altro-link-anyrun)
  - [📌 6: Bonus 2 - Interpret HTTP and DNS Data to Isolate Threat Actor](#-bonus-2-interpret-http-and-dns-data-to-isolate-threat-actor)
  - [📌 7: Bonus 3 - Isolate Compromised Host Using 5-Tuple](#-bonus-3-isolate-compromised-host-using-5-tuple)
  - [📌 8: Extra 1 - Malware Mydoom](#-extra-1-malware-mydoom)
  - [📌 9: Extra 2 - Sviluppo Exploit - Buffer Overflow](#-extra-2-sviluppo-exploit-buffer-overflow)

- ### [🚀 Conclusioni](#-conclusioni-e-prospettive-future)

---

# **🚀 Introduzione**

Durante questa **Build Week**, il team **CyberCerberus** ha affrontato un programma avanzato di Cybersecurity, completando diverse attività relative all’analisi malware, alla forensics analysis e alla simulazione di attacchi e difese su ambienti controllati.

L'obiettivo principale era mettere in pratica competenze avanzate nell’identificazione e mitigazione delle minacce informatiche attraverso:
- Analisi di malware tramite static e dynamic analysis 🦠
- Studio delle minacce con Anyrun e strumenti avanzati 🔍
- Investigazioni forensi su filesystem Linux 📂
- Packet analysis per estrazione di eseguibili da PCAP 📡
- Exploit di vulnerabilità critiche come buffer overflow 🔥

Il team ha lavorato in maniera sinergica, documentando ogni attività con un approccio metodologico rigoroso e con l’adozione delle best practices del settore.

---

## **🔍 TRACCIA 1: Malware Analysis**

- **Obiettivo:** Analizzare il malware *AdwereCleaner.exe* per comprenderne comportamento ed evasione.
- **Strumenti Utilizzati:**
  - Any.run, IDA Pro, Wireshark
  - Static/Dynamic Analysis
- **Output:** Report dettagliato con IOC e mitigazioni.

---

## **🔍 TRACCIA 2: Anyrun**

- **Obiettivo:** Analizzare minacce tramite Any.run e proporre azioni di remediation.
- **Link Analizzati:**
  - [Threat Analysis 1](https://app.any.run/tasks/371957e1-d960-4b8a-8c68-241ff918517d/)
  - [Threat Analysis 2](https://app.any.run/tasks/f1f20828-2222-46fb-a886-09f77581e67b/)
- **Output:** Report dettagliati e proposte di mitigazione.

---

## **📂 TRACCIA 3: Navigating Linux Filesystem**

- **Obiettivo:** Comprendere la gestione dei filesystem Linux e i permessi utente.
- **Strumenti Utilizzati:**
  - Terminale Linux, comandi `ls`, `chmod`, `chown`
- **Output:** Report sulle configurazioni di sicurezza dei permessi.

---

## **📡 TRACCIA 4: Extract an Exec from a PCAP**

- **Obiettivo:** Estrarre un file eseguibile da un dump PCAP.
- **Strumenti Utilizzati:**
  - Wireshark, Foremost, Tshark
- **Output:** File estratto e analizzato con report dettagliato.

---

## **📌 BONUS 1: Un altro link Anyrun**

- **Obiettivo:** Approfondire una nuova minaccia tramite Any.run.
- **Link Analizzato:** [Threat Analysis Bonus](https://app.any.run/tasks/9a158718-43fe-45ce-85b3-66203dbc2281/)

---

## **🔍 BONUS 2: Interpret HTTP and DNS Data to Isolate Threat Actor**

- **Obiettivo:** Analisi di SQL Injection e DNS Exfiltration con Security Onion.
- **Strumenti Utilizzati:**
  - Suricata, Zeek, Elastic Stack

---

## **🔍 BONUS 3: Isolate Compromised Host Using 5-Tuple**

- **Obiettivo:** Investigare un exploit con Security Onion.
- **Strumenti Utilizzati:**
  - Security Onion, Kibana, Suricata

---

## **🦠 EXTRA 1: Malware Mydoom**

- **Obiettivo:** Analizzare il worm Mydoom e individuare pattern di detection.
- **Strumenti Utilizzati:**
  - Reverse Engineering, IDA Pro

---

## **🔥 EXTRA 2: Sviluppo Exploit - Buffer Overflow**

- **Obiettivo:** Dimostrare uno scenario di exploit tramite buffer overflow.
- **Passaggi:**
  1. Setup di un'applicazione vulnerabile
  2. Debug con GDB
  3. Creazione di un payload exploitativo
- **Output:** Report dettagliato con codice exploit e mitigazioni.

---

## Più nel dettaglio:

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

# **🚀 Conclusioni e Prospettive Future**

Il team **CyberCerberus** ha portato a termine tutte le tracce assegnate, dimostrando elevate competenze tecniche nell’analisi di vulnerabilità e nella gestione delle minacce informatiche. 

Le prossime attività saranno incentrate su:
- **Approfondimento delle tecniche di attacco avanzate** (ROP, Heap Overflow)
- **Utilizzo di nuove piattaforme di penetration testing** (Hack The Box, TryHackMe)
- **Sviluppo di strumenti custom per automatizzare l’analisi delle minacce**

Siamo pronti a nuove sfide! 🚀🔥

**Team CyberCerberus** - Epicode Cyber Security Program 2025

---
