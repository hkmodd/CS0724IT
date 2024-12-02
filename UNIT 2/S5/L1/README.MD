# Consegna S5/L1: Information Gathering

## Target: `concadorohotel.it`

Questo esercizio ha l'obiettivo di simulare una fase di raccolta di informazioni pubbliche (OSINT) su un target specifico, utilizzando strumenti come **Google** e **Maltego**. Di seguito vengono descritti i passaggi effettuati, i risultati ottenuti e l'analisi delle informazioni raccolte.

---

## **1. Raccolta delle Informazioni con Google**

### 1.1. Pagine Indicizzate del Sito
Utilizzando la query `site:concadorohotel.it`, sono state identificate le seguenti pagine principali:
- **Home Page**: Presenta l'hotel e i suoi servizi principali.
- **Promozioni**: Dettagli sulle offerte attuali.
- **I nostri servizi**: Descrive i servizi disponibili.
- **Food & Drinks**: Informazioni sull'offerta gastronomica.
- **Garda e dintorni**: Suggerimenti per attività nella zona del Lago di Garda.
- **F.A.Q.**: Risponde alle domande frequenti degli ospiti.

---

### 1.2. Documenti Pubblici Disponibili
Utilizzando la query `filetype:pdf OR filetype:docx OR filetype:xlsx site:concadorohotel.it`, sono stati individuati:
- **Menù Bar**: PDF con bevande e snack disponibili al bar dell'hotel.
- **Menù Ristorante**: PDF con l'offerta culinaria del ristorante.

---

### 1.3. Indirizzi Email Associati
Con la query `"@concadorohotel.it"`, è stato identificato il seguente indirizzo email:
- **info@concadorohotel.it**: Email pubblica utilizzata per comunicazioni generali e prenotazioni.

---

### 1.4. Contatti
Utilizzando la query `"contatti" site:concadorohotel.it`, sono stati trovati:
- **Indirizzo**: Lungolago Europa 2, Garda (VR) - 37016  
- **Telefono**: +39 045 7255275  
- **Email**: info@concadorohotel.it

---

### 1.5. Presenza sui Social Media
Con la query `"concadorohotel" site:instagram.com`, è stato identificato il profilo Instagram ufficiale:
- **[@concadorohotel](https://www.instagram.com/hotel_ristorante_conca_doro/)**

---

## **2. Analisi con Maltego**

### 2.1. Creazione della Mappa del Grafo
In Maltego, è stato creato un grafo con le seguenti entità iniziali:
- **Dominio**: `concadorohotel.it`
- **Email**: info@concadorohotel.it
- **Telefono**: +39 045 7255275
- **Documenti**: Menù Bar, Menù Ristorante
- **Social**: Profilo Instagram ufficiale

---

### 2.2. Trasformazioni Eseguite
Per approfondire l'analisi, sono state applicate le seguenti trasformazioni:
1. **To DNS Name - NS (name server)**: Ha rivelato i server DNS associati:
   - `ns.abdns.biz`
   - `ns.abdns.info`
2. **To Domain Owner Detail**: Ha evidenziato che il dominio è gestito da Aruba.
3. **To DNS Name - MX (mail server)**: Ha mostrato che il servizio di posta è configurato su Aruba.
4. **To Domain (Find other TLDs)**: Nessun dominio aggiuntivo trovato.
5. **To Search Web [Bing]**: Ha rivelato collegamenti con alcuni siti secondari.

---

### 2.3. Nuove Entità Rilevate
L'analisi ha portato all'identificazione di:
- **Server DNS**:
  - `ns.abdns.biz`
  - `ns.abdns.info`
- **Email aggiuntive**:
  - `postmaster@arubabusiness.it` (gestione email di Aruba).
- **Siti Web Collegati**:
  - Alcuni domini non direttamente collegati al target (es. `biblioteca-digitala.org`, `stepone4.hh.ru`).

---

### 2.4. Screenshot del Grafo
Di seguito lo screenshot del grafo aggiornato:

![Alt text](./ScreenshotGraph.png "Graph tree concadorohotel.it")

---

## **3. Conclusioni**

L'attività di Information Gathering ha portato ai seguenti risultati:
- Il dominio `concadorohotel.it` è gestito dai server DNS di Aruba (`ns.abdns.biz` e `ns.abdns.info`).
- L'email **info@concadorohotel.it** è associata al dominio principale e utilizza i server di posta Aruba.
- Sono stati individuati file pubblici (menù del bar e del ristorante) e informazioni sui contatti ufficiali dell'hotel.
- L'account Instagram ufficiale è attivo e aggiornato.
- Alcuni siti web individuati potrebbero richiedere ulteriori approfondimenti per verificarne la rilevanza.

> **Nota**: Tutte le informazioni raccolte sono pubbliche e accessibili tramite ricerche OSINT.

---

## **Passaggi Effettuati**
1. **Raccolta dati con Google**:
   - Utilizzo di query mirate per ottenere dati pubblici.
2. **Analisi con Maltego**:
   - Creazione di un grafo per visualizzare relazioni tra entità.
   - Applicazione di trasformazioni per approfondire i collegamenti.
3. **Conclusione**:
   - Organizzazione dei risultati e creazione del report finale.

---
