from django.contrib import admin
from .models import Livre, DVD, CD, JeuDePlateau, Membre

admin.site.register(Livre)
admin.site.register(DVD)
admin.site.register(CD)
admin.site.register(JeuDePlateau)
admin.site.register(Membre)
