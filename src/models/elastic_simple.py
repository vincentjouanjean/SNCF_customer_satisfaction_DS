import warnings

import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNetCV
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

barometer = pd.read_csv('../../data/processed/barometer_processed.csv', index_col=0)

barometer = barometer.select_dtypes(include='number')

barometer = barometer.dropna()

X = barometer.drop(['_global', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7'], axis=1)
y = barometer['_global']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

# ----------------------------

model = ElasticNetCV(cv=5, random_state=101)

model.fit(X_train, y_train)

print('score train :', model.score(X_train, y_train))
print('score test :', model.score(X_test, y_test))

pred = model.predict(X_train)
pred_test = model.predict(X_test)

print('rmse train :', np.sqrt(mean_squared_error(y_train, pred)))
print('rmse test : ', np.sqrt(mean_squared_error(y_test, pred_test)))

# print(pd.DataFrame(cross_validate(model, X, y, return_train_score=True)))

# ----------------------------


# sns.heatmap(barometer.corr(numeric_only=True), annot=True, cmap="RdBu_r", center=0)

# plt.show()
