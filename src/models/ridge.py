import warnings

import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import Ridge

from src.models.train import train_reg_model

warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

grid_params = {
    'alpha': [0.1, 1, 5, 10, 30, 50, 100],
    # 'fit_intercept': [True, False],
    # 'max_iter': [1000],
    # 'tol': [1e-4, 1e-3, 1e-2, 1e0, 1e1, 1e2],
    # 'solver': ['auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga', 'lbfgs']
}

model = model_selection.GridSearchCV(
    Ridge(),
    grid_params,
    verbose=0,
    n_jobs=-1
)

train_reg_model(model)
