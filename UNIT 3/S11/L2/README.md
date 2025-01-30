# 📝 Consegna S11/L2

# 🔥 Cisco CyberOps - 1

1. 🖥 **Installazione e configurazione di macchine virtuali per ambienti di test e analisi di sicurezza.**
2. 🔍 **Esplorazione di processi, thread, handle e il registro di Windows utilizzando strumenti avanzati.**

---

## 📌 **Indice**
1. [🔧 Requisiti](#🔧-requisiti)
2. [🏗 Laboratorio 1 - Installazione delle macchine virtuali](#🏗-laboratorio-1---installazione-delle-macchine-virtuali)
3. [🖥 Laboratorio 2 - Analisi di processi e registro di Windows](#🖥-laboratorio-2---analisi-di-processi-e-registro-di-windows)
   - [📥 Installazione degli strumenti](#📥-installazione-degli-strumenti)
   - [🔍 Analisi dei processi](#🔍-analisi-dei-processi)
   - [🗂 Esplorazione e modifica del registro di sistema](#🗂-esplorazione-e-modifica-del-registro-di-sistema)
4. [📚 Risorse utili](#📚-risorse-utili)

---

## 🔧 **Requisiti**
🔹 **Sistema operativo:** Windows 10/11 o una distribuzione Linux compatibile con VirtualBox/VMware.  
🔹 **Strumenti necessari:**

   - [Oracle VirtualBox](https://www.virtualbox.org/)
   - [Windows SysInternals Suite](https://docs.microsoft.com/en-us/sysinternals/downloads/)
   - Accesso ai file delle VM preconfigurate (disponibili nei link forniti)

---

## 🏗 **Laboratorio 1 - Installazione delle macchine virtuali**
### 📥 **Download degli strumenti**
### 🔄 **Importazione della VM**
1. Apri **VirtualBox** e seleziona **File > Importa Appliance**.
2. Seleziona il file `.ova` della VM scaricata.
3. Clicca su **Avanti** e poi su **Importa**.

### ⚙️ **Configurazione delle VM**
1. **Assegna almeno 4GB di RAM e 2 core CPU**.
2. **Abilita la rete bridge**.

---

## 🖥 **Laboratorio 2 - Analisi di processi e registro di Windows**
### 📥 **Installazione degli strumenti**
1. Scaricare **SysInternals Suite** da [qui](https://docs.microsoft.com/en-us/sysinternals/downloads/).
2. Estrarre il file `.zip` e aprire la cartella estratta.
3. Eseguire `procexp.exe` come amministratore.

### 🔍 **Analisi dei processi**
1. Avviare **Process Explorer** (`procexp.exe`).
2. Osservare la colonna **PID**.
3. Identificare processi critici come `explorer.exe`, `svchost.exe`, `winlogon.exe`.

---

### 🗂 **Esplorazione e modifica del registro di sistema**
🔹 **Strumento utilizzato:** **Regedit** (`regedit.exe`)  
🔹 **Scopo:** Simulazione della modifica di chiavi di registro per ottimizzare il sistema.

#### 🔎 **Navigazione nel registro**
1. Apro il **Registro di sistema di Windows** (`regedit.exe`).
2. Mi sposto tra le chiavi più critiche:
   - `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services`
   - `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`

#### 🛠 **Simulazione della modifica delle chiavi di registro**
1. **Disabilitazione dell'avvio automatico di un'applicazione**  
   🔹 **Percorso:** `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`  
   🔹 **Azione:** Rimosso `OneDrive.exe`.  
   🎯 **Motivazione:** Migliora le prestazioni di avvio.

2. **Ottimizzazione del tempo di spegnimento**  
   🔹 **Percorso:** `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control`  
   🔹 **Chiave:** `WaitToKillServiceTimeout = 2000`  
   🎯 **Motivazione:** Riduce il tempo di spegnimento.

3. **Abilitazione della visualizzazione delle estensioni dei file**  
   🔹 **Percorso:** `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced`  
   🔹 **Chiave:** `HideFileExt = 0`  
   🎯 **Motivazione:** Evita attacchi di phishing.

4. **Abilitazione dell'avvio veloce di Windows**  
   🔹 **Percorso:** `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power`  
   🔹 **Chiave:** `HiberbootEnabled = 1`  
   🎯 **Motivazione:** Riduce il tempo di riavvio.

---

## 📚 **Risorse utili**
🔗 **VirtualBox Guide:** [https://www.virtualbox.org/manual/](https://www.virtualbox.org/manual/)  
🔗 **SysInternals Documentation:** [https://docs.microsoft.com/en-us/sysinternals/](https://docs.microsoft.com/en-us/sysinternals/)  
🔗 **Registro di Windows - Guida Microsoft:** [https://docs.microsoft.com/en-us/windows/](https://docs.microsoft.com/en-us/windows/)  

---

🎯 **Obiettivi completati:**
✅ Installazione e configurazione di macchine virtuali  
✅ Esplorazione avanzata di processi e thread  
✅ Simulazione di modifiche strategiche al registro di Windows  
