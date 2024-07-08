from sklearn.linear_model import LinearRegression

from src.models.train import train_reg_model, display_report

report = train_reg_model(LinearRegression())
display_report(report)
