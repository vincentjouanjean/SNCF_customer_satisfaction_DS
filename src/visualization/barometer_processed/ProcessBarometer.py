import numpy as np
import pandas as pd
from IPython.core.display_functions import display

from src.visualization.barometer_processed.IProcess import IProcess


class ProcessBarometer(IProcess):
    def __init__(self, visualize_before, visualize_after):
        super().__init__(visualize_before, visualize_after)

    def change_typology(self, typology, uic):
        output = typology
        if typology in ['1', 'Gare A']:
            gares_loc = self.df.loc[(self.df['Code UIC'] == uic) & -(self.df['Typologie de la gare'] != '1') | (
                    self.df['Typologie de la gare'] != '1')]['Typologie de la gare']
            try:
                output = gares_loc.iloc[0]
            except IndexError:
                output = output
        return output

    def transform(self):
        self.df = self.df.rename(columns={'Agence': 'DRG'})

        # Replacement '24' par 'Gare A - 24'
        self.df['Typologie de la gare'] = self.df['Typologie de la gare'].replace({'24': 'Gare A - 24'})

        # Convert P to float
        for code in ['_global', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7']:
            self.df[code] = self.df[code].replace({'-': np.nan})
            self.df[code] = pd.to_numeric(self.df[code])

        # Supprime les lignes sans code UIC
        self.df = self.df[self.df['Code UIC'].notna()]

        # Supprime les lignes sans note
        self.df = self.df[self.df['_global'].notna()]

        # Convert Code UIC to string
        self.df['Code UIC'] = self.df['Code UIC'].apply(lambda x: str(int(x)))

        self.df['Typologie de la gare'] = self.df.apply(
            lambda x: self.change_typology(x['Typologie de la gare'], x['Code UIC']),
            axis=1)

        # Remplace les P6 et P7 manquant par la moyenne
        self.df['p6'] = self.df['p6'].fillna(round(self.df['p6'].mean(), 2))
        self.df['p7'] = self.df['p7'].fillna(round(self.df['p7'].mean(), 2))

    # def visualize_before_(self):
    #     self
        # # Direction régionnale
        # display(self.df['Agence'].unique())
        #
        # # Unité régionnale
        # display(self.df['Région (UG)'].unique())
        #
        # # Typologie de la gare
        # display(self.df['Typologie de la gare'].unique())
        #
        # for code in ['Agence', 'Région (UG)', 'Typologie de la gare', 'Niveau de service', 'Gare']:
        #     self.df[[code, 'Code UIC']].groupby([code, 'Code UIC']).apply(lambda x: self.print_duplicates(x, code))
        #
        # # 255 na Code UIC
        # display(self.df.isna().sum())
        #
        # # PERIGUEUX n'a pas le bon UIC code
        # display(self.df[self.df[['Code UIC', 'period']].duplicated(keep=False)])

        # display(self.df.info())
        #
        # display(self.df.head(5))
        #
        # display(self.df['Typologie de la gare'].unique())
        #
        # # Min _global = 5.11
        # # Max _global = 8.96
        # # Min des P = 4.36
        # # Max des P = 9.72
        # display(self.df.describe())
        #
        # # 474 null value P6 & P7
        # display(self.df.isna().sum())

    def print_duplicates(self, x, code_):
        if len(x[code_].value_counts()) > 1:
            print(x[code_].value_counts())
