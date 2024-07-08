import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV

from src.models.train import train_reg_model, display_report

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=3)]
# Number of features to consider at every split
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 100, num=3)]
max_depth.append(None)
max_features = ['auto', 'sqrt']
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]  # Create the random grid
random_grid = {
    # 'n_estimators': [2000],
    'n_estimators': n_estimators,
    # 'max_features': max_features,
    'max_depth': max_depth,
    # 'max_depth': [100],
    'min_samples_split': min_samples_split,
    'min_samples_leaf': min_samples_leaf,
    'bootstrap': bootstrap
}

model = RandomizedSearchCV(
    estimator=RandomForestRegressor(),
    param_distributions=random_grid,
    n_iter=100,
    verbose=2,
    random_state=42,
    n_jobs=-1,
    error_score='raise'
)

report = train_reg_model(RandomForestRegressor())
display_report(report)
