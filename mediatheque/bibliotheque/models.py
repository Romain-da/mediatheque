from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import now
from datetime import timedelta

# Modèle pour les médias (DVD, CD, Livre)
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
    disponible = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.name = self.titre
        super().save(*args, **kwargs)

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
        """ Vérifie si le membre peut emprunter un nouvel objet. """
        if self.bloque or self.emprunts_actifs >= 3:
            return False

        # Vérifier si un emprunt dépasse une semaine
        emprunts = Emprunt.objects.filter(membre=self)
        for emprunt in emprunts:
            if emprunt.date_emprunt < now() - timedelta(days=7):
                return False  # L'utilisateur a un emprunt en retard

        return True

class Emprunt(models.Model):
    membre = models.ForeignKey('Membre', on_delete=models.CASCADE)
    objet_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=1)  # Ajout d'une valeur par défaut
    objet_id = models.PositiveIntegerField(default=1)  # Ajout d'une valeur par défaut
    objet = GenericForeignKey('objet_type', 'objet_id')
    date_emprunt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.membre.name} - {self.objet}"