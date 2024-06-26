import pandas as pd

from src.visualization.barometer_processed.IProcess import IProcess


class ProcessWifi(IProcess):
    def __init__(self, visualize_before, visualize_after):
        super().__init__(visualize_before, visualize_after)

    def transform(self):
        wifi = pd.read_csv('../../../data/raw/voyage/gares-equipees-du-wifi.csv', sep=';')

        wifi['Code UIC'] = wifi['UIC'].apply(lambda x: str(x))

        wifi = wifi[['Code UIC', 'Service Wifi']]

        merged = self.df.merge(wifi, how='left', left_on='Code UIC', right_on="Code UIC")

        merged['Service Wifi'] = merged['Service Wifi'].replace({'Oui': 1, 'Non': 0})

        merged['Service Wifi'].fillna(value=0, inplace=True)

        self.df = merged
