import pandas as pd
from IPython.core.display_functions import display
from numpy.core.defchararray import upper

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

barometer = pd.read_csv('../../../data/processed/barometer_clean.csv')

barometer = barometer.loc[barometer['period'] == 'mai 2023']

proprete = pd.read_csv('../../../data/raw/proprete/proprete-en-gare.csv', sep=';')

proprete['UIC'] = proprete['UIC'].apply(lambda x: str(x)[2:])
barometer['Code UIC'] = barometer['Code UIC'].apply(lambda x: str(x))

merged = barometer.merge(proprete, how='left', left_on='Code UIC', right_on="UIC")

ff = merged.select_dtypes(include='number')
display(ff.corr())
