import pandas as pd
from numpy.core.defchararray import upper

barometer = pd.read_csv('../../../data/processed/barometer_clean.csv', index_col=0)

equipement = pd.read_csv('../../../data/raw/equipement/equipements-accessibilite-en-gares.csv', sep=';')

barometer_2021 = barometer.loc[barometer['period'] == 'sept 2021']
barometer_not_2021 = barometer.loc[barometer['period'] != 'sept 2021']

equipement['Nom de la gare'] = equipement['Nom de la gare'].apply(upper)

equipement = equipement[['Nom de la gare', 'Accessibilité']].groupby('Nom de la gare')['Accessibilité'].apply(','.join).reset_index()

merged = barometer_2021.merge(equipement, how='left', left_on='Gare', right_on="Nom de la gare")
merged = merged.drop(['Nom de la gare'], axis=1)

merged = pd.concat([merged, barometer_not_2021])

merged.to_csv('../../../data/processed/barometer_with_equipment.csv')
