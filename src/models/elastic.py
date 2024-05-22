from sklearn.linear_model import LinearRegression, LassoCV, RidgeCV, ElasticNetCV, MultiTaskElasticNetCV
from sklearn import model_selection, preprocessing
from sklearn.model_selection import cross_val_predict, cross_val_score, cross_validate, train_test_split
from sklearn.metrics import mean_squared_error


import numpy as np
import pandas as pd
from IPython.core.display_functions import display
from matplotlib import pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

barometer = pd.read_csv('../../data/processed/barometer_processed.csv', index_col=0)

# barometer = barometer[
#     ['_global', 'accessibilite_quantity', 'taux_proprete', 'Piano', 'Power&Station', 'Baby-Foot', 'Distr Histoires Courtes',
#      'service_attente_quantity', 'items_found', 'returned_items', 'Régularité composite', 'Ponctualité origine',
#      'Total Voyageurs', 'Total Voyageurs + Non voyageurs', 'Service Wifi',
#
#      'accessibilite_list',
#      'Type de point de vente',
#      'CB', 'Chèque', 'Espèces'
#      ]]

barometer.drop('UIC', axis=1, inplace=True)

barometer = barometer.select_dtypes(include='number')

# display(barometer.corr(numeric_only=True))

display(barometer.isna().sum())

barometer = barometer.dropna()

X = barometer.drop(['_global', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7'], axis=1)
y = barometer[['_global', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)
scaler = preprocessing.StandardScaler()
X_train[X_train.columns] = pd.DataFrame(scaler.fit_transform(X_train), index=X_train.index)
X_test[X_test.columns] = pd.DataFrame(scaler.transform(X_test), index=X_test.index)

# ----------------------------

model_en = MultiTaskElasticNetCV(cv=8, l1_ratio=(0.1, 0.25, 0.5, 0.7, 0.75, 0.8, 0.85, 0.9, 0.99),
                        alphas=(0.001, 0.01, 0.02, 0.025, 0.05, 0.1, 0.25, 0.5, 0.8, 1.0))
model_en.fit(X_train, y_train)

print('score train :', model_en.score(X_train, y_train))
print('score test :', model_en.score(X_test, y_test))

pred = model_en.predict(X_train)
pred_test = model_en.predict(X_test)

print('rmse train :', np.sqrt(mean_squared_error(y_train, pred)))
print('rmse test : ', np.sqrt(mean_squared_error(y_test, pred_test)))

cross_validate(model_en, X, y, return_train_score=True)

# ----------------------------



# sns.heatmap(barometer.corr(numeric_only=True), annot=True, cmap="RdBu_r", center=0)

# plt.show()
