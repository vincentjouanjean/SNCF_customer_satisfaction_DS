import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)

from src.visualization.barometer_processed.ProcessBarometer import ProcessBarometer
from src.visualization.barometer_processed.ProcessEquipment import ProcessEquipment
from src.visualization.barometer_processed.ProcessFrequentation import ProcessFrequentation
from src.visualization.barometer_processed.ProcessObj import ProcessObj
from src.visualization.barometer_processed.ProcessObjRest import ProcessObjRest
from src.visualization.barometer_processed.ProcessPiano import ProcessPiano
from src.visualization.barometer_processed.ProcessPointVente import ProcessPointVente
from src.visualization.barometer_processed.ProcessPonctualite import ProcessPonctualite
from src.visualization.barometer_processed.ProcessProprete import ProcessProprete
from src.visualization.barometer_processed.ProcessWifi import ProcessWifi

barometer = pd.read_csv('../../../data/processed/barometer.csv')

processBarometer = ProcessBarometer(True, True)
processEquipment = ProcessEquipment(True, True)
processProprete = ProcessProprete(True, True)
processPiano = ProcessPiano(True, True)
processPointVente = ProcessPointVente(True, True)
processObj = ProcessObj(True, True)
processObjRest = ProcessObjRest(True, True)
processPonctualite = ProcessPonctualite(True, True)
processFrequentation = ProcessFrequentation(True, True)
processWifi = ProcessWifi(True, True)

processBarometer.set_next(processEquipment)
processEquipment.set_next(processProprete)
processProprete.set_next(processPiano)
processPiano.set_next(processPointVente)
processPointVente.set_next(processObj)
processObj.set_next(processObjRest)
processObjRest.set_next(processPonctualite)
processPonctualite.set_next(processFrequentation)
processFrequentation.set_next(processWifi)

df_output = processBarometer.process(barometer)

df_output = df_output.drop(columns=['UIC', 'Date', 'period_year_month', 'period_month', 'period_year'], errors='ignore')
df_output = df_output.drop(columns=['Gare'], errors='ignore')
# df_output = df_output.drop(columns=['Code UIC'], errors='ignore')
# df_output = df_output.drop(columns=['DRG', 'Région (UG)', 'Typologie de la gare', 'Niveau de service'], errors='ignore')
# self.df = self.df.drop('Gare', axis=1)
# self.df = self.df.drop('DRG', axis=1)
# self.df = self.df.drop('Région (UG)', axis=1)
# self.df = self.df.drop('Typologie de la gare', axis=1)
# self.df = self.df.drop('Niveau de service', axis=1)

df_output.to_csv('../../../data/processed/barometer_processed.csv')
