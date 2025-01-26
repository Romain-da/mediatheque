from django.db import models

class livre() :
    auteur = models.CharField(max_length=100)

class dvd() :
    realisateur = models.CharField(max_length=100)

class cd() :
    artiste = models.CharField(max_length=100)

class jeuDePlateau() :
    name = models.CharField(max_length=100)
    createur = models.CharField(max_length=100)

class Emprunteur() :
    name = models.CharField(max_length=100)
    bloque = models.BooleanField(default=False)