from sklearn import model_selection
from sklearn import svm

from src.models.train import train_model

grid_params = {
    'C': [0.1, 1, 10, 100, 1000],
    'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
    'kernel': ['rbf']
}

model = model_selection.GridSearchCV(
    svm.SVC(),
    grid_params,
    n_jobs=-1,
    verbose=1
)

train_model(model)
