from django import forms
from .models import Livre, Membre

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'disponible']

    def clean(self):
        cleaned_data = super().clean()
        titre = cleaned_data.get("titre")
        auteur = cleaned_data.get("auteur")

        if not titre or not auteur:
            raise forms.ValidationError("Les champs Titre et Auteur sont obligatoires")
        return cleaned_data

class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields =  ['name', 'bloque', 'emprunts_actifs']


