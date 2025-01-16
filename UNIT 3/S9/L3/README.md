
# Pratica S9/L3 - **Business Continuity & Disaster Recovery** 💼🌍

In questa pratica, abbiamo analizzato l'impatto economico di vari disastri su asset critici di una compagnia, calcolando i valori di **Single Loss Expectancy (SLE)** e **Annualized Loss Expectancy (ALE)** per ogni scenario.

---

## 📝 **Obiettivo**
Determinare la perdita economica annuale associata a ciascun disastro sugli asset seguenti:
1. **Inondazione sull'edificio secondario**.
2. **Terremoto sul datacenter**.
3. **Incendio sull'edificio primario**.
4. **Incendio sull'edificio secondario**.
5. **Inondazione sull'edificio primario**.
6. **Terremoto sull'edificio primario**.

---

## 📚 **Dati Forniti**

### **Valore degli Asset**:
- **Edificio Primario**: 350.000 €
- **Edificio Secondario**: 150.000 €
- **Datacenter**: 100.000 €

### **Frequenza degli Eventi (ARO)**:
- **Terremoto**: 1 ogni 30 anni (**ARO = 0,033**)
- **Incendio**: 1 ogni 20 anni (**ARO = 0,05**)
- **Inondazione**: 1 ogni 50 anni (**ARO = 0,02**)

### **Exposure Factor (EF)**:
| Asset               | Terremoto (%) | Incendio (%) | Inondazione (%) |
|---------------------|---------------|--------------|-----------------|
| **Edificio Primario**  | 80%           | 60%          | 55%             |
| **Edificio Secondario**| 80%           | 50%          | 40%             |
| **Datacenter**        | 95%           | 60%          | 35%             |

---

## 🧮 **Formule Utilizzate**

1. **Single Loss Expectancy (SLE)**:
   \[
   SLE = 	ext{Valore dell'asset (AV)} 	imes 	ext{Exposure Factor (EF)}
   \]

2. **Annualized Loss Expectancy (ALE)**:
   \[
   ALE = SLE 	imes 	ext{Annualized Rate of Occurrence (ARO)}
   \]

---

## 📊 **Esempio di Calcolo**

### **Incendio sull'Edificio Primario**:
1. **Valore dell'asset (AV)**: 350.000 €
2. **Exposure Factor (EF)**: 60% (**0,6**)
3. **Annualized Rate of Occurrence (ARO)**: 0,05

#### Calcoli:
- **SLE**: \( 350.000 	imes 0,6 = 210.000 \, € \)
- **ALE**: \( 210.000 	imes 0,05 = 10.500 \, € \)

---

## 📂 **Risultati Finali**

I risultati per tutti gli scenari sono stati organizzati in un foglio di calcolo. Ogni riga rappresenta:
- L'**asset** coinvolto.
- Il **tipo di disastro**.
- Il valore calcolato di **SLE**.
- Il valore calcolato di **ALE**.

Puoi scaricare il foglio di calcolo qui: [Pratica S9 L3 - Analisi Disastro](Pratica_S9_L3_Analisi_Disastro.xlsx).

---

## 🛠️ **Strumenti Utilizzati**
- **Python**: per calcolare e organizzare i risultati.
- **Pandas**: per elaborare i dati e salvare il foglio di calcolo.
- **Excel**: per una presentazione chiara e strutturata.

---

## 🚨 **Nota Importante**
Questa analisi è a scopo didattico. I dati, le formule e i risultati possono essere personalizzati per scenari reali. Utilizzare con responsabilità.

---

🔒 **Autore**: Sebastiano  
📅 **Data**: Gennaio 2025  
