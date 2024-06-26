import pandas as pd

from src.visualization.barometer_processed.IProcess import IProcess


class ProcessPiano(IProcess):
    def __init__(self, visualize_before, visualize_after):
        super().__init__(visualize_before, visualize_after)

    def transform(self):
        piano = pd.read_csv('../../../data/raw/gare/gares-pianos.csv', sep=';')

        piano = piano[piano['UIC'].notna()]
        piano['Code UIC'] = piano['UIC'].apply(lambda x: str(int(x))[2:])
        piano.drop(['Gare'], axis=1, inplace=True)

        merged = self.df.merge(piano, how='left', left_on='Code UIC', right_on="Code UIC")

        merged.rename(columns={'total': 'service_attente_quantity'}, inplace=True)
        merged['Piano'] = merged['Piano'].fillna(0)
        merged['Power&Station'] = merged['Power&Station'].fillna(0)
        merged['Baby-Foot'] = merged['Baby-Foot'].fillna(0)
        merged['Distr Histoires Courtes'] = merged['Distr Histoires Courtes'].fillna(0)
        merged['service_attente_quantity'] = merged['service_attente_quantity'].fillna(0)
        merged.drop('UIC', axis=1, inplace=True)

        self.df = merged
