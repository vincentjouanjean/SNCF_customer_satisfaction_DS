import warnings

import numpy as np
import pandas as pd
from IPython.core.display_functions import display
from imblearn.over_sampling import RandomOverSampler
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error, classification_report
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.models.BarometerReport import BarometerReport

warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)


def train_reg_model(model, one_hot_encoder=True, standard_scaler=False, test_size=0.2, data_path='../../data/processed/barometer_processed.csv'):
    barometer_report = BarometerReport()
    barometer = pd.read_csv(data_path, index_col=0)

    barometer = barometer.dropna()
    barometer = barometer.select_dtypes(include='number')

    X = barometer.drop(['_global', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7'], axis=1)
    y = barometer['_global']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=101)

    if one_hot_encoder:
        # Encode categorical features as a one-hot numeric array
        enc = OneHotEncoder(handle_unknown='ignore', sparse=False)
        X_train = enc.fit_transform(X_train)
        X_test = enc.transform(X_test)

    if standard_scaler:
        # Standardize features by removing the mean and scaling to unit variance.
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    model.fit(X_train, y_train)

    barometer_report.score_train = 'score train :' + str(model.score(X_train, y_train))
    barometer_report.score_test = 'score test :' + str(model.score(X_test, y_test))

    if hasattr(model, 'best_score_'):
        barometer_report.best_score = 'best_score_ : ' + str(model.best_score_)
    if hasattr(model, 'best_params_'):
        barometer_report.best_params = 'best_params_ : ' + str(model.best_params_)

    pred_train = model.predict(X_train)
    pred_test = model.predict(X_test)

    barometer_report.rmse_train = 'rmse train :', str(np.sqrt(mean_squared_error(y_train, pred_train)))
    barometer_report.rmse_test = 'rmse test : ', str(np.sqrt(mean_squared_error(y_test, pred_test)))

    if one_hot_encoder:
        X = enc.transform(X)

    barometer_report.cross_validate = pd.DataFrame(cross_validate(model, X, y, return_train_score=True))

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
    ax2.plot(barometer[['pred-real']], label='Ecart')
    ax2.grid(axis='y', alpha=1)

    barometer_report.fig = fig

    return barometer_report


def train_model(model, random_over_sampler=False, categorization_by_deviation=False, data_path='../../data/processed/barometer_processed.csv'):
    barometer_report = BarometerReport()
    barometer = pd.read_csv(data_path, index_col=0)

    barometer = barometer.dropna()

    if not categorization_by_deviation:
        X = barometer.drop(['_global', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7'], axis=1)
        bins = []
        labels = []
        for x in np.arange(50, 90 - 1, 1, dtype=int):
            bins.append(x / 10)
            labels.append(x)

        bins.append(9)
    else:
        bins = [0, 7, 8, 10]
        labels = ['Note basse', 'Note moyenne', 'Note élevée']

    charges_classes = pd.cut(x=barometer['_global'],
                             bins=bins,
                             labels=labels)

    X_train, X_test, y_train, y_test = train_test_split(X, charges_classes, test_size=0.2, random_state=101)

    if random_over_sampler:
        X_train, y_train = RandomOverSampler().fit_resample(X_train, y_train)

    enc = OneHotEncoder(sparse=True, handle_unknown='ignore')

    X_train = enc.fit_transform(X_train)
    X_test = enc.transform(X_test)

    model.fit(X_train, y_train)

    barometer_report.score_train = 'score train :' + str(model.score(X_train, y_train))
    barometer_report.score_test = 'score test :' + str(model.score(X_test, y_test))

    y_pred = model.predict(X_test)

    barometer_report.classification_report = classification_report(y_test, y_pred)

    barometer_report.classification_crosstab = pd.crosstab(y_test, y_pred, rownames=['Classe réelle'], colnames=['Classe prédite'])

    if hasattr(model, 'best_params_'):
        barometer_report.best_params = model.best_params_

    return barometer_report


def display_report(report: BarometerReport):
    display(report.score_train)
    display(report.score_test)
    if report.best_score is not None:
        display(report.best_score)
    if report.best_params is not None:
        display(report.best_params)
    if report.rmse_train is not None:
        display(report.rmse_train)
    if report.rmse_test is not None:
        display(report.rmse_test)
    if report.cross_validate is not None:
        display(report.cross_validate)
    if report.classification_report is not None:
        display(report.classification_report)
    if report.classification_crosstab is not None:
        display(report.classification_crosstab)
    plt.show()
