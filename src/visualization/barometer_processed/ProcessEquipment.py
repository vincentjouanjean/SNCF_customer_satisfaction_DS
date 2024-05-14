import pandas as pd
from IPython.core.display_functions import display
from numpy.core.defchararray import upper


class ProcessEquipment:
    def __init__(self):
        self.next = None

    def process(self, df: pd.DataFrame, verbose: bool) -> pd.DataFrame:
        self.df = df

        # barometer = pd.read_csv('../../../data/processed/barometer_clean.csv', index_col=0)
        equipment = pd.read_csv('../../../data/raw/equipement/equipements-accessibilite-en-gares.csv', sep=';')

        barometer_2021 = self.df.loc[self.df['period'] == 'sept 2021']
        barometer_not_2021 = self.df.loc[self.df['period'] != 'sept 2021']

        equipment['Code UIC'] = equipment['UIC'].apply(lambda x: str(x)[2:])

        equipment_count = equipment[['Code UIC', 'Accessibilité']].groupby('Code UIC')['Accessibilité'].count()

        equipment_count = equipment_count.fillna(0)

        equipment = equipment[['Code UIC', 'Accessibilité']].groupby('Code UIC')['Accessibilité'].apply(','.join).reset_index()

        merged = barometer_2021.merge(equipment, how='left', left_on='Code UIC', right_on="Code UIC")
        merged = merged.merge(equipment_count, how='left', left_on='Code UIC', right_on="Code UIC")

        merged = pd.concat([merged, barometer_not_2021])

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
