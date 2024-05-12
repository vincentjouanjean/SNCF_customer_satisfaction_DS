from abc import ABC, abstractmethod

import numpy as np
import pandas as pd

from src.visualization.barometer.PeriodPromise import PeriodPromise


class IBarometerTransform(ABC):
    def __init__(self, headers):
        self.df_periods = []
        self.df_merged = []
        self.headers = headers

    @abstractmethod
    def transform(self) -> pd.DataFrame:
        pass

    def retrieve_df_with_period(self, df_period, period: PeriodPromise):
        df_output = pd.DataFrame()

        for col in self.headers.dictionary_headers:
            # Add categorical variable (agency, station, ...)
            df_output[col] = df_period.iloc[:, [self.headers.dictionary_headers[col] - 1]]
        for field in period.fields:
            value = getattr(period, field)
            if value is np.nan:
                df_output[field] = np.nan
            else:
                # Add global, p1, p2, ... values
                df_output[field] = df_period.iloc[:, [value - 1]]
        # Add period to a column
        df_output['period'] = period.title
        return df_output
