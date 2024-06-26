import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from IPython.core.display_functions import display

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

barometer = pd.read_csv('../../../data/processed/barometer_clean.csv')

barometer['period_year'] = barometer['period'].apply(lambda x: x.split(' ')[1])
barometer['period_month'] = barometer['period'].apply(lambda x: x.split(' ')[0]
                                                      .replace('mars', "03")
                                                      .replace('mai', "05")
                                                      .replace('sept', "09"))
barometer['period_year_month'] = barometer['period_year'] + '-' + barometer['period_month']
merged = barometer.groupby('period_year_month')['_global'].mean().to_frame()
for i in range(1, 8):
    merged = merged.merge(barometer.groupby('period_year_month')['p' + str(i)].mean().to_frame(),
                          left_index=True, right_index=True)

merged.rename(columns={'_global': 'global'}, inplace=True)

display(merged)

sns.lineplot(data=merged, marker='o')

plt.show()
