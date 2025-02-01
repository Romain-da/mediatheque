from django.db import models
from django.contrib.auth.models import User

# Modèle abstrait pour les médias (DVD, CD, Livre)
class Media(models.Model):
    name = models.CharField(max_length=255)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey('Membre', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True

class DVD(Media):
    realisateur = models.CharField(max_length=255)

class CD(Media):
    artiste = models.CharField(max_length=255)

class Livre(Media):  # Livre doit être une classe séparée
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)

    def __str__(self):
        return self.titre

class JeuDePlateau(models.Model):
    name = models.CharField(max_length=255)
    createur = models.CharField(max_length=255)

class Membre(models.Model):
    name = models.CharField(max_length=255)
    bloque = models.BooleanField(default=False)
    emprunts_actifs = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def peut_emprunter(self):
        return not self.bloque and self.emprunts_actifs < 3

class Emprunt(models.Model):  # Emprunt doit être une classe séparée
    membre = models.ForeignKey('Membre', on_delete=models.CASCADE, related_name='emprunts')
    livre = models.ForeignKey('Livre', on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour = models.DateField(null=True, blank=True)  # Null si le livre n'a pas été rendu

    def est_en_cours(self):
        return self.date_retour is None

    def __str__(self):
        return f"{self.membre.name} - {self.livre.titre}"