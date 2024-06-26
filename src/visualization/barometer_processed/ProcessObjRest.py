import pandas as pd

from src.visualization.barometer_processed.IProcess import IProcess


class ProcessObjRest(IProcess):
    def __init__(self, visualize_before, visualize_after):
        super().__init__(visualize_before, visualize_after)

    def transform(self):
        obj = pd.read_csv('../../../data/raw/obj/objets-trouves-restitution.csv', sep=';')

        obj = obj[obj['Code UIC'].notna()]
        obj['Code UIC'] = obj['Code UIC'].apply(lambda x: str(int(x))[2:])
        obj['Date'] = obj['Date'].apply(lambda x: x[:7])

        obj_count = obj[['Date', 'Code UIC']].groupby(['Date', 'Code UIC']).size().to_frame()

        self.df['period_year'] = self.df['period'].apply(lambda x: x.split(' ')[1])
        self.df['period_month'] = self.df['period'].apply(lambda x: x.split(' ')[0]
                                                          .replace('mars', "03")
                                                          .replace('mai', "05")
                                                          .replace('sept', "09"))
        self.df['period_year_month'] = self.df['period_year'] + '-' + self.df['period_month']

        merged = self.df.merge(obj_count, how='left', left_on=['period_year_month', "Code UIC"],
                               right_on=['Date', 'Code UIC'])

        merged[0].fillna(0, inplace=True)
        merged = merged.rename(columns={0: 'returned_items'})

        self.df = merged
