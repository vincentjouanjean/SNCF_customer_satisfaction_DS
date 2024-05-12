import copy

import pandas as pd

from src.visualization.barometer.BarometerHeaders import BarometerHeaders
from src.visualization.barometer.IBarometerTransform import IBarometerTransform
from src.visualization.barometer.PeriodPromise import PeriodPromise


class NewBarometerTransform(IBarometerTransform):
    # New structure
    # BSC mars 2022, sept 2022, mai 2023 contains data in same column index
    FILES__NAME = [
        {
            'title': 'mars 2022',
            'file_name': 'BSC mars 2022.xlsx'
        },
        {
            'title': 'sept 2022',
            'file_name': 'BSC sept 2022.xlsx'
        },
        {
            'title': 'mai 2023',
            'file_name': 'BSC mai 2023.xlsx'
        }
    ]

    def __init__(self):
        super().__init__(BarometerHeaders(6, 7, 8, 9, 10, 11))
        self.period = PeriodPromise('all', 14, 15, 16, 17, 18, 19, 20, 21)

    def transform(self) -> pd.DataFrame:
        for file in self.FILES__NAME:
            df = pd.read_excel('../../data/raw/barometre-client/' + file['file_name'], skiprows=2, header=0)
            period = copy.deepcopy(self.period)
            period.title = file['title']
            df_by_period = self.retrieve_df_with_period(df, period)
            self.df_periods.append(df_by_period)
        return pd.concat(self.df_periods, axis=0)
