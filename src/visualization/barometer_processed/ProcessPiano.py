import pandas as pd
from IPython.core.display_functions import display


class ProcessPiano:
    def __init__(self):
        self.next = None

    def process(self, df: pd.DataFrame, verbose: bool) -> pd.DataFrame:
        self.df = df

        # barometer = pd.read_csv('../../../data/processed/barometer_clean.csv', index_col=0)
        piano = pd.read_csv('../../../data/raw/gare/gares-pianos.csv', sep=';')

        piano = piano[piano['UIC'].notna()]
        piano['Code UIC'] = piano['UIC'].apply(lambda x: str(int(x))[2:])

        display(piano.head(5))

        merged = df.merge(piano, how='left', left_on='Code UIC', right_on="Code UIC")

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

    def set_next(self, next_process):
        self.next = next_process
