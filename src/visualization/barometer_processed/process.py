import pandas as pd

from src.visualization.barometer_processed.ProcessBarometer import ProcessBarometer
from src.visualization.barometer_processed.ProcessEquipment import ProcessEquipment
from src.visualization.barometer_processed.ProcessPiano import ProcessPiano
from src.visualization.barometer_processed.ProcessProprete import ProcessProprete

barometer = pd.read_csv('../../../data/processed/barometer.csv')

processBarometer = ProcessBarometer()
processEquipment = ProcessEquipment()
processProprete = ProcessProprete()
processPiano = ProcessPiano()

processBarometer.set_next(processEquipment)
processEquipment.set_next(processProprete)
processProprete.set_next(processPiano)

#process1.visualize()

step1 = processBarometer.process(barometer, False)

step1.to_csv('../../../data/processed/barometer_processed.csv')


