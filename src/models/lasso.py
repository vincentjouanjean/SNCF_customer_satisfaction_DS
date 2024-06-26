import warnings

from sklearn import model_selection
from sklearn.linear_model import Lasso

from src.models.train import train_reg_model

warnings.filterwarnings('ignore')

grid_params = {
    'alpha': [0.1, 1, 5, 10, 30, 50, 100],
    'fit_intercept': [True, False],
    'max_iter': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
    'tol': [1e-4, 1e-3, 1e-2, 1e0, 1e1, 1e2],
    'warm_start': [True, False],
    'positive': [True, False],
    'selection': ['cyclic', 'random'],
}

model = model_selection.GridSearchCV(
    Lasso(),
    grid_params,
    verbose=0,
    n_jobs=-1
)
train_reg_model(model)
