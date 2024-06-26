from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier

from src.models.train import train_model

grid_params = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 30, 40, 50, 70, 90, 120, 150]
}

model = model_selection.GridSearchCV(
    DecisionTreeClassifier(),
    grid_params,
    # scoring='f1_macro',
    verbose=1
)

train_model(model)
