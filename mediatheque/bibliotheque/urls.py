from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import liste_membres, ajouter_membre, supprimer_membre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),
    path('login/', views.login_bibliothecaire, name='login'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('membres/', views.liste_membres, name='liste_membres'),
    path('membres/ajouter/', views.ajouter_membre, name='ajouter_membre'),
    path('livres/ajouter/', views.ajouter_livre, name='ajouter_livre'),
    path('livres/', views.liste_livres, name='liste_livres'),

]
