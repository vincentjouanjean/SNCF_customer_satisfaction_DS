from sklearn.linear_model import ElasticNetCV

from src.models.train import train_reg_model, display_report

model = ElasticNetCV(cv=2, random_state=101)
report = train_reg_model(model)
display_report(report)
