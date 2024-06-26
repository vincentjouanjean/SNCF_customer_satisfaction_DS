import pandas as pd

from src.visualization.barometer_processed.IProcess import IProcess


class ProcessPonctualite(IProcess):
    def __init__(self, visualize_before, visualize_after):
        super().__init__(visualize_before, visualize_after)

    def transform(self):
        ponctualite = pd.read_csv('../../../data/raw/ponctualite/reglarite-mensuelle-tgv-nationale.csv', sep=';')

        self.df['period_year'] = self.df['period'].apply(lambda x: x.split(' ')[1])
        self.df['period_month'] = self.df['period'].apply(lambda x: x.split(' ')[0]
                                                          .replace('mars', "03")
                                                          .replace('mai', "05")
                                                          .replace('sept', "09"))
        self.df['period_year_month'] = self.df['period_year'] + '-' + self.df['period_month']

        merged = self.df.merge(ponctualite, how='left', left_on='period_year_month',
                               right_on='Date')

        self.df = merged
