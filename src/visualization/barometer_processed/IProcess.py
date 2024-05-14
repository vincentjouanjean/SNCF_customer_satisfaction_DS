from abc import ABC, abstractmethod

import numpy as np
import pandas as pd

from src.visualization.barometer.PeriodPromise import PeriodPromise


class IProcess(ABC):
    def __init__(self, headers):
        self.df_periods = []
        self.df_merged = []
        self.headers = headers

    @abstractmethod
    def process(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def visualize(self):
        pass
