import numpy as np
import pandas as pd

from src.visualization.barometer.NewBarometerTransform import NewBarometerTransform
from src.visualization.barometer.OldBarometerTransform import OldBarometerTransform
from src.visualization.barometer.ValueTest import ValueTest

data = [NewBarometerTransform(), OldBarometerTransform()]
df = pd.DataFrame()
for data in data:
    df = pd.concat([df, data.transform()])

df.reset_index()
df = df.replace({',': '.'}, regex=True)

df.to_csv('../../data/processed/barometer.csv', index=False)

test = pd.read_csv('../../data/processed/barometer.csv')

vt_mai_2023 = ValueTest('mai 2023', 'MASSY TGV', 7.26, 8.35, 8.58, 8.13, 7.54, 7.54, 5.72, 6.67, test).verify()
vt_mars_2019 = ValueTest('mars 2019', 'DIJON VILLE', 7.42, 7.93, 8.49, 8.23, 7.74, 7.88, np.nan, np.nan, test).verify()
vt_mars_2021 = ValueTest('mars 2021', 'LYON PART DIEU', 7.10, 8, 8.19, 7.81, 6.81, 7.23, 5.08, 5.95, test).verify()
vt_mars_2022 = ValueTest('mars 2022', 'LAVAL', 7.29, 8.16,  8.69, 7.90, 7.46, 6.59, 5.90, 5.65, test).verify()
vt_sept_2019 = ValueTest('sept 2019', 'BOURGOIN JALLIEU', 7.32, 8,  8.13, 7.78, 7.29, 6.89, np.nan, np.nan, test).verify()
vt_sept_2020 = ValueTest('sept 2020', 'EVREUX NORMANDIE', 6.53, 8.22,  8.81, 6.89, 5.46, 4.83, np.nan, np.nan, test).verify()
vt_sept_2021 = ValueTest('sept 2021', 'LORIENT BRETAGNE SUD', 8.18, 8.63,  8.84, 8.72, 8.22, 7.60, 7.09, 6.89, test).verify()
vt_sept_2022 = ValueTest('sept 2022', 'DAX', 8.23, 8.49,  8.46, 8.51, 8.55, 7.70, 7.23, 7.43, test).verify()
