import pandas as pd
from IPython.core.display_functions import display
from numpy.core.defchararray import upper


class ProcessEquipment:
    def __init__(self):
        self.next = None

    def merged(self, period, df, equip, equip_count):
        barometer_year = df.loc[df['period'] == period]
        barometer_not_year = df.loc[df['period'] != period]
        barometer_year = barometer_year.drop(columns=['accessibilite_list', 'accessibilite_quantity'],
                                             errors='ignore')
        # equip_count.rename(columns={'Accessibilité': 'accessibilite_quantity'}, inplace=True)
        merged_tmp = barometer_year.merge(equip, how='left', left_on='Code UIC', right_on="Code UIC")
        merged_tmp = merged_tmp.merge(equip_count, how='left', left_on='Code UIC', right_on="Code UIC")
        display(merged_tmp.head(5))
        merged_tmp.rename(columns={'Accessibilité_x': 'accessibilite_list'}, inplace=True)
        merged_tmp.rename(columns={'Accessibilité_y': 'accessibilite_quantity'}, inplace=True)
        return pd.concat([merged_tmp, barometer_not_year])

    def process(self, df: pd.DataFrame, verbose: bool) -> pd.DataFrame:
        self.df = df

        # barometer = pd.read_csv('../../../data/processed/barometer_clean.csv', index_col=0)
        equipment = pd.read_csv('../../../data/raw/equipement/equipements-accessibilite-en-gares.csv', sep=';')

        equipment['Code UIC'] = equipment['UIC'].apply(lambda x: str(x)[2:])
        equipment = equipment[['Code UIC', 'Accessibilité']]
        equipment_count = equipment[['Code UIC', 'Accessibilité']].groupby('Code UIC')['Accessibilité'].count()
        equipment_count = equipment_count.fillna(0)

        equipment = equipment[['Code UIC', 'Accessibilité']].groupby('Code UIC')['Accessibilité'].apply(','.join).reset_index()

        merged = self.merged('mai 2023', df, equipment, equipment_count)
        merged = self.merged('sept 2022', merged, equipment, equipment_count)
        merged = self.merged('mars 2022', merged, equipment, equipment_count)
        merged = self.merged('sept 2021', merged, equipment, equipment_count)
        merged = self.merged('mars 2021', merged, equipment, equipment_count)
        merged = self.merged('sept 2020', merged, equipment, equipment_count)
        merged = self.merged('sept 2019', merged, equipment, equipment_count)
        merged = self.merged('mars 2019', merged, equipment, equipment_count)

        # barometer_2021 = self.df.loc[self.df['period'] == 'sept 2021']
        # barometer_not_2021 = self.df.loc[self.df['period'] != 'sept 2021']

        # merged = barometer_2021.merge(equipment2, how='left', left_on='Code UIC', right_on="Code UIC")
        # merged = merged.merge(equipment_count, how='left', left_on='Code UIC', right_on="Code UIC")

        # merged = pd.concat([merged, barometer_not_2021])

        # merged.rename(columns={'Accessibilité': 'accessibilite_list'}, inplace=True)
        # merged.rename(columns={'Accessibilité_y': 'accessibilite_quantity'}, inplace=True)

        equips = equipment['Accessibilité'].unique()
        for equip in equips:
            merged[equip] = merged['accessibilite_list'].apply(lambda x: self.ok(x, equip))

        merged['accessibilite_quantity'] = merged['accessibilite_quantity'].fillna(0)

        if self.next is not None:
            return self.next.process(merged, verbose)
        else:
            return merged

    def ok(self, x, equip):
        if str(x) != 'nan':
            if equip in x:
                return 1
            else:
                return 0
        else:
            return 0

    def visualize(self):
        display(self.df.shape)

    def visualize_after_process(self):
        display(self.df.isna().sum())

    def set_next(self, next_process):
        self.next = next_process
