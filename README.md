Project Name
==============================

This repo is a Starting Pack for DS projects. You can rearrange the structure to make it fits your project.

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               <- Should be in your computer but not on Github (only in .gitignore)
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's name, and a short `-` delimited description, e.g.
    │                         `1.0-alban-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, links, and all other explanatory materials.
    │
    ├── reports            <- The reports that you'll make during this project as PDF
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   ├── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   │   └── visualize.py

--------

# Retrieve Data

Copy Open SNCF data to `./data/raw` - https://data.sncf.com/pages/accueil/

- data/raw/barometre-client/BSC sept 2021.csv : https://data.sncf.com/explore/dataset/barometre-client/information/ (convert it to csv)
- data/raw/barometre-client/BSC mars 2022.xlsx : https://data.sncf.com/explore/dataset/barometre-client/information/
- data/raw/barometre-client/BSC sept 2022.xlsx : https://data.sncf.com/explore/dataset/barometre-client/information/
- data/raw/barometre-client/BSC mai 2023.xlsx : https://data.sncf.com/explore/dataset/barometre-client/information/
- data/raw/equipement/equipements-accessibilite-en-gares.csv : https://data.sncf.com/explore/dataset/equipements-accessibilite-en-gares/information/
- data/raw/proprete/proprete-en-gare.csv : https://data.sncf.com/explore/dataset/proprete-en-gare/information/
- data/raw/gare/gares-pianos.csv : https://data.sncf.com/explore/dataset/gares-pianos/information/
- data/raw/horaire/points-vente.csv : https://data.sncf.com/explore/dataset/points-vente/information/
- data/raw/obj/objets-trouves-gares.csv : https://data.sncf.com/explore/dataset/objets-trouves-gares/information/
- data/raw/obj/objets-trouves-restitution.csv : https://data.sncf.com/explore/dataset/objets-trouves-restitution/information/
- data/raw/ponctualite/reglarite-mensuelle-tgv-nationale.csv : https://data.sncf.com/explore/dataset/reglarite-mensuelle-tgv-nationale/information/
- data/raw/voyage/frequentation-gares.csv : https://data.sncf.com/explore/dataset/frequence-gare/information/
- data/raw/voyage/gares-equipees-du-wifi.csv : https://data.sncf.com/explore/dataset/gares-equipees-du-wifi/information/

# Process - concatenation barometers

```
cd .
python src/visualization/barometer/process.py
```

# Process - integration of indicators

```
cd .
python src/visualization/barometer_processed/process.py
```

# Run Streamlit

```
cd .
python -m streamlit run src/streamlit/0_🚄_Projet.py
```

# 

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
