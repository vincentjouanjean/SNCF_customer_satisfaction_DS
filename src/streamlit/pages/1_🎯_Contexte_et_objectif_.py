import streamlit as st

st.set_page_config(
    page_title="Contexte et objectif",
    page_icon="🎯"
)

st.header("Baromètre de Satisfaction Clients (BSC)", divider='rainbow')

st.write("""
Le baromètre de satisfaction client en gare est l’outil principal de mesure de la qualité perçue 
de SNCF Gares & Connexions. Les clients sont interrogés en face à face en gare et notent la gare de 
0 à 10 autour des 7 promesses de service :
""")

st.markdown("""
- Promesse 1 : les informations
- Promesse 2 : les déplacements
- Promesse 3 : la propreté et la sûreté
- Promesses 4 : le confort de l'attente
- Promesse 5 : les commerces et les services
- Promesse 6 : l’architecture et les animations
- Promesse 7 : la mobilité durable
""")

st.write("""
Ces mesures sont réalisées dans les 130 plus grandes gares avec une fréquence de 2 vagues annuelles en mars et en septembre.

Objectif :
On souhaite vérifier si les résultats du Baromètre de Satisfaction Clients (BSC) effectué en gare ont un lien avec les indicateurs de production.
Pour cela on cherche à savoir si :
""")

st.write(r'''
$\textsf{
\large Les résultats sont-ils différents entre les vagues ?
}$
''')

st.write(r'''
$\textsf{
\large Y-a-t-il une corrélation entre la satisfaction globale et la réalité des services en gare ?
}$
''')

st.write(r'''
$\textsf{
\large Est-il possible de faire un modèle de prédiction fiable pour prédire la note globale ainsi que les différentes promesses ?
}$
''')

st.subheader("Périmètre")
st.write("""
- Résultat du BSC sur une centaine des plus grandes gares de France
- Utilisation de 2 périodes de BSC pour les années 2019, 2020,2021,2022,2023
- Utilisation d’un ensemble de KPIs disponible à la maille gare en Open Data
""")

st.subheader("Indicateur de production")
st.write("""
- Equipements en gare
- Fréquentation en gares
- Régularité mensuelle TGV globale
- Taux de déclaration de pertes satisfaites
- Taux objets trouvés restitués
- Contrôles de propreté en gare
- Points de vente SNCF
- Accompagnement de personnes à mobilité réduite dans les gares
- Service d’attente
- Service Wifi
""")


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
