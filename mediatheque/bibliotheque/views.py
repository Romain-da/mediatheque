from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Livre, DVD, CD, JeuDePlateau, Membre
from .forms import LivreForm, MembreForm

# Page d'accueil
def accueil(request):
    return render(request, 'bibliotheque/index.html')

# Connexion bibliothécaire
def login_bibliothecaire(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'bibliotheque/login.html', {'error': 'Identifiants invalides'})
    return render(request, 'bibliotheque/login.html')

@login_required
def dashboard(request):
    return render(request, 'bibliotheque/dashboard.html')

@login_required
def liste_membres(request):
    if request.method == "POST":
        membres_a_supprimer = request.POST.getlist("membres_selectionnes")
        if membres_a_supprimer:
            Membre.objects.filter(id__in=membres_a_supprimer).delete()
            return redirect('liste_membres')

    membres = Membre.objects.all()
    return render(request, 'bibliotheque/liste_membres.html', {'membres': membres})

@login_required
def ajouter_membre(request):
    if request.method == 'POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = MembreForm()
    return render(request, 'bibliotheque/ajouter_membre.html', {'form': form})

@login_required
def supprimer_membre(request, membre_id):
    membre = get_object_or_404(Membre, id=membre_id)
    membre.delete()
    return redirect('liste_membres')

@login_required
def ajouter_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_livres')
    else:
        form = LivreForm()
    return render(request, 'bibliotheque/ajouter_livre.html', {'form': form})

@login_required
def liste_livres(request):
    if request.method == "POST":
        livres_a_supprimer = request.POST.getlist("livres_selectionnes")
        if livres_a_supprimer:
            Livre.objects.filter(id__in=livres_a_supprimer).delete()
            return redirect('liste_livres')

    livres = Livre.objects.all()
    return render(request, 'bibliotheque/liste_livres.html', {'livres': livres})