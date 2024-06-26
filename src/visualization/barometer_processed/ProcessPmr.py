import pandas as pd


class ProcessPmr:
    def __init__(self):
        self.next = None

    def process(self, df: pd.DataFrame, verbose: bool) -> pd.DataFrame:
        self.df = df

        pmr = pd.read_csv('../../../data/raw/pmr/accompagnement-pmr-gares.csv', sep=';')

        pmr['Code UIC'] = pmr['Code UIC'].apply(lambda x: str(int(x))[2:])

        df['period_year'] = df['period'].apply(lambda x: x.split(' ')[1])
        df['period_month'] = df['period'].apply(lambda x: x.split(' ')[0]
                                                .replace('mars', "03")
                                                .replace('mai', "05")
                                                .replace('sept', "09"))
        df['period_year_month'] = df['period_year'] + '-' + df['period_month']

        merged = df.merge(pmr, how='left', left_on=['period_year_month', "Code UIC"],
                          right_on=['Date/Mensuel', 'Code UIC'])

        merged.rename(columns={'Total': 'total_pmr'}, inplace=True)

        if self.next is not None:
            return self.next.process(merged, verbose)
        else:
            return merged
