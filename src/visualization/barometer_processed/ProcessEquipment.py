import pandas as pd

from src.visualization.barometer_processed.IProcess import IProcess


class ProcessEquipment(IProcess):
    def __init__(self, visualize_before, visualize_after):
        super().__init__(visualize_before, visualize_after)

    def transform(self):
        equipment = pd.read_csv('../../../data/raw/equipement/equipements-accessibilite-en-gares.csv', sep=';')

        equipment['Code UIC'] = equipment['UIC'].apply(lambda x: str(x)[2:])
        equipment = equipment[['Code UIC', 'Accessibilité']]
        equipment_count = equipment[['Code UIC', 'Accessibilité']].groupby('Code UIC')['Accessibilité'].count()
        equipment_count = equipment_count.fillna(0)

        equipment = equipment[['Code UIC', 'Accessibilité']].groupby('Code UIC')['Accessibilité'].apply(
            '||'.join).reset_index()

        merged = self.merged('mai 2023', self.df, equipment, equipment_count)
        merged = self.merged('sept 2022', merged, equipment, equipment_count)
        merged = self.merged('mars 2022', merged, equipment, equipment_count)
        merged = self.merged('sept 2021', merged, equipment, equipment_count)
        merged = self.merged('mars 2021', merged, equipment, equipment_count)
        merged = self.merged('sept 2020', merged, equipment, equipment_count)
        merged = self.merged('sept 2019', merged, equipment, equipment_count)
        merged = self.merged('mars 2019', merged, equipment, equipment_count)

        equips = equipment['Accessibilité'].unique()
        unique_equips = []
        for equip in equips:
            unique_equips.extend(equip.split('||'))
        for equip in set(unique_equips):
            merged[equip] = merged['accessibilite_list'].apply(lambda x: self.is_equipped(x, equip))

        merged['accessibilite_list'] = merged['accessibilite_list'].fillna(' ')
        merged = merged.fillna(0)

        self.df = merged

    @staticmethod
    def merged(period, df, equip, equip_count):
        barometer_year = df.loc[df['period'] == period]
        barometer_not_year = df.loc[df['period'] != period]
        barometer_year = barometer_year.drop(columns=['accessibilite_list', 'accessibilite_quantity'],
                                             errors='ignore')
        merged_tmp = barometer_year.merge(equip, how='left', left_on='Code UIC', right_on="Code UIC")
        merged_tmp = merged_tmp.merge(equip_count, how='left', left_on='Code UIC', right_on="Code UIC")
        merged_tmp.rename(columns={'Accessibilité_x': 'accessibilite_list'}, inplace=True)
        merged_tmp.rename(columns={'Accessibilité_y': 'accessibilite_quantity'}, inplace=True)
        return pd.concat([merged_tmp, barometer_not_year])

    @staticmethod
    def is_equipped(x, equip):
        if str(x) != 'nan':
            if equip in x:
                return 1
            else:
                return 0
        else:
            return 0
