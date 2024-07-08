import pandas as pd

import streamlit as st

st.set_page_config(
    page_title="Exploration des données",
    page_icon="🗃️"
)

st.header("Baromètre de Satisfaction Clients (BSC)", divider='rainbow')

st.title("Exploration des données")

barometer_brut = pd.read_csv('data/processed/barometer.csv', index_col=0)
barometer = pd.read_csv('data/processed/barometer_processed.csv', index_col=0)

st.subheader("1. Concaténation des fichiers dans un même DataFrame en ne gardant que les colonnes suivantes :")
st.table(barometer_brut.columns.values.tolist())

st.subheader("2. Nettoyage du DataFrame :")

st.markdown("""
- Normaliser la colonne "Typologie de la gare"
- Convertion des notes des promesses en valeur numérique
- Suppression des lignes sans code UIC ou note global (correspond à des lignes de sous-total)
- Remplacement des notes P6 et P7 absentes par la moyenne (les notes P6 et P7 ont été introduites en 2022)
""")

st.subheader("3. Intégration des équipements : ")

st.table(barometer.iloc[0:5, 14:25])

st.subheader("4. Intégration du taux de propreté : ")

st.table(barometer.iloc[0:5, 25:26])

st.subheader("5. Service d’attente : ")

st.table(barometer.iloc[0:5, 26:31])

st.subheader("6. Points de vente SNCF : ")

st.table(barometer.iloc[0:5, 31:38])

st.subheader("7. Objets trouvés/récupérés : ")

st.table(barometer.iloc[0:5, 38:40])

st.subheader("8. Régularité mensuelle TGV globale : ")

st.table(barometer.iloc[0:5, 40:42])

st.subheader("8. Fréquentation : ")

st.table(barometer.iloc[0:5, 42:44])

st.subheader("8. Service Wifi en gare : ")

st.table(barometer.iloc[0:5, 44:45])

st.subheader("Affichage des premières lignes du DataFrame : ")
st.dataframe(barometer.head(10))
st.write("Dimention du DataFrame: ", barometer.shape)

st.subheader("Affichage de la description des différentes notes : ")
st.dataframe(barometer[['_global', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7']].describe())

st.subheader("Netoyage du DataFrame : ")
st.dataframe(barometer_brut.isna().sum())

st.dataframe(barometer.isna().sum())

st.markdown(
    '''
    <style>
    .block-container {
        width: 80%;
        max-width: 80%;
    }
    .element-container {
        margin-top: 15px;
    }
    ul {
        list-style-position: inside;
        margin: 0px;
    }
    </style>
    ''', unsafe_allow_html=True
)
