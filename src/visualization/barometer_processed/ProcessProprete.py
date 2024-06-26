import pandas as pd

from src.visualization.barometer_processed.IProcess import IProcess


class ProcessProprete(IProcess):
    def __init__(self, visualize_before, visualize_after):
        super().__init__(visualize_before, visualize_after)

    def transform(self):
        proprete = pd.read_csv('../../../data/raw/proprete/proprete-en-gare.csv', sep=';')

        self.df['period_year'] = self.df['period'].apply(lambda x: x.split(' ')[1])
        self.df['period_month'] = self.df['period'].apply(lambda x: x.split(' ')[0]
                                                          .replace('mars', "03")
                                                          .replace('mai', "05")
                                                          .replace('sept', "09"))
        self.df['period_year_month'] = self.df['period_year'] + '-' + self.df['period_month']

        proprete['Code UIC'] = proprete['UIC'].apply(lambda x: str(x)[2:])

        proprete_to_merge = proprete[['Mois', 'Code UIC', 'Taux de conformité']]

        merged = self.df.merge(proprete_to_merge, how='left', left_on=['period_year_month', "Code UIC"],
                               right_on=['Mois', 'Code UIC'])
        merged.drop('period_month', axis=1, inplace=True)
        merged.drop('period_year', axis=1, inplace=True)
        merged.drop('period_year_month', axis=1, inplace=True)
        merged.drop('Mois', axis=1, inplace=True)

        merged.rename(columns={'Taux de conformité': 'taux_proprete'}, inplace=True)

        merged['taux_proprete'] = merged['taux_proprete'].fillna(merged['taux_proprete'].mean())

        self.df = merged
