import pandas as pd
from sklearn.linear_model import RidgeClassifier

from src.models.train import train_model, display_report

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

report = train_model(RidgeClassifier())
display_report(report)
