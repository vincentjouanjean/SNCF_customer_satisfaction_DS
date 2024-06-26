import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

barometer = pd.read_csv('../../../data/processed/barometer_processed.csv')

sns.boxplot(data=barometer['taux_proprete'])

plt.show()
