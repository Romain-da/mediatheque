Médiathèque - Gestion des Emprunts et des Membres

Ce projet est une application web de gestion de médiathèque développée avec Django. Il permet d'ajouter, de gérer et d'emprunter des livres, CD, DVD et jeux de plateau tout en limitant les emprunts par membre.

- Fonctionnalités

- Gestion des médias : Ajout, suppression et affichage des livres, CD, DVD et jeux de plateau.
- Gestion des membres : Ajout, suppression et suivi des emprunts actifs.
- Gestion des emprunts :

Un membre peut emprunter jusqu'à 3 objets à la fois.

Si un emprunt dépasse une semaine, le membre ne peut plus emprunter jusqu'à la restitution.
- Authentification :

Interface d'administration pour les bibliothécaires.

Espace membre accessible pour consulter la liste des médias.
- Tests unitaires : Vérification du bon fonctionnement des emprunts et de l'affichage des médias.

- Installation

1- Cloner le projet

git clone https://github.com/ton-repo/mediatheque.git
cd mediatheque

2- Créer un environnement virtuel

python -m venv myenv
source myenv/bin/activate  # Sur macOS/Linux
myenv\Scripts\activate  # Sur Windows

3- Installer les dépendances

pip install -r requirements.txt

4- Appliquer les migrations

python manage.py migrate

5- Créer un superutilisateur

python manage.py createsuperuser

6- Lancer le serveur

python manage.py runserver

Accéder à l'application : http://127.0.0.1:8000

- Modèles de base de données

- Modèles principaux

Membre : Représente un utilisateur qui emprunte des objets.

Livre, CD, DVD, JeuDePlateau : Différents types de médias disponibles.

Emprunt : Relie un membre à un objet emprunté.

- Règles d'emprunt

Un membre ne peut avoir que 3 emprunts actifs.

Si un emprunt dépasse 7 jours, le membre ne peut plus emprunter d'autres objets.

- Tests

Des tests unitaires sont inclus pour vérifier les fonctionnalités clés.
Pour exécuter les tests :

python manage.py test bibliotheque

- Contributeurs

 Romain - Développeur principal

- Licence

Ce projet est sous licence MIT. Libre d'utilisation et de modification !
 
Bon développement et bonne gestion de médiathèque ! 🚀

