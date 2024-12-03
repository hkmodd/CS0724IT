# 🛠️ Esercitazione Extra

### Documentazione sugli switch avanzati di Nmap

#### 1. **Switch `-g`**
- Lo switch `-g <porta>` permette di impostare manualmente il numero di porta sorgente utilizzato da Nmap per inviare i pacchetti. 
- **Scopo**:
  - Questo può essere utile per aggirare firewall che filtrano in base alla porta sorgente.
  - Ad esempio:
    ```bash
    nmap -g 80 192.168.60.2
    ```
    - Utilizza la porta sorgente 80 per inviare i pacchetti, camuffando il traffico come se provenisse da un server web.

#### 2. **Switch `-f`**
- Lo switch `-f` frammenta i pacchetti generati da Nmap in segmenti più piccoli.
- **Scopo**:
  - È utile per bypassare firewall che si basano su una semplice ispezione dei pacchetti.
  - Ad esempio:
    ```bash
    nmap -f 192.168.60.2
    ```
    - Genera pacchetti frammentati per cercare di evitare rilevamenti da parte di sistemi IDS.

#### Analisi con Wireshark:
- Con Wireshark è possibile osservare come:
  - **`-g`** altera la porta sorgente nei pacchetti in uscita.
  - **`-f`** suddivide i pacchetti in frammenti più piccoli, visibili come pacchetti multipli con il flag `More Fragments`.

---

### 3. **Switch `-D`**
- Lo switch `-D` permette di specificare indirizzi IP "decoy" per mascherare il vero indirizzo IP dell'host che esegue la scansione.
- **Scopo**:
  - Aumenta l'anonimato dell'utente confondendo eventuali sistemi IDS.
  - Ad esempio:
    ```bash
    nmap -D 192.168.1.100,192.168.1.101 192.168.60.2
    ```
    - Genera traffico simulato come se provenisse dagli indirizzi IP 192.168.1.100 e 192.168.1.101, rendendo difficile identificare il vero scanner.

#### Switch avanzato `-D RND:10`
- L'opzione `RND:<numero>` genera un numero casuale di IP "decoy".
- Ad esempio:
    ```bash
    nmap -D RND:10 192.168.60.2
    ```
    - Genera 10 indirizzi IP casuali come "decoy" per confondere i sistemi di rilevamento.

---

### 4. **Uso combinato delle porte con `-p`**
- È possibile specificare porte sia UDP che TCP con lo switch `-p`.
- **Formato**:
  ```bash
  nmap -p u:<porta_udp>,t:<porta_tcp> <target>
  ```
- **Esempio**:
  ```bash
  nmap -p u:53,t:200 192.168.60.2
  ```
  - Scansiona la porta UDP 53 (DNS) e la porta TCP 200.
- **Nota**:
  - È corretto utilizzare questa sintassi, poiché consente di specificare contemporaneamente protocolli diversi.

---

### Conclusioni
Gli switch `-g`, `-f`, e `-D` offrono opzioni avanzate per migliorare l'efficacia e l'anonimato delle scansioni Nmap, mentre l'uso combinato delle porte con `-p` consente un maggiore controllo sulle scansioni. Tuttavia, l'uso di queste funzionalità in ambienti reali deve essere sempre conforme a normative legali ed etiche.
