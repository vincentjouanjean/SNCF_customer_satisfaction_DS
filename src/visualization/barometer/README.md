# Baromètre de satisfaction

Il existe 2 formats de baromètre de satisfaction, l'ancien format XLSX qui n'est pas exploitable en l'état, il est nécessaire de faire la conversion vers un fichier CSV.

## L'ancien format

Le fichier `BSC sept 2021.csv` contient l'ensemble des données de mars 2019, septembre 2019, septembre 2020, mars 2021 et septembre 2021 dans des colonnes différentes.

Le chargement du fichier dans un Data Frame est difficilement exploitable, les entêtes de colonne possèdent le même nom (P1.1, P1.2, etc.).
C'est pourquoi un ojet `PeriodPromise` est construit indiquant l'indice des colonnes concernant la période, exemple :
```PeriodPromise('mars 2019', 12, 26, 36, 46, 60, 70, np.nan, np.nan)```
Pour la période de mars 2019, la récupération de la note globale se fait sur la 12ème colonne, et les critères P1 à P5, respectivement sur les indices 26, 36, 46, 60 et 70.

## Le nouveau format

La lecture du nouveau format est bien plus pratique sur la récupération des données, le fichier XLSX est directement exploitable et l'emplacement des colonnes est la même pour tous les fichiers.
Une boucle de lecture sur chaque fichier est réalisée avec l'aide de la même structure de l'ancien format.

## Process

Le fichier Process permet de lancer le script et de concaténer l'ensemble des données dans un fichier de sortir vers `data/processed`.
