from abc import ABC, abstractmethod

import pandas as pd
from IPython.core.display_functions import display


class IProcess(ABC):
    def __init__(self, visualize_before=False, visualize_after=False):
        self.next = None
        self.is_visualize_before = visualize_before
        self.is_visualize_after = visualize_after
        self.df_input = None
        self.df = None

    @abstractmethod
    def transform(self) -> pd.DataFrame:
        pass

    def visualize_before(self):
        display(self.df.shape)

    def visualize_after(self):
        display(self.df.shape)
        for col in self.df.columns:
            if (self.df[col].isna() > 0).sum() > 0:
                display(col)
                display(self.df[col].isna().sum())

    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        self.df_input = df
        self.df = df
        if self.is_visualize_before:
            self.visualize_before()
        self.transform()
        if self.is_visualize_after:
            self.visualize_after()
        return self.next_process()

    def next_process(self):
        if self.next is not None:
            return self.next.process(self.df)
        else:
            return self.df

    def set_next(self, next_process):
        self.next = next_process
