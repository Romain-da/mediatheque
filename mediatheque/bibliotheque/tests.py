from django.test import TestCase
from .models import Membre, Livre

class MembreTestCase(TestCase):
    def setUp(self):
        self.membre = Membre.objects.create(name="Test Membre")

    def test_peut_emprunter(self):
        self.assertTrue(self.membre.peut_emprunter())

class LivreTestCase(TestCase):
    def setUp(self):
        self.livre = Livre.objects.create(name="Test Livre", auteur="Auteur Test", disponible=True)

    def test_livre_disponible(self):
        self.assertTrue(self.livre.disponible)
