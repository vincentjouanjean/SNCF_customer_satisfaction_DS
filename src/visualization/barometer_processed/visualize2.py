import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from IPython.core.display_functions import display

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

barometer = pd.read_csv('../../../data/processed/barometer_clean.csv')

display(barometer.info())

sns.pairplot(data=barometer[['_global', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7']], diag_kind='hist')

plt.show()
