from sklearn.ensemble import RandomForestClassifier

from src.models.train import train_model, display_report

model = RandomForestClassifier()

report = train_model(model)
display_report(report)
