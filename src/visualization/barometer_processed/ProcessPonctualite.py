import numpy as np
import pandas as pd
from IPython.core.display_functions import display

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


class ProcessPonctualite:
    def __init__(self):
        self.next = None

    def process(self, df: pd.DataFrame, verbose: bool) -> pd.DataFrame:
        self.df = df

        ponctualite = pd.read_csv('../../../data/raw/ponctualite/reglarite-mensuelle-tgv-nationale.csv', sep=';')

        df['period_year'] = df['period'].apply(lambda x: x.split(' ')[1])
        df['period_month'] = df['period'].apply(lambda x: x.split(' ')[0]
                                                .replace('mars', "03")
                                                .replace('mai', "05")
                                                .replace('sept', "09"))
        df['period_year_month'] = df['period_year'] + '-' + df['period_month']

        display(ponctualite)

        merged = df.merge(ponctualite, how='left', left_on='period_year_month',
                          right_on='Date')

        if self.next is not None:
            return self.next.process(merged, verbose)
        else:
            return merged

    def visualize(self):
        display(self.df.shape)

        # promises are object type
        display(self.df.info())

        display(self.df.describe())

        display(self.df.head(5))

        # Direction régionnale
        display(self.df['Agence'].unique())

        # Unité régionnale
        display(self.df['Région (UG)'].unique())

        # Typologie de la gare
        display(self.df['Typologie de la gare'].unique())

        for code in ['Agence', 'Région (UG)', 'Typologie de la gare', 'Niveau de service', 'Gare']:
            self.df[[code, 'Code UIC']].groupby([code, 'Code UIC']).apply(lambda x: self.print_duplicates(x, code))

        # 255 na Code UIC
        display(self.df.isna().sum())

        # PERIGUEUX n'a pas le bon UIC code
        display(self.df[self.df[['Code UIC', 'period']].duplicated(keep=False)])

    def visualize_after_process(self):
        display(self.df.isna().sum())

        display(self.df.info())

        display(self.df.head(5))

        # Min _global = 5.11
        # Max _global = 8.96
        # Min des P = 4.36
        # Max des P = 9.72
        display(self.df.describe())

        # 474 null value P6 & P7
        display(self.df.isna().sum())

    def print_duplicates(self, x, code_):
        if len(x[code_].value_counts()) > 1:
            print(x[code_].value_counts())

    def set_next(self, next_process):
        self.next = next_process
