# Projet Final – Réduction de Dimension & Conteneurisation Docker

## Objectif du Projet

Ce projet a pour objectif de simuler un workflow collaboratif en Data Science en utilisant :

- Git & GitHub (travail par branches)
- Des méthodes de réduction de dimension (PCA et t-SNE)
- Une évaluation quantitative via la métrique de *trustworthiness*
- La conteneurisation avec Docker pour assurer la reproductibilité

Chaque membre du binôme a développé une méthode dans une branche dédiée avant fusion dans la branche `main`.  
Le projet final permet d’évaluer automatiquement les méthodes via un conteneur Docker.

---

# Description du Dataset

Dataset : **City Lifestyle Segmentation Dataset**

- 300 villes synthétiques
- 10 variables numériques
- Données économiques, environnementales et sociales

Exemples de variables :

- Densité de population  
- Revenu moyen  
- Taux de pénétration Internet  
- Indice de qualité de l’air  
- Score de transport public  
- Score de bonheur  
- Ratio d’espaces verts  

Les données ont été générées avec des corrélations réalistes afin de former naturellement plusieurs groupes de villes.

---

# Méthodes Implémentées

## 1️- PCA (Analyse en Composantes Principales)

- Méthode linéaire
- Maximisation de la variance expliquée
- Méthode déterministe

## 2️- t-SNE (t-distributed Stochastic Neighbor Embedding)

- Méthode non-linéaire
- Préservation des voisinages locaux
- Adaptée à la visualisation de clusters

---

# Métriques d’Évaluation

## Trustworthiness

La trustworthiness mesure la capacité d’une réduction de dimension à préserver les relations de voisinage locales.

- Valeur comprise entre 0 et 1
- Plus la valeur est proche de 1, meilleure est la préservation

## Erreur de Reconstruction (PCA uniquement)

Mesure la perte d’information après réduction puis reconstruction inverse.

Plus la valeur est faible, meilleure est la conservation de l’information.

---

# Exécution avec Docker

## Construire l’image Docker

```bash
docker build -t city-project .
