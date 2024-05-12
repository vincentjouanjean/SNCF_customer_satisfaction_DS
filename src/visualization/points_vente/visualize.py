import pandas as pd
from IPython.core.display_functions import display
from numpy.core.defchararray import upper

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

barometer = pd.read_csv('../../data/processed/barometer_clean.csv')

barometer = barometer.loc[barometer['period'] == 'mai 2023']

points_vente = pd.read_csv('../../data/raw/horaire/points-vente.csv', sep=';')

points_vente['Gare - code uic'] = points_vente['Gare - code uic'].apply(lambda x: str(x)[2:])
barometer['Code UIC'] = barometer['Code UIC'].apply(lambda x: str(x))

display(points_vente['Type de point de vente'].unique())

merged = barometer.merge(points_vente, how='left', left_on='Code UIC', right_on="Gare - code uic")

i = 0
for equip in merged['Type de point de vente'].unique():
    i += 1
    merged.replace(to_replace=equip, value=i, inplace=True)

display(merged['Type de point de vente'].unique())

ff = merged.select_dtypes(include='number')
display(ff.corr())

display(merged['Type de point de vente'].unique())

###
merged = barometer.merge(points_vente, how='left', left_on='Code UIC', right_on="Gare - code uic")

ff = merged.join(merged['Type de point de vente'].str.get_dummies())

ff = ff.select_dtypes(include='number')

display(ff.corr())

###

