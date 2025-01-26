def menu():
    print("menu")

if __name__ == '__main__':
    menu()

class livre():
    name = ""
    auteur = ""
    dateEmprunt = ""
    disponible = ""
    emprunteur = ""

class dvd():
    name = ""
    realisateur = ""
    dateEmprunt = ""
    disponible = ""
    emprunteur = ""

class cd():
    name = ""
    artiste = ""
    dateEmprunt = ""
    disponible = ""
    emprunteur = ""

class jeuDePlateau :
    name = ""
    createur = ""

class Emprunteur():
    name = ""
    bloque = ""


def menuBibliotheque() :
    print("c'est le menu de l'application des bibliothéquaire")


def menuMembre():
    print("c'est le menu de l'application des membres")
    print("affiche tout")