from django import forms
from .models import Livre, Membre, DVD, CD, JeuDePlateau

# 📌 Formulaire pour les Livres
class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur']  # `name` est géré automatiquement

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.name = instance.titre  # Remplit `name` avec `titre`
        if commit:
            instance.save()
        return instance

# 📌 Formulaire pour les Membres
class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields =  ['name', 'bloque', 'emprunts_actifs']

# 📌 Formulaire pour les DVD
class DVDForm(forms.ModelForm):
    class Meta:
        model = DVD
        fields = ['name', 'realisateur', 'disponible']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        realisateur = cleaned_data.get("realisateur")

        if not name or not realisateur:
            raise forms.ValidationError("Les champs Nom et Réalisateur sont obligatoires")
        return cleaned_data

# 📌 Formulaire pour les CD
class CDForm(forms.ModelForm):
    class Meta:
        model = CD
        fields = ['name', 'artiste', 'disponible']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        artiste = cleaned_data.get("artiste")

        if not name or not artiste:
            raise forms.ValidationError("Les champs Nom et Artiste sont obligatoires")
        return cleaned_data

# 📌 Formulaire pour les Jeux de Plateau
class JeuDePlateauForm(forms.ModelForm):
    class Meta:
        model = JeuDePlateau
        fields = ['name', 'createur']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        createur = cleaned_data.get("createur")

        if not name or not createur:
            raise forms.ValidationError("Les champs Nom et Créateur sont obligatoires")
        return cleaned_data


