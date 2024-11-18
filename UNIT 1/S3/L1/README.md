# Esercizio S3/L1 - Sistemi Operativi

## Descrizione del progetto

In questo esercizio abbiamo analizzato tre approcci ai sistemi operativi per la gestione dei processi:
- **Sistemi mono-tasking**
- **Sistemi multi-tasking**
- **Sistemi time-sharing**

L'obiettivo era valutare le differenze tra i metodi di pianificazione e rappresentarli graficamente per comprenderne i vantaggi e gli svantaggi.

---

## Sistemi Mono-tasking
Nei sistemi mono-tasking, un solo processo alla volta utilizza la CPU fino al completamento o fino all'attesa di un evento esterno. Durante l'attesa, nessun altro processo viene eseguito, portando a tempi di inattività.

![Mono-tasking](mono_tasking.png)

---

## Sistemi Multi-tasking
Nei sistemi multi-tasking, i processi vengono gestiti in modo che la CPU venga occupata il più possibile. Se un processo entra in stato di attesa, un altro processo può essere eseguito. Questo riduce i tempi morti e aumenta l'efficienza.

![Multi-tasking](multi_tasking.png)

---

## Sistemi Time-sharing
Nei sistemi time-sharing, il tempo della CPU viene suddiviso in piccoli intervalli chiamati "quanti". Ogni processo riceve un quanto in modo ciclico, garantendo che tutti i processi abbiano accesso alla CPU in tempi relativamente brevi.

![Time-sharing](time_sharing.png)

---

## Conclusioni
- I sistemi mono-tasking, ormai obsoleti, soffrono di inefficienze dovute ai tempi morti della CPU durante l'attesa di eventi esterni.
- I sistemi multi-tasking migliorano l'efficienza sfruttando il tempo morto di un processo per eseguire altri processi.
- I sistemi time-sharing garantiscono una distribuzione equa della CPU tra i processi, riducendo i tempi di attesa per ogni processo.

Questi concetti sono fondamentali per comprendere il funzionamento dei moderni sistemi operativi e l'ottimizzazione delle risorse hardware.

