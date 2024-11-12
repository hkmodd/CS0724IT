# Consegna S1/L2 ✉️

## Calcolo degli Ottetti nelle Reti IP

Questo documento descrive il processo di calcolo per ottenere le informazioni chiave della rete (come indirizzo di rete, gateway convenzionale, broadcast, e la suddivisione degli ottetti) partendo dagli indirizzi IP e dalle subnet mask assegnate.

---

### 1. Indirizzo IP: 128.1.6.5/12
- **Subnet Mask**: /12 significa che i primi 12 bit sono riservati per la rete.
  
**Calcoli**:
1. La subnet mask in binario è: `11111111.11110000.00000000.00000000` (i primi 12 bit sono '1').
2. **IP Network**: Impostiamo i bit degli host a zero nel secondo e terzo ottetto → `128.0.0.0`.
3. **IP Gateway Convenzionale**: È il primo indirizzo utile della rete, quindi `128.0.0.1`.
4. **IP Broadcast**: Impostiamo i bit degli host a '1' → `128.15.255.255`.
5. **Calcolo Ottetti**:
   - Ottetti per la network: i primi 12 bit coprono 1 ottetto e mezzo (8 bit nel primo ottetto e 4 nel secondo).
   - Ottetti per gli host: i restanti 20 bit coprono i 3 ottetti rimanenti.

---

### 2. Indirizzo IP: 200.1.2.3/24
- **Subnet Mask**: /24 indica che i primi 24 bit sono riservati alla rete.

**Calcoli**:
1. La subnet mask in binario è: `11111111.11111111.11111111.00000000` (24 bit di '1').
2. **IP Network**: Impostiamo gli 8 bit dell'ultimo ottetto a zero → `200.1.2.0`.
3. **IP Gateway Convenzionale**: Il primo indirizzo utile è `200.1.2.1`.
4. **IP Broadcast**: Impostiamo gli 8 bit dell’ultimo ottetto a '1' → `200.1.2.255`.
5. **Calcolo Ottetti**:
   - Ottetti per la network: /24 copre 3 ottetti completi (24 bit).
   - Ottetti per gli host: gli 8 bit dell'ultimo ottetto restano per gli host.

---

### 3. Indirizzo IP: 192.192.1.1/22
- **Subnet Mask**: /22 significa che i primi 22 bit sono riservati alla rete.

**Calcoli**:
1. La subnet mask in binario è: `11111111.11111111.11111100.00000000` (22 bit di '1').
2. **IP Network**: Impostiamo i bit dell'host a zero nei primi due ottetti e nei primi 6 bit del terzo ottetto → `192.192.0.0`.
3. **IP Gateway Convenzionale**: Il primo indirizzo utile è `192.192.0.1`.
4. **IP Broadcast**: Impostiamo i bit dell’host a '1' nei 10 bit rimanenti → `192.192.3.255`.
5. **Calcolo Ottetti**:
   - Ottetti per la network: /22 copre 2 ottetti e mezzo (16 bit nei primi due ottetti, più 6 bit nel terzo).
   - Ottetti per gli host: 1.5 ottetti (i restanti 10 bit) restano per gli host.

---

### 4. Indirizzo IP: 126.5.4.3/9
- **Subnet Mask**: /9 indica che i primi 9 bit sono riservati alla rete.

**Calcoli**:
1. La subnet mask in binario è: `11111111.10000000.00000000.00000000` (9 bit di '1').
2. **IP Network**: Impostiamo i bit dell'host a zero → `126.0.0.0`.
3. **IP Gateway Convenzionale**: Il primo indirizzo utile è `126.0.0.1`.
4. **IP Broadcast**: Impostiamo i bit dell’host a '1' nei 23 bit rimanenti → `126.127.255.255`.
5. **Calcolo Ottetti**:
   - Ottetti per la network: 1.125 ottetti (8 bit nel primo ottetto e 1 bit del secondo).
   - Ottetti per gli host: 3.5 ottetti (i restanti 23 bit) restano per gli host.

---

### 5. Indirizzo IP: 200.1.9.8/24
- **Subnet Mask**: /24 (24 bit riservati per la rete).

**Calcoli**:
1. La subnet mask è la stessa della maschera /24 precedente: `11111111.11111111.11111111.00000000`.
2. **IP Network**: Gli ultimi 8 bit sono impostati a zero → `200.1.9.0`.
3. **IP Gateway Convenzionale**: Il primo indirizzo utile è `200.1.9.1`.
4. **IP Broadcast**: Gli ultimi 8 bit dell’host sono impostati a '1' → `200.1.9.255`.
5. **Calcolo Ottetti**:
   - Ottetti per la network: Copre interamente i primi 3 ottetti (24 bit).
   - Ottetti per gli host: Gli 8 bit dell'ultimo ottetto restano per gli host.

---

### 6. Indirizzo IP: 172.16.0.4/16
- **Subnet Mask**: /16 (16 bit riservati alla rete).

**Calcoli**:
1. La subnet mask in binario è: `11111111.11111111.00000000.00000000`.
2. **IP Network**: Impostiamo i bit dell’host a zero nei primi due ottetti → `172.16.0.0`.
3. **IP Gateway Convenzionale**: Il primo indirizzo utile è `172.16.0.1`.
4. **IP Broadcast**: Impostiamo tutti i bit dell'host a '1' nei successivi 16 bit → `172.16.255.255`.
5. **Calcolo Ottetti**:
   - Ottetti per la network: /16 copre 2 ottetti interi (16 bit).
   - Ottetti per gli host: Gli altri 2 ottetti restano per gli host.

---

## Conclusioni
Questo esercizio fa vedere come facile si possa ottenere i tre indirizzi fondamentali di una rete (rete, gateway, e broadcast) e il ripartimento degli ottetti in network e host, tramite alcune operazioni binarie. A tale scopo, abbiamo seguito questi passaggi per ogni indirizzo e maschera, in linea di principio impegnandoci a non utilizzare i bit di subnet e quelli per gli host oltre quelli richiesti da ogni maschera.
