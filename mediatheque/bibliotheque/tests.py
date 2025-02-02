from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from bibliotheque.models import Membre, Livre, DVD, CD, JeuDePlateau, Emprunt

class BibliothequeTestCase(TestCase):

    def setUp(self):
        """Création des objets nécessaires aux tests"""

        # Créer un utilisateur test et le connecter
        self.user = User.objects.create_user(username='testadmin', password='password123')
        self.client.login(username='testadmin', password='password123')

        # Création des objets
        self.membre = Membre.objects.create(name="Jean Dupont", bloque=False, emprunts_actifs=0)

        self.livre = Livre.objects.create(name="Python pour les Nuls", titre="Python pour les Nuls", auteur="John Doe")
        self.dvd = DVD.objects.create(name="Inception", realisateur="Christopher Nolan")
        self.cd = CD.objects.create(name="Thriller", artiste="Michael Jackson")
        self.jeu = JeuDePlateau.objects.create(name="Monopoly", createur="Parker Brothers")

    def test_affichage_livres(self):
        """ Vérifie que la liste des livres s'affiche bien """
        response = self.client.get('/livres/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.livre.titre)

    def test_affichage_dvd(self):
        """ Vérifie que la liste des DVD s'affiche bien """
        response = self.client.get('/dvd/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.dvd.name)

    def test_affichage_cd(self):
        """ Vérifie que la liste des CD s'affiche bien """
        response = self.client.get('/cd/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cd.name)

    def test_emprunt_livre(self):
        """ Vérifie qu'un membre peut emprunter un livre """
        livre_type = ContentType.objects.get_for_model(Livre)
        emprunt = Emprunt.objects.create(membre=self.membre, objet_type=livre_type, objet_id=self.livre.id)

        self.livre.refresh_from_db()
        self.membre.refresh_from_db()

        self.assertEqual(emprunt.membre, self.membre)
        self.assertEqual(emprunt.objet_id, self.livre.id)
        self.assertEqual(emprunt.objet_type, livre_type)

    def test_espace_membre(self):
        """ Vérifie que l'espace membre affiche bien tous les objets """
        response = self.client.get('/espace_membre/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.livre.titre)
        self.assertContains(response, self.dvd.name)
        self.assertContains(response, self.cd.name)
        self.assertContains(response, self.jeu.name)

    def test_rendre_livre(self):
        """ Vérifie qu'un membre peut rendre un livre """
        livre_type = ContentType.objects.get_for_model(Livre)
        emprunt = Emprunt.objects.create(membre=self.membre, objet_type=livre_type, objet_id=self.livre.id)

        # Suppression de l'emprunt (rendu du livre)
        emprunt.delete()

        self.livre.refresh_from_db()
        self.membre.refresh_from_db()

        self.assertEqual(Emprunt.objects.count(), 0)
        self.assertEqual(self.membre.emprunts_actifs, 0)