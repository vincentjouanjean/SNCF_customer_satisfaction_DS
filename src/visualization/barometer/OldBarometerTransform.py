import numpy as np
import pandas as pd

from src.visualization.barometer.BarometerHeaders import BarometerHeaders
from src.visualization.barometer.IBarometerTransform import IBarometerTransform
from src.visualization.barometer.PeriodPromise import PeriodPromise


class OldBarometerTransform(IBarometerTransform):
    # Old structure
    # BSC Sept 2021 contains mars 2019, sept 2019, sept 2020, mars 2021, sept 2021 in different column
    FILE_NAME = '../../data/raw/barometre-client/BSC sept 2021.csv'

    def __init__(self):
        super().__init__(BarometerHeaders(1, 2, 4, 5, 6, 3))
        # Define all periods with column index in sept 2021 file
        self.periods = [
            PeriodPromise('mars 2019', 12, 26, 36, 46, 60, 70, np.nan, np.nan),
            PeriodPromise('sept 2019', 13, 27, 37, 47, 61, 71, np.nan, np.nan),
            PeriodPromise('sept 2020', 15, 29, 39, 49, 63, 73, np.nan, np.nan),
            PeriodPromise('mars 2021', 16, 30, 40, 50, 64, 74, 80, 84),
            PeriodPromise('sept 2021', 17, 31, 41, 51, 65, 75, 81, 85),
        ]

    def transform(self) -> pd.DataFrame:
        for period in self.periods:
            df_period = pd.read_csv(self.FILE_NAME, sep=';', skiprows=2, header=0)
            df_period = self.retrieve_df_with_period(df_period, period)
            self.df_periods.append(df_period)
        self.df_merged = pd.concat(self.df_periods, axis=0)
        return self.df_merged
