from django.shortcuts import render, get_object_or_404
from .models import Livre, DVD, CD, JeuDePlateau, Membre

def liste_livres(request):
    livres = Livre.objects.all()
    return render(request, 'bibliotheque/liste_livres.html', {'livres': livres})

def liste_membres(request):
    membres= Membre.objects.all()
    return render(request,'bibliotheque/liste_membres.html', {'membres' : membres})

