import pandas as pd

import streamlit as st

st.set_page_config(
    page_title="Exploration des données",
    page_icon="📈"
)

st.header("Baromètre de Satisfaction Clients (BSC)", divider='rainbow')

st.title("Visualisation des données")

barometer_brut = pd.read_csv('data/processed/barometer.csv', index_col=0)
barometer = pd.read_csv('data/processed/barometer_processed.csv', index_col=0)

st.subheader("1. Satisfaction globale par direction régionale")

st.image('src/streamlit/img/1.png')

st.subheader("2. Niveau de satisfaction sur les différentes périodes")

st.image('src/streamlit/img/2.png', width=600)

st.subheader("3. La distribution des différentes promesses ainsi que la satisfaction globale")

st.image('src/streamlit/img/3.png')

st.subheader("4. Evolution des Notes de la satisfaction selon les différentes périodes analysées")

st.image('src/streamlit/img/4.png')

st.subheader("5. Taux de propreté dans les gares")

st.image('src/streamlit/img/5.png')

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
