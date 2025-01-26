from django.db import models

class Media(models.Model):
    name = models.CharField(max_length=255)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey('Membre', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True

class Livre(models.Model):
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    def __str__(self):
        return self.titre

class DVD(Media):
    realisateur = models.CharField(max_length=255)

class CD(Media):
    artiste = models.CharField(max_length=255)

class JeuDePlateau(models.Model):
    name = models.CharField(max_length=255)
    createur = models.CharField(max_length=255)

class Membre(models.Model):
    name = models.CharField(max_length=255)
    bloque = models.BooleanField(default=False)
    emprunts_actifs = models.PositiveIntegerField(default=0)

    def peut_emprunter(self):
        return not self.bloque and self.emprunts_actifs < 3