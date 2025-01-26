from django.shortcuts import render
from  .models import Emprunteur, livre, dvd, cd, jeuDePlateau

def nemu (request):
    return render(request, 'menu.html')

def menuBibliotheque(request):
    return render(request, 'bibliotheque/menu.html')

def nemuMembre(request):
    return render(request, 'membre/menu.html')