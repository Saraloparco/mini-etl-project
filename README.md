# Mini ETL Project

Mini progetto ETL sviluppato in Python per simulare un flusso base di Data Engineering.

## Tecnologie
- Python
- Pandas

## Descrizione
Il progetto legge dati da un file CSV, esegue alcune trasformazioni
e salva i risultati in nuovi file CSV.

## Fasi ETL
- Extract: lettura del file clienti_raw.csv
- Transform:
  - calcolo del fatturato annuo
  - filtro clienti della città di Milano
  - aggregazione del fatturato per città
- Load: esportazione dei risultati in file CSV

## Esecuzione
