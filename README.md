🎬 Movie Recommender From Scratch
🎯 Aperçu du Projet
Ce projet est la réalisation d'un système de recommandation de films basé sur le contenu (Content-Based Filtering). L'objectif principal est de recoder manuellement les fonctions clés des librairies de Machine Learning populaires (comme sklearn) afin de comprendre les mécanismes fondamentaux qui animent les systèmes de recommandation.

Le jeu de données utilisé est le célèbre MovieLens 25M (ou la version small, selon votre choix), et les recommandations sont basées sur la similarité des genres de films.

🛠️ Concepts Recodés (From Scratch)
Nous avons évité l'utilisation directe des fonctions de haut niveau pour reconstruire les briques de base :

Concept	Fonction Recodée	Rôle dans le Moteur
Vectorisation du texte	myCountVectorizer()	Transforme les genres de films (texte) en vecteurs numériques.
Similitude	produit_scalaire(), norm(), mycosinussimilarity()	Calcule un score de similarité entre les vecteurs de deux films (méthode de la Similarité Cosinus).
Chargement des données	(En cours / À venir)	Lecture et préparation du fichier CSV sans utiliser pandas.
⚙️ Structure du Dépôt
Le projet est organisé pour séparer le code réutilisable de l'analyse exploratoire :

recommender_utils.py : Contient toutes les fonctions Python pures (myCountVectorizer, mycosinussimilarity, etc.) développées from scratch.

Movie_Recommender.ipynb : Le notebook Jupyter principal. Il sert à charger les données, exécuter les fonctions du fichier recommender_utils.py, tester les étapes, et présenter les résultats des recommandations.

ml-latest-small/ : Dossier contenant le jeu de données MovieLens.

🚀 Comment Lancer le Projet
Prérequis

Assurez-vous d'avoir Python 3.x installé, ainsi que les librairies suivantes (principalement pour l'environnement Jupyter et l'affichage/test des données) :

Bash
pip install jupyter numpy pandas
Étapes

Cloner le dépôt :

Bash
git clone https://github.com/votre_nom_utilisateur/nom_du_repo.git
cd nom_du_repo
Télécharger les données : Téléchargez le jeu de données MovieLens 25M (ou small) et placez le fichier movies.csv dans un dossier approprié (par exemple, dans le dossier ml-latest-small/).

Exécuter le Notebook : Lancez Jupyter et ouvrez le notebook :

Bash
jupyter notebook
# Ouvrez 'Movie_Recommender.ipynb'
Le notebook vous guidera à travers chaque étape du processus, du chargement des données au calcul de la matrice de similarité.

🤝 Contribution
Ce projet est un travail d'apprentissage et d'implémentation manuelle. Les suggestions d'amélioration des fonctions from scratch (optimisation, gestion des cas limites, etc.) sont les bienvenues. N'hésitez pas à ouvrir une issue ou soumettre une Pull Request.

👨‍💻 Auteur
[Votre Nom] - Étudiant/Développeur Passionné de ML
