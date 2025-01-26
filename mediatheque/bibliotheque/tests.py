from django.test import TestCase
from .models import Emprunteur, livre

class EmprunteurTestCase(TestCase):
    def setUp(self):
        Emprunteur.objects.create(name="John Doe")

    def test_emprunteur_creation(self):
        emprunteur = Emprunteur.objects.get(name="John Doe")
        self.assertEqual(emprunteur.name, "John Doe")
