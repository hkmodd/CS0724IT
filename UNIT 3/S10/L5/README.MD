# Progetto S10/L5: Creazione e Gestione di Gruppi e Permessi su Windows Server

## Introduzione
In questo progetto, abbiamo configurato un ambiente **Windows Server 2022** per gestire utenti, gruppi e risorse condivise. L'obiettivo è stato quello di:

1. Creare due Organizational Units (OU) con relativi utenti e gruppi.
2. Configurare i permessi per le cartelle condivise:
   - **Pubblica**: accessibile a tutti ma con limitazioni per gli utenti standard.
   - **ADMIN**: accessibile solo agli amministratori.
3. Verificare che i permessi funzionino correttamente.

Questo README funge da walkthrough completo del progetto, con tutti i passaggi eseguiti. 📝✨

---

## Struttura del Progetto

### 1. Creazione delle OU, Utenti e Gruppi

#### Passaggio 1: Accesso a Active Directory Users and Computers
- Dal **Server Manager**, clicca su **Tools** > **Active Directory Users and Computers** (vedi [screenshot 1.png](./1.png)).

#### Passaggio 2: Creazione di Organizational Units (OU)
- Nella struttura **Epicode.local**, ho creato due OU:
  - **Amministrazione** (vedi [screenshot 2.png](./2.png))
  - **Utenti Standard** (vedi [screenshot 3.png](./3.png))

#### Passaggio 3: Creazione degli Utenti
- All'interno di ogni OU, ho aggiunto utenti pertinenti:
  - **Amministrazione**:
    - *Sergio Vanni*
    - *Vannis Ergio*
  - **Utenti Standard**:
    - *Utente1*
    - *Utente2*

Vedi [screenshot 4.png](./4.png) e [screenshot 4.5.png](./4.5.png) per i dettagli della creazione.

#### Passaggio 4: Creazione dei Gruppi
- Ho creato i seguenti gruppi:
  - **IT_Admins** (in *Amministrazione*).
  - **UtentiStandard** (in *Utenti Standard*).
- Vedi [screenshot 5.png](./5.png) per la procedura.

---

### 2. Configurazione delle Cartelle e dei Permessi

#### Cartella **ADMIN**
- **Path**: `C:\ADMIN`
- **Permessi**:
  - Accesso completo (Full Control) per **IT_Admins**.
  - Nessun accesso per **UtentiStandard**.
- Ho verificato che utenti come *Sergio Vanni* possano accedere e modificare i file (vedi [screenshot 6.png](./6.png)).
- Gli utenti standard ricevono un errore di accesso negato (vedi [screenshot 7.png](./7.png)).

#### Cartella **Pubblica**
- **Path**: `C:\Pubblica`
- **Permessi**:
  - Accessibile da tutti i gruppi.
  - Modifica vietata per **UtentiStandard** (permessi in sola lettura).
- Ho verificato che gli utenti standard possano aprire ma non modificare i file, come mostrato in [screenshot 8.png](./8.png).

---

### 3. Condivisione delle Cartelle in Rete

#### Passaggio 1: Condivisione della Cartella **ADMIN**
- Ho condiviso la cartella **ADMIN** con il gruppo **IT_Admins** attraverso le **proprietà di condivisione avanzata** (vedi [screenshot 5.5.png](./5.5.png)).
- Ho verificato che solo gli amministratori possano accedere in rete.

#### Passaggio 2: Condivisione della Cartella **Pubblica**
- Ho condiviso la cartella **Pubblica**, garantendo l'accesso completo solo agli amministratori e limitando le modifiche per gli utenti standard.

---

### 4. Verifica dei Permessi

#### Test Utenti **IT_Admins**
- Accesso completo a **ADMIN** e **Pubblica**.
- Possibilità di modificare file e aggiungere nuovi contenuti.

#### Test Utenti **UtentiStandard**
- Accesso limitato a **Pubblica** (solo lettura).
- Impossibilità di accedere a **ADMIN** (errore di rete confermato).

---

## Conclusione

Il progetto si è concluso con successo. 💪🎉

Abbiamo creato un ambiente sicuro e ben organizzato su Windows Server 2022, rispettando le best practice di gestione utenti e risorse. Questo walkthrough è una guida utile per chiunque voglia replicare un setup simile.

Se ci sono domande o dubbi, non esitare a contattarmi! 😉
