import pandas as pd
from IPython.core.display_functions import display

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

barometer = pd.read_csv('../../../data/processed/barometer_processed.csv')

display(barometer.isna().sum())

# Direction régionnale
display(barometer['DRG'].unique())

# Unité régionnale
display(barometer['Région (UG)'].unique())

# Typologie de la gare
display(barometer['Typologie de la gare'].unique())

display(barometer['Niveau de service'].unique())

display(barometer.describe())
