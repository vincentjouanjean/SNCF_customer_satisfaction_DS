import pandas as pd

from src.visualization.barometer_processed.IProcess import IProcess


class ProcessFrequentation(IProcess):
    def __init__(self, visualize_before, visualize_after):
        super().__init__(visualize_before, visualize_after)

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

        merged_tmp['Total Voyageurs'] = merged_tmp['Total Voyageurs'].fillna(merged_tmp['Total Voyageurs'].mean())
        merged_tmp['Total Voyageurs + Non voyageurs'] = merged_tmp['Total Voyageurs + Non voyageurs'].fillna(
            merged_tmp['Total Voyageurs + Non voyageurs'].mean())
        return pd.concat([merged_tmp, barometer_not_year])

    def transform(self):
        frequentation = pd.read_csv('../../../data/raw/voyage/frequentation-gares.csv', sep=';')

        frequentation['Code UIC'] = frequentation['Code UIC'].apply(lambda x: str(int(x))[2:])
        self.df['period_year'] = self.df['period'].apply(lambda x: x.split(' ')[1])

        merged = self.merged('2022', 'sept 2022', self.df, frequentation)
        merged = self.merged('2022', 'mars 2022', merged, frequentation)
        merged = self.merged('2021', 'sept 2021', merged, frequentation)
        merged = self.merged('2021', 'mars 2021', merged, frequentation)
        merged = self.merged('2020', 'sept 2020', merged, frequentation)
        merged = self.merged('2019', 'sept 2019', merged, frequentation)
        merged = self.merged('2019', 'mars 2019', merged, frequentation)

        self.df = merged

        self.df['Total Voyageurs'].fillna(round(self.df['Total Voyageurs'].mean(), 0), inplace=True)
        self.df['Total Voyageurs + Non voyageurs'].fillna(round(self.df['Total Voyageurs + Non voyageurs'].mean(), 0),
                                                          inplace=True)
