from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import Lasso, LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge, PoissonRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

import streamlit as st
from src.models.train import train_reg_model, train_model

st.set_page_config(
    page_title="Modèles",
    page_icon="⟠"
)

st.header("Baromètre de Satisfaction Clients (BSC)", divider='rainbow')

st.title("Modèles")

st.write("Modèle")
option = st.selectbox(
    "Modèle",
    ("LinearRegression", "Poisson", "Lasso", "Ridge", "KNN", "SVM", "Tree", "Logistic regression", "Voting")
)

st.write("You selected:", option)
if "LinearRegression" == option:
    report = train_reg_model(LinearRegression(), one_hot_encoder=True, standard_scaler=False,
                             data_path='data/processed/barometer_processed.csv')
if "Poisson" == option:
    report = train_reg_model(PoissonRegressor(), one_hot_encoder=True, standard_scaler=False,
                             data_path='data/processed/barometer_processed.csv')
if "Lasso" == option:
    report = train_reg_model(Lasso(), one_hot_encoder=True, standard_scaler=False,
                             data_path='data/processed/barometer_processed.csv')
if "Ridge" == option:
    report = train_reg_model(Ridge(), one_hot_encoder=True, standard_scaler=False,
                             data_path='data/processed/barometer_processed.csv')
if "KNN" == option:
    report = train_model(KNeighborsClassifier(), data_path='data/processed/barometer_processed.csv')
if "SVM" == option:
    report = train_model(SVC(), data_path='data/processed/barometer_processed.csv')
if "Tree" == option:
    report = train_model(DecisionTreeClassifier(), data_path='data/processed/barometer_processed.csv')
if "Logistic regression" == option:
    report = train_model(LogisticRegression(), data_path='data/processed/barometer_processed.csv')
if "Voting" == option:
    clf1 = KNeighborsClassifier(
        algorithm='auto',
        leaf_size=5,
        metric='manhattan',
        n_neighbors=5,
        p=1, weights='distance',
        n_jobs=-1
    )
    clf2 = SVC(
        C=10,
        kernel='rbf',
        gamma=0.1
    )
    clf3 = LogisticRegression(
        C=0.1,
        multi_class='multinomial',
        penalty='l2'
    )
    clf4 = DecisionTreeClassifier(
        criterion='gini',
        max_depth=5
    )

    model = VotingClassifier(
        estimators=[
            ('KNeighborsClassifier', clf1),
            ('SVC', clf2),
            ('LogisticRegression', clf3),
            ('DecisionTreeClassifier', clf4)
        ],
        voting='hard'
    )
    report = train_model(DecisionTreeClassifier(), data_path='data/processed/barometer_processed.csv')

st.write(report.score_train)
st.write(report.score_test)
if report.best_score is not None:
    st.write(report.best_score)
if report.best_params is not None:
    st.write(report.best_params)
if report.rmse_train is not None:
    st.write(report.rmse_train)
if report.rmse_test is not None:
    st.write(report.rmse_test)
if report.cross_validate is not None:
    st.write(report.cross_validate)
if report.classification_report is not None:
    st.write(report.classification_report)
if report.classification_crosstab is not None:
    st.write(report.classification_crosstab)
if report.fig is not None:
    st.pyplot(report.fig)
