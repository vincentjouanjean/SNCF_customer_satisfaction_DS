from sklearn import model_selection
from sklearn.linear_model import LinearRegression

from src.models.train import train_reg_model

train_reg_model(model_selection.GridSearchCV(LinearRegression(), param_grid={}))
