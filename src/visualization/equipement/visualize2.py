import pandas as pd
from IPython.core.display_functions import display
from numpy.core.defchararray import upper

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

barometer = pd.read_csv('../../data/processed/barometer_clean.csv')

equipement = pd.read_csv('../../data/raw/equipement/referentiel-equipements-gares-.csv', sep=';')

display(barometer.head(5))
display(equipement.head(5))
display(equipement.info())

merged = barometer.merge(equipement, how='left', left_on='Code UIC', right_on="Code gare")

display(merged.head(15))

i = 0
for equip in merged['Nom'].unique():
    i += 1
    merged.replace(to_replace=equip, value=i, inplace=True)

display(merged['Nom'].unique())

ff = merged.select_dtypes(include='number')

display(ff.corr())

equipement2 = equipement[['Nom de la gare', 'Nom']].groupby('Nom de la gare')['Nom'].apply(','.join).reset_index()

merged = barometer.merge(equipement2, how='left', left_on='Code UIC', right_on="Code gare")

i = 0
for equip in merged['Nom'].unique():
    i += 1
    merged.replace(to_replace=equip, value=i, inplace=True)

display(merged['Nom'].unique())

ff = merged.select_dtypes(include='number')

display(ff.corr())

equipement3 = equipement[['Nom de la gare', 'Nom']].groupby('Nom de la gare')['Nom'].count()

equipement3 = equipement3.fillna(0)

display(equipement3)

merged = barometer.merge(equipement3, how='left', left_on='Code UIC', right_on="Code gare")

display(merged)

ff = merged.select_dtypes(include='number')

display(ff.corr())

