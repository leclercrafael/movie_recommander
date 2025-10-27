# 🎬 Movie Recommender From Scratch

## 🎯 Aperçu du Projet

Ce projet est la réalisation d'un **système de recommandation de films basé sur le contenu (Content-Based Filtering)**. L'objectif principal est de **recoder manuellement** les fonctions clés des librairies de *Machine Learning* populaires (comme `sklearn`) afin de comprendre les mécanismes fondamentaux qui animent les systèmes de recommandation.

Le jeu de données utilisé est le célèbre **MovieLens 25M** (ou la version small, selon votre choix), et les recommandations sont basées sur la similarité des genres de films.

---

## 🛠️ Concepts Recodés (From Scratch)

Nous avons évité l'utilisation directe des fonctions de haut niveau pour reconstruire les briques de base :

| Concept | Fonction Recodée | Rôle dans le Moteur |
| :--- | :--- | :--- |
| **Vectorisation du texte** | `myCountVectorizer()` | Transforme les genres de films (texte) en vecteurs numériques. |
| **Similitude** | `produit_scalaire()`, `norm()`, `mycosinussimilarity()` | Calcule un score de similarité entre les vecteurs de deux films (méthode de la **Similarité Cosinus**). |
| **Chargement des données** | (En cours / À venir) | Lecture et préparation du fichier CSV sans utiliser `pandas`. |

---

## ⚙️ Structure du Dépôt

Le projet est organisé pour séparer le code réutilisable de l'analyse exploratoire :

* **`recommender_utils.py`** : Contient toutes les fonctions Python pures (`myCountVectorizer`, `mycosinussimilarity`, etc.) développées *from scratch*.
* **`Movie_Recommender.ipynb`** : Le notebook Jupyter principal. Il sert à charger les données, exécuter les fonctions du fichier `recommender_utils.py`, tester les étapes, et présenter les résultats des recommandations.
* **`ml-latest-small/`** : Dossier contenant le jeu de données MovieLens.

