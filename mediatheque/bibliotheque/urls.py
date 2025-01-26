from django.urls import path
from . import views

urlpatterns = [
    path('livres/', views.liste_livres, name='liste_livres'),
    path('membres/', views.liste_membres, name='liste_membres'),
]