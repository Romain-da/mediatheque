"""
URL configuration for mediatheque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from bibliotheque import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),
    path('login/', views.login_bibliothecaire, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='accueil'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('espace_membre/', views.espace_membre, name='espace_membre'),
    path('membres/', views.liste_membres, name='liste_membres'),
    path('membres/ajouter/', views.ajouter_membre, name='ajouter_membre'),
    path('membres/supprimer/<int:membre_id>/', views.supprimer_membre, name='supprimer_membre'),
    path('membres/modifier/<int:membre_id>/', views.modifier_membre, name='modifier_membre'),

    path('livres/ajouter/', views.ajouter_livre, name='ajouter_livre'),
    path('livres/', views.liste_livres, name='liste_livres'),
    path('livres/supprimer/<int:livre_id>/', views.supprimer_livre, name='supprimer_livre'),

    path('dvd/', views.liste_dvd, name='liste_dvd'),
    path('dvd/ajouter/', views.ajouter_dvd, name='ajouter_dvd'),
    path('dvd/supprimer/<int:dvd_id>/', views.supprimer_dvd, name='supprimer_dvd'),

    path('cd/', views.liste_cd, name='liste_cd'),
    path('cd/ajouter/', views.ajouter_cd, name='ajouter_cd'),
    path('cd/supprimer/<int:cd_id>/', views.supprimer_cd, name='supprimer_cd'),

    path('jeux/', views.liste_jeux, name='liste_jeux'),
    path('jeux/ajouter/', views.ajouter_jeu, name='ajouter_jeu'),
    path('jeux/supprimer/<int:jeu_id>/', views.supprimer_jeu, name='supprimer_jeu'),

    path('emprunts/', views.gerer_emprunt, name='gerer_emprunt'),
    path('emprunts/rendre/<int:emprunt_id>/', views.rendre_emprunt, name='rendre_emprunt'),
    path('emprunts/rendre/<int:emprunt_id>/', views.rendre_emprunt, name='rendre_emprunt'),
    ]
