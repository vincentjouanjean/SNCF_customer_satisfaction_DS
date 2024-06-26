from sklearn.ensemble import RandomForestClassifier

from src.models.train import train_model

model = RandomForestClassifier()

train_model(model)
