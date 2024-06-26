from sklearn import linear_model
from sklearn import model_selection

from src.models.train import train_model

grid_params = {
    'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
    'penalty': ['none', 'elasticnet', 'l1', 'l2'],
    'C': [0.001, 0.01, 0.1, 1, 10, 100],
    'multi_class': ['ovr', 'multinomial']
}

model = model_selection.GridSearchCV(
    linear_model.LogisticRegression(),
    grid_params,
    n_jobs=-1,
    verbose=1
)

train_model(model)
