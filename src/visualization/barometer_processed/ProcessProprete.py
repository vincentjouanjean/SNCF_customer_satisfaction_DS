import pandas as pd
from IPython.core.display_functions import display


class ProcessProprete:
    def __init__(self):
        self.next = None

    def process(self, df: pd.DataFrame, verbose: bool) -> pd.DataFrame:
        self.df = df

        proprete = pd.read_csv('../../../data/raw/proprete/proprete-en-gare.csv', sep=';')

        df['period_year'] = df['period'].apply(lambda x: x.split(' ')[1])
        df['period_month'] = df['period'].apply(lambda x: x.split(' ')[0]
                                                .replace('mars', "03")
                                                .replace('mai', "05")
                                                .replace('sept', "09"))
        df['period_year_month'] = df['period_year'] + '-' + df['period_month']

        proprete['Code UIC'] = proprete['UIC'].apply(lambda x: str(x)[2:])

        proprete_to_merge = proprete[['Mois', 'Code UIC', 'Taux de conformité']]

        merged = df.merge(proprete_to_merge, how='left', left_on=['period_year_month', "Code UIC"],
                          right_on=['Mois', 'Code UIC'])
        merged.drop('period_month', axis=1, inplace=True)
        merged.drop('period_year', axis=1, inplace=True)
        merged.drop('period_year_month', axis=1, inplace=True)
        merged.drop('Mois', axis=1, inplace=True)

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
