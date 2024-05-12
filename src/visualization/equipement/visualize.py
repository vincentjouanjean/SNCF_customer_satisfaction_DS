import pandas as pd
from IPython.core.display_functions import display
from numpy.core.defchararray import upper

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

barometer = pd.read_csv('../../data/processed/barometer_clean.csv')

equipement = pd.read_csv('../../data/raw/equipement/equipements-accessibilite-en-gares.csv', sep=';')

barometer = barometer.loc[barometer['period'] == 'sept 2021']

display(barometer.head(5))
display(equipement.head(5))
display(equipement.info())

equipement['Nom de la gare'] = equipement['Nom de la gare'].apply(upper)

merged = barometer.merge(equipement, how='left', left_on='Gare', right_on="Nom de la gare")

display(merged.head(15))

i = 0
for equip in merged['Accessibilité'].unique():
    i += 1
    merged.replace(to_replace=equip, value=i, inplace=True)

display(merged['Accessibilité'].unique())

ff = merged.select_dtypes(include='number')

display(ff.corr())

equipement2 = equipement[['Nom de la gare', 'Accessibilité']].groupby('Nom de la gare')['Accessibilité'].apply(','.join).reset_index()

merged = barometer.merge(equipement2, how='left', left_on='Gare', right_on="Nom de la gare")

i = 0
for equip in merged['Accessibilité'].unique():
    i += 1
    merged.replace(to_replace=equip, value=i, inplace=True)

#display(merged['Accessibilité'].unique())

ff = merged.select_dtypes(include='number')

display(ff.corr())

equipement3 = equipement[['Nom de la gare', 'Accessibilité']].groupby('Nom de la gare')['Accessibilité'].count()

equipement3 = equipement3.fillna(0)

#display(equipement3)

merged = barometer.merge(equipement3, how='left', left_on='Gare', right_on="Nom de la gare")

#display(merged)

ff = merged.select_dtypes(include='number')

display(ff.corr())

#
print('---------------')
merged = barometer.merge(equipement, how='left', left_on='Gare', right_on="Nom de la gare")

ff = merged.join(merged['Accessibilité'].str.get_dummies())

ff = ff.select_dtypes(include='number')

display(ff.corr())

