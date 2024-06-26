import warnings

import numpy as np
import pandas as pd
from sklearn.linear_model import MultiTaskElasticNetCV
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

barometer = pd.read_csv('../../data/processed/barometer_processed.csv', index_col=0)

barometer = barometer.select_dtypes(include='number')

barometer = barometer.dropna()

X = barometer.drop(['_global', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7'], axis=1)
y = barometer[['_global', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7']]
# y = barometer['_global']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

# ----------------------------

model = MultiTaskElasticNetCV(
    cv=8,
    l1_ratio=(0.1, 0.25, 0.5, 0.7, 0.75, 0.8, 0.85, 0.9, 0.99),
    alphas=(0.001, 0.01, 0.02, 0.025, 0.05, 0.1, 0.25, 0.5, 0.8, 1.0)
)

model.fit(X_train, y_train)

enc = OneHotEncoder(handle_unknown='ignore')

X_train = enc.fit_transform(X_train)
X_test = enc.transform(X_test)

print('score train :', model.score(X_train, y_train))
print('score test :', model.score(X_test, y_test))

pred = model.predict(X_train)
pred_test = model.predict(X_test)

print('rmse train :', np.sqrt(mean_squared_error(y_train, pred)))
print('rmse test : ', np.sqrt(mean_squared_error(y_test, pred_test)))
