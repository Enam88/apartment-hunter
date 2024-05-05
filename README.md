
# Apartment Hunters - Chasseurs d'appart'

## Overview
[FR]
Ce projet vise à prédire les prix des maisons en utilisant des techniques d'apprentissage automatique. Il s'agit d'une solution complète qui comprend le prétraitement des données, l'entraînement du modèle, l'évaluation et le déploiement à l'aide d'une application web Flask dans un conteneur Docker. De plus, le projet propose des visualisations de données interactives avec Power BI.

[EN]
This project aims to predict house prices using machine learning techniques. It is an end-to-end solution that includes data preprocessing, model training, evaluation, and deployment using a Flask web app within a Docker container. Additionally, the project features interactive data visualizations using Power BI.

## Usage

Notebook data cleaning & vizualisations using python:
```
house_price.ipynb
```

To run Flask app locally:

```
pip install -r requirements.txt
python app.py
```
To view PowerBI vizualisations, click on:

```
data_analysis_kc.pbix
```

```
house_pricing.pbix
```

- Docker
```
docker build -t apartmenthunters .
docker run -p 5000:5000 apartmenthunters
```

## Contributors

- Amina SADIO
- Aimen CHERIF
- Enam Akli
