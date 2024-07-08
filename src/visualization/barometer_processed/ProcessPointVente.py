import pandas as pd

from src.visualization.barometer_processed.IProcess import IProcess


def yes_or_not(x):
    if isinstance(x, str) and 'Oui' in x:
        return 1
    else:
        return 0


class ProcessPointVente(IProcess):
    def __init__(self, visualize_before, visualize_after):
        super().__init__(visualize_before, visualize_after)

    def transform(self):
        point = pd.read_csv('../../../data/raw/horaire/points-vente.csv', sep=';')

        point['Code UIC'] = point['Gare - code uic'].apply(lambda x: str(int(x))[2:])

        point_type1 = point[['Code UIC', 'Type de point de vente', 'CB', 'Chèque', 'Espèces']].groupby('Code UIC')[
            'Type de point de vente'].apply(','.join).reset_index()
        point_type2 = point[['Code UIC', 'Type de point de vente', 'CB', 'Chèque', 'Espèces']].groupby('Code UIC')[
            'CB'].apply(','.join).reset_index()
        point_type3 = point[['Code UIC', 'Type de point de vente', 'CB', 'Chèque', 'Espèces']].groupby('Code UIC')[
            'Chèque'].apply(','.join).reset_index()
        point_type4 = point[['Code UIC', 'Type de point de vente', 'CB', 'Chèque', 'Espèces']].groupby('Code UIC')[
            'Espèces'].apply(','.join).reset_index()

        merged = self.df.merge(point_type1, how='left', left_on='Code UIC', right_on="Code UIC")
        merged = merged.merge(point_type2, how='left', left_on='Code UIC', right_on="Code UIC")
        merged = merged.merge(point_type3, how='left', left_on='Code UIC', right_on="Code UIC")
        merged = merged.merge(point_type4, how='left', left_on='Code UIC', right_on="Code UIC")

        merged['CB'] = merged['CB'].apply(lambda x: yes_or_not(x))
        merged['Chèque'] = merged['Chèque'].apply(lambda x: yes_or_not(x))
        merged['Espèces'] = merged['Espèces'].apply(lambda x: yes_or_not(x))
        merged['Type de point de vente'] = merged['Type de point de vente'].fillna(' ')

        merged['Poste de vente guichet'] = merged['Type de point de vente'].apply(lambda x: self.is_present(x, 'Poste de vente guichet'))
        merged['Automates TGV-Intercités'] = 'Automates TGV-Intercités' in merged['Type de point de vente']
        merged['Automates TER'] = 'Automates TER' in merged['Type de point de vente']
        merged['Libre-Service Assisté'] = 'Libre-Service Assisté' in merged['Type de point de vente']

        merged = merged.drop(['Type de point de vente'], axis=1)

        self.df = merged

    @staticmethod
    def is_present(x, equip):
        if isinstance(x, str) and equip in x:
            return 1
        else:
            return 0
