from sklearn import model_selection
from sklearn import neighbors

from src.models.train import train_model, display_report

grid_params = {
    'n_neighbors': range(2, 40),
    'weights': ['uniform', 'distance'],
    'algorithm': ['auto'],
    'leaf_size': [5, 10, 20],
    'p': [1, 2],
    'metric': ['euclidean', 'manhattan']
}

model = model_selection.GridSearchCV(
    neighbors.KNeighborsClassifier(),
    grid_params,
    n_jobs=-1,
    verbose=1
)

report = train_model(model)
display_report(report)
