from django.urls import path
from . import views

urlpatterns = [
    path('', views.nemu, name='menu'),
    path('bibliotheque/', views.menuBlibliotheque, name='menuBibliotheque'),
    path('membre', views.menuMembre, name='menuMembre'),
]