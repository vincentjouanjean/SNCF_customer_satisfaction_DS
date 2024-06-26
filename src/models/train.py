import warnings

import numpy as np
import pandas as pd
from IPython.core.display_functions import display
from imblearn.over_sampling import RandomOverSampler, SMOTENC
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn.exceptions import ConvergenceWarning
from sklearn.metrics import mean_squared_error, classification_report, auc, roc_curve
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.preprocessing import OneHotEncoder

warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)


def train_reg_model(model):
    barometer = pd.read_csv('../../data/processed/barometer_processed.csv', index_col=0)

    barometer = barometer.dropna()

    X = barometer.drop(['_global', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7'], axis=1)
    y = barometer['_global']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)
    # scaler = preprocessing.StandardScaler()
    # X_train[X_train.columns] = pd.DataFrame(scaler.fit_transform(X_train), index=X_train.index)
    # X_test[X_test.columns] = pd.DataFrame(scaler.transform(X_test), index=X_test.index)

    # X_train, y_train = RandomOverSampler().fit_resample(X_train, y_train)

    enc = OneHotEncoder(handle_unknown='ignore')

    X_train = enc.fit_transform(X_train)
    X_test = enc.transform(X_test)

    model.fit(X_train, y_train)

    print('score train :', model.score(X_train, y_train))
    print('score test :', model.score(X_test, y_test))

    print('best_score_ : ', model.best_score_)
    print('best_params_ : ', model.best_params_)

    pred_train = model.predict(X_train)
    pred_test = model.predict(X_test)

    print('rmse train :', np.sqrt(mean_squared_error(y_train, pred_train)))
    print('rmse test : ', np.sqrt(mean_squared_error(y_test, pred_test)))

    X = enc.transform(X)

    print(pd.DataFrame(cross_validate(model, X, y, return_train_score=True)))

    pred = model.predict(X)

    barometer['pred'] = pred
    barometer['pred-real'] = barometer['pred'] - barometer['_global']

    fig = plt.figure()
    fig.legend(loc='outside upper right')
    fig.set_size_inches(30, 10)

    ax1 = fig.add_subplot(211)
    ax1.set_title('Comparaison des valeurs réelles et des valeurs prédites', fontsize=22)
    ax1.plot(barometer['_global'], label='Valeur réelle')
    ax1.plot(barometer['pred'], label='Prédiction')
    ax1.grid(axis='y', alpha=1)
    ax1.legend()

    ax2 = fig.add_subplot(212)
    ax2.set_title('Ecart entre la valeur réelle et la prédiction', fontsize=22)
    ax2.plot(barometer[['pred-real']])
    ax2.grid(axis='y', alpha=1)

    plt.show()


def train_model(model):
    barometer = pd.read_csv('../../data/processed/barometer_processed.csv', index_col=0)

    barometer = barometer.dropna()

    X = barometer.drop(['_global', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7'], axis=1)
    bins = []
    labels = []
    for x in np.arange(50, 90 - 1, 1, dtype=int):
        bins.append(x / 10)
        labels.append(x)

    bins.append(9)

    # bins = [0, 7, 8, 10]
    # labels = ['Note basse', 'Note moyenne', 'Note élevée']

    charges_classes = pd.cut(x=barometer['_global'],
                             bins=bins,
                             labels=labels)

    X_train, X_test, y_train, y_test = train_test_split(X, charges_classes, test_size=0.2, random_state=101)

    # X_train, y_train = RandomOverSampler().fit_resample(X_train, y_train)

    enc = OneHotEncoder(sparse=True, handle_unknown='ignore')

    X_train = enc.fit_transform(X_train)
    X_test = enc.transform(X_test)

    model.fit(X_train, y_train)

    print('score train :', model.score(X_train, y_train))
    print('score test :', model.score(X_test, y_test))

    y_pred = model.predict(X_test)

    print(classification_report(y_test, y_pred))

    df = pd.crosstab(y_test, y_pred, rownames=['Classe réelle'], colnames=['Classe prédite'])

    display(df)

    display(model.best_params_)

    plt.show()
