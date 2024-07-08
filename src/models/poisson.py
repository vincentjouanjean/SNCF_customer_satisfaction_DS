import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import PoissonRegressor

from src.models.train import train_reg_model, display_report

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

grid_params = {
    'alpha': [0.1, 1, 5, 10, 30, 50, 100],
    'fit_intercept': [True, False],
    'solver': ['lbfgs', 'adam'],
    'max_iter': range(100, 1000, 100),
    'tol': [1e-4, 1e-3, 1e-2, 1e-1],
    'warm_start': [True, False]
}

report = train_reg_model(
    model_selection.GridSearchCV(
        PoissonRegressor(),
        grid_params,
        verbose=0,
        n_jobs=-1
    )
)
display_report(report)
