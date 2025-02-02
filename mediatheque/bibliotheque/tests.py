from bibliotheque.models import Emprunt, Membre, Livre

# Vérifier un membre et un livre
membre = Membre.objects.first()
livre = Livre.objects.filter(disponible=True).first()

if membre and livre:
    emprunt = Emprunt.objects.create(membre=membre, objet=livre)
    livre.disponible = False
    livre.save()
    print(f"✅ {membre.name} a emprunté {livre.titre}")

# Vérifier si l'emprunt est bien enregistré
print("📌 Liste des emprunts :", Emprunt.objects.all())