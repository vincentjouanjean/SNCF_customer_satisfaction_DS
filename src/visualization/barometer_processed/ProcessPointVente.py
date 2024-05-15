import pandas as pd
from IPython.core.display_functions import display


class ProcessPointVente:
    def __init__(self):
        self.next = None

    def process(self, df: pd.DataFrame, verbose: bool) -> pd.DataFrame:
        self.df = df

        # barometer = pd.read_csv('../../../data/processed/barometer_clean.csv', index_col=0)
        point = pd.read_csv('../../../data/raw/horaire/points-vente.csv', sep=';')

        point['Code UIC'] = point['Gare - code uic'].apply(lambda x: str(int(x))[2:])

        point_type1 = point[['Code UIC', 'Type de point de vente', 'CB', 'Chèque', 'Espèces']].groupby('Code UIC')['Type de point de vente'].apply(','.join).reset_index()
        point_type2 = point[['Code UIC', 'Type de point de vente', 'CB', 'Chèque', 'Espèces']].groupby('Code UIC')['CB'].apply(','.join).reset_index()
        point_type3 = point[['Code UIC', 'Type de point de vente', 'CB', 'Chèque', 'Espèces']].groupby('Code UIC')['Chèque'].apply(','.join).reset_index()
        point_type4 = point[['Code UIC', 'Type de point de vente', 'CB', 'Chèque', 'Espèces']].groupby('Code UIC')['Espèces'].apply(','.join).reset_index()

        merged = df.merge(point_type1, how='left', left_on='Code UIC', right_on="Code UIC")
        merged = merged.merge(point_type2, how='left', left_on='Code UIC', right_on="Code UIC")
        merged = merged.merge(point_type3, how='left', left_on='Code UIC', right_on="Code UIC")
        merged = merged.merge(point_type4, how='left', left_on='Code UIC', right_on="Code UIC")

        #merged = merged.merge(point_payment, how='left', left_on='Code UIC', right_on="Code UIC")
        # merged.drop('Gare - code uic', axis=1, inplace=True)
        # merged.drop('Pays', axis=1, inplace=True)
        # merged.drop('Région', axis=1, inplace=True)
        # merged.drop('Adresse', axis=1, inplace=True)
        # merged.drop('Ville', axis=1, inplace=True)
        #merged.drop('Gare', axis=1, inplace=True)

        if self.next is not None:
            return self.next.process(merged, verbose)
        else:
            return merged

    def visualize(self):
        display(self.df.shape)

    def visualize_after_process(self):
        display(self.df.isna().sum())

    def set_next(self, next_process):
        self.next = next_process

    def set_next(self, next_process):
        self.next = next_process
