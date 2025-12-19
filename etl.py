import pandas as pd

# EXTRACT
df = pd.read_csv('data/clienti_raw.csv')

# TRANSFORM
df['fatturato_annuo'] = df['spesa'] * 12

df_milano = df[df['citta'] == 'Milano']

fatturato_per_citta = (
    df.groupby('citta')['fatturato_annuo']
    .sum()
    .reset_index()
)

# LOAD
df_milano.to_csv('output_clienti_milano.csv', index=False)
fatturato_per_citta.to_csv('output_fatturato_citta.csv', index=False)

print('ETL completato con successo')
