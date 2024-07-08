from sklearn import model_selection
from sklearn.linear_model import RidgeClassifier

from src.models.train import train_model, display_report

grid_params = {
    'alpha': [0.1, 1, 5, 10, 30, 50, 100],
    'fit_intercept': [True, False],
    'max_iter': [1000],
    'tol': [1e-4, 1e-3, 1e-2, 1e0, 1e1, 1e2],
    'class_weight': ['balanced', 'dict', None],
    'solver': ['auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga', 'lbfgs']
}

model = model_selection.GridSearchCV(RidgeClassifier(), grid_params, verbose=1)

report = train_model(model)
display_report(report)
