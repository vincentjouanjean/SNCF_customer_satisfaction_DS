import numpy as np
import pandas as pd
from IPython.core.display_functions import display


class ValueTest:
    def __init__(self, period, station, _global, p1, p2, p3, p4, p5, p6, p7, df):
        self.station = station
        self.period = period
        self._global = _global
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.p7 = p7
        self.df = df

    @staticmethod
    def check(param, expect, line):
        value = float(line[param].to_list()[0])
        if np.isnan(expect):
            return np.isnan(value)
        else:
            return expect == value

    def verify(self):
        # Verify value with one value, global value and other promises values
        line = self.df.loc[(self.df['period'] == self.period) & (self.df['Gare'] == self.station)]
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        if not (
                self.check('_global', self._global, line)
                & self.check('p1', self.p1, line)
                & self.check('p2', self.p2, line)
                & self.check('p3', self.p3, line)
                & self.check('p4', self.p4, line)
                & self.check('p5', self.p5, line)
                & self.check('p6', self.p6, line)
                & self.check('p7', self.p7, line)
        ):
            display(line)
            raise AssertionError("value are different in file")
