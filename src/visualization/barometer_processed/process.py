import pandas as pd

from src.visualization.barometer_processed.ProcessBarometer import ProcessBarometer
from src.visualization.barometer_processed.ProcessFrequentation import ProcessFrequentation
from src.visualization.barometer_processed.ProcessEquipment import ProcessEquipment
from src.visualization.barometer_processed.ProcessObj import ProcessObj
from src.visualization.barometer_processed.ProcessObjRest import ProcessObjRest
from src.visualization.barometer_processed.ProcessPiano import ProcessPiano
from src.visualization.barometer_processed.ProcessPointVente import ProcessPointVente
from src.visualization.barometer_processed.ProcessPonctualite import ProcessPonctualite
from src.visualization.barometer_processed.ProcessProprete import ProcessProprete
from src.visualization.barometer_processed.ProcessWifi import ProcessWifi

barometer = pd.read_csv('../../../data/processed/barometer.csv')

processBarometer = ProcessBarometer()
processEquipment = ProcessEquipment()
processProprete = ProcessProprete()
processPiano = ProcessPiano()
processPointVente = ProcessPointVente()
processObj = ProcessObj()
processObjRest = ProcessObjRest()
processPonctualite = ProcessPonctualite()
processFrequentation = ProcessFrequentation()
processWifi = ProcessWifi()

processBarometer.set_next(processEquipment)
processEquipment.set_next(processProprete)
processProprete.set_next(processPiano)
processPiano.set_next(processPointVente)
processPointVente.set_next(processObj)
processObj.set_next(processObjRest)
processObjRest.set_next(processPonctualite)
processPonctualite.set_next(processFrequentation)
processFrequentation.set_next(processWifi)

step1 = processBarometer.process(barometer, False)

step1.to_csv('../../../data/processed/barometer_processed.csv')


