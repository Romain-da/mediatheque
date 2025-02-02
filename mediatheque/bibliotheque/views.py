from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Livre, DVD, CD, JeuDePlateau, Membre, Emprunt
from .forms import LivreForm, MembreForm, DVDForm, CDForm, JeuDePlateauForm
from django.http import HttpResponse
import json
from django.core.serializers import serialize

# PAGE D'ACCUEIL
def accueil(request):
    return render(request, 'bibliotheque/index.html')

# PAGE ESPACE MEMBRE
def espace_membre(request):
    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    jeux = JeuDePlateau.objects.all()

    print("Livres trouvés :", livres)
    print("DVDs trouvés :", dvds)
    print("CDs trouvés :", cds)
    print("Jeux trouvés :", jeux)

    context = {
        'livres': livres,
        'dvds': dvds,
        'cds': cds,
        'jeux': jeux,
    }
    return render(request, 'bibliotheque/espace_membre.html', context)

# CONNEXION BIBLIOTHÉCAIRE
def login_bibliothecaire(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'bibliotheque/login.html', {'error': 'Identifiants invalides'})
    return render(request, 'bibliotheque/login.html')

# TABLEAU DE BORD
@login_required
def dashboard(request):
    context = {
        'livres': Livre.objects.all(),
        'dvds': DVD.objects.all(),
        'cds': CD.objects.all(),
        'jeux': JeuDePlateau.objects.all(),
        'membres': Membre.objects.all(),
    }
    return render(request, 'bibliotheque/dashboard.html', context)

# GESTION DES MEMBRES
@login_required
def liste_membres(request):
    return render(request, 'bibliotheque/liste_membres.html', {'membres': Membre.objects.all()})

@login_required
def ajouter_membre(request):
    form = MembreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_membres')
    return render(request, 'bibliotheque/ajouter_membre.html', {'form': form})

@login_required
def supprimer_membre(request, membre_id):
    membre = get_object_or_404(Membre, id=membre_id)
    membre.delete()
    return redirect('liste_membres')

# GESTION DES LIVRES
@login_required
def liste_livres(request):
    return render(request, 'bibliotheque/liste_livres.html', {'livres': Livre.objects.all()})

@login_required
def ajouter_livre(request):
    form = LivreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_livres')
    return render(request, 'bibliotheque/ajouter_livre.html', {'form': form})

@login_required
def supprimer_livre(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)
    livre.delete()
    return redirect('liste_livres')

# GESTION DES DVD
@login_required
def liste_dvd(request):
    return render(request, 'bibliotheque/liste_dvd.html', {'dvds': DVD.objects.all()})

@login_required
def ajouter_dvd(request):
    form = DVDForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_dvd')
    return render(request, 'bibliotheque/ajouter_dvd.html', {'form': form})

@login_required
def supprimer_dvd(request, dvd_id):
    dvd = get_object_or_404(DVD, id=dvd_id)
    dvd.delete()
    return redirect('liste_dvd')

# GESTION DES CD
@login_required
def liste_cd(request):
    return render(request, 'bibliotheque/liste_cd.html', {'cds': CD.objects.all()})

@login_required
def ajouter_cd(request):
    form = CDForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_cd')
    return render(request, 'bibliotheque/ajouter_cd.html', {'form': form})

@login_required
def supprimer_cd(request, cd_id):
    cd = get_object_or_404(CD, id=cd_id)
    cd.delete()
    return redirect('liste_cd')

# GESTION DES JEUX DE PLATEAU
@login_required
def liste_jeux(request):
    return render(request, 'bibliotheque/liste_jeux.html', {'jeux': JeuDePlateau.objects.all()})

@login_required
def ajouter_jeu(request):
    form = JeuDePlateauForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_jeux')
    return render(request, 'bibliotheque/ajouter_jeu.html', {'form': form})

@login_required
def supprimer_jeu(request, jeu_id):
    jeu = get_object_or_404(JeuDePlateau, id=jeu_id)
    jeu.delete()
    return redirect('liste_jeux')

# GESTION DES EMPRUNTS
@login_required
def gerer_emprunt(request):
    membres = Membre.objects.all()
    livres = Livre.objects.filter(disponible=True)
    dvds = DVD.objects.filter(disponible=True)
    cds = CD.objects.filter(disponible=True)

    if request.method == "POST":
        membre_id = request.POST.get("membre")
        emprunt_type = request.POST.get("type")
        emprunt_id = request.POST.get("objet")

        if not all([membre_id, emprunt_type, emprunt_id]):
            return render(request, 'bibliotheque/gerer_emprunt.html', {
                'membres': membres,
                'livres': livres,
                'dvds': dvds,
                'cds': cds,
                'error': "Veuillez remplir tous les champs."
            })

        membre = get_object_or_404(Membre, id=membre_id)

        objet_map = {"livre": Livre, "dvd": DVD, "cd": CD}
        objet_class = objet_map.get(emprunt_type)
        if not objet_class:
            return render(request, 'bibliotheque/gerer_emprunt.html', {
                'membres': membres,
                'livres': livres,
                'dvds': dvds,
                'cds': cds,
                'error': "Type d'objet non valide."
            })

        objet = get_object_or_404(objet_class, id=emprunt_id)

        if not objet.disponible:
            return render(request, 'bibliotheque/gerer_emprunt.html', {
                'membres': membres,
                'livres': livres,
                'dvds': dvds,
                'cds': cds,
                'error': f"{objet} est déjà emprunté."
            })

        # Création de l'emprunt
        Emprunt.objects.create(membre=membre, objet=objet, date_emprunt=now())

        # Marquer l'objet comme emprunté
        objet.disponible = False
        objet.save()

        return redirect('dashboard')

    return render(request, 'bibliotheque/gerer_emprunt.html', {
        'membres': membres,
        'livres': livres,
        'dvds': dvds,
        'cds': cds
    })


@login_required
def rendre_emprunt(request, emprunt_id):
    emprunt = get_object_or_404(Emprunt, id=emprunt_id)

    # Mettre à jour l'objet emprunté pour qu'il redevienne disponible
    emprunt.objet.disponible = True
    emprunt.objet.save()

    # Vérifier que le membre a au moins 1 emprunt actif avant de décrémenter
    if emprunt.membre.emprunts_actifs > 0:
        emprunt.membre.emprunts_actifs -= 1
        emprunt.membre.save()

    # Supprimer l'emprunt
    emprunt.delete()

    return redirect('liste_membres')  # Rediriger après suppression