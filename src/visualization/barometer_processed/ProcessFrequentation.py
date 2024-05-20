import pandas as pd
from IPython.core.display_functions import display

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


class ProcessFrequentation:
    def __init__(self):
        self.next = None

    def merged(self, year, period, df, freq):
        barometer_year = df.loc[df['period'] == period]
        barometer_not_year = df.loc[df['period'] != period]
        barometer_year = barometer_year.drop(columns=['Total Voyageurs', 'Total Voyageurs + Non voyageurs'],
                                             errors='ignore')

        freq_year = freq[['Code UIC', 'Total Voyageurs ' + year, 'Total Voyageurs + Non voyageurs ' + year]]
        freq_year = freq_year.rename(columns={
            'Total Voyageurs ' + year: 'Total Voyageurs',
            'Total Voyageurs + Non voyageurs ' + year: 'Total Voyageurs + Non voyageurs'
        })
        merged_tmp = barometer_year.merge(freq_year, how='left', left_on='Code UIC', right_on="Code UIC")
        return pd.concat([merged_tmp, barometer_not_year])

    def process(self, df: pd.DataFrame, verbose: bool) -> pd.DataFrame:
        self.df = df

        frequentation = pd.read_csv('../../../data/raw/voyage/frequentation-gares.csv', sep=';')

        frequentation['Code UIC'] = frequentation['Code UIC'].apply(lambda x: str(int(x))[2:])
        df['period_year'] = df['period'].apply(lambda x: x.split(' ')[1])

        merged = self.merged('2022', 'sept 2022', df, frequentation)
        display(merged.head(5))
        merged = self.merged('2022', 'mars 2022', merged, frequentation)
        merged = self.merged('2021', 'sept 2021', merged, frequentation)
        merged = self.merged('2021', 'mars 2021', merged, frequentation)
        merged = self.merged('2020', 'sept 2020', merged, frequentation)
        merged = self.merged('2019', 'sept 2019', merged, frequentation)
        merged = self.merged('2019', 'mars 2019', merged, frequentation)

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
