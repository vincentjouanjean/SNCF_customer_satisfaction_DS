from sklearn.linear_model import Ridge
from sklearn.neighbors import KNeighborsClassifier

import streamlit as st
from src.models.train import train_reg_model, train_model

st.set_page_config(
    page_title="Conclusion",
    page_icon="✓"
)

st.header("Baromètre de Satisfaction Clients (BSC)", divider='rainbow')

st.title("Conclusion")

st.write("""
Le modèle de prédiction n'est pas fiable à 100% notamment sur la prédiction des valeurs extrêmes.
L'analyse n'a pas démontré de forte corrélation d'un indicateur spécifique mais nous arrivons à un premier résultat satisfaisant.
Le modèle est entraîné sur 10 indicateurs et pourrait être amélioré en intégrant de nouveaux indicateurs et de nouvelles périodes.
Le meilleur modèle est la régression Ridge et est celui qui est retenu dans ce projet.
""")
