import numpy as np
import pandas as pd
from IPython.core.display_functions import display

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

barometer = pd.read_csv('../../data/processed/barometer.csv')

display(barometer.shape)

# promises are object type
display(barometer.info())

display(barometer.describe())

display(barometer.head(5))

# Direction régionnale
display(barometer['Agence'].unique())

barometer = barometer.rename(columns={'Agence': 'DRG'})

# Unité régionnale
display(barometer['Région (UG)'].unique())

# Replacement '24' par 'Gare A - 24'
barometer['Typologie de la gare'] = barometer['Typologie de la gare'].replace({'24': 'Gare A - 24'})

# Typologie de la gare
display(barometer['Typologie de la gare'].unique())

display(barometer['Typologie de la gare'].unique())


def print_duplicates(x, code_):
    if len(x[code_].value_counts()) > 1:
        print(x[code_].value_counts())


for code in ['DRG', 'Région (UG)', 'Typologie de la gare', 'Niveau de service', 'Gare']:
    barometer[[code, 'Code UIC']].groupby([code, 'Code UIC']).apply(lambda x: print_duplicates(x, code))

# 255 na Code UIC
display(barometer.isna().sum())

barometer = barometer[barometer['Code UIC'].notna()]

# 474 null value P6 & P7
display(barometer.isna().sum())

# Convert P to float
for code in ['_global', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7']:
    barometer[code] = barometer[code].replace({'-': np.nan})
    barometer[code] = pd.to_numeric(barometer[code])

# Convert Code UIC to string
barometer['Code UIC'] = barometer['Code UIC'].apply(lambda x: str(int(x)))

display(barometer.isna().sum())

display(barometer.info())

display(barometer.head(5))

# Min _global = 5.11
# Max _global = 8.96
# Min des P = 4.36
# Max des P = 9.72
display(barometer.describe())

barometer.to_csv('../../data/processed/barometer_clean.csv')
