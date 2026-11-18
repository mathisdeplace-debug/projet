# paquet.py
import random
from carte import Carte


class Paquet:
    def __init__(self):
        """Crée un paquet vide."""
        self.cartes = []

    def remplir(self):
        """Ajoute les 52 cartes (13 valeurs x 4 signes) au paquet."""
        for i in range(13):
            self.cartes.append(Carte(i + 2, "pique"))
            self.cartes.append(Carte(i + 2, "trefle"))
            self.cartes.append(Carte(i + 2, "coeur"))
            self.cartes.append(Carte(i + 2, "carreau"))

    def melanger(self):
        """Mélange les cartes du paquet aléatoirement """
        random.shuffle(self.cartes)

    def longueur(self):
        """Retourne le nombre de cartes dans le paquet"""
        return len(self.cartes)

    def est_vide(self):
        """Retourne True si le paquet ne contient aucune carte."""
        return self.longueur() == 0

    def __repr__(self):
        return repr(self.cartes)

    def tirer(self):
        """Retire et retourne la dernière carte du paquet."""
        return self.cartes.pop()

    def ajouter(self, nouvelle_carte: Carte):
        """Ajoute une carte à la fin du paquet."""
        self.cartes.append(nouvelle_carte)

    def distribuer(self, main_j1, main_j2):
        """Distribue toutes les cartes une par une aux deux joueurs."""
        while not self.est_vide():
            main_j1.ajouter(self.tirer())
            if not self.est_vide():
                main_j2.ajouter(self.tirer())


def test_paquet():

    paquet_plein = Paquet()
    paquet_plein.remplir()
    paquet_plein.melanger()
    print(paquet_plein)

    main_j1 = Paquet()
    main_j2 = Paquet()
    print(paquet_plein.longueur(), main_j1.longueur(), main_j2.longueur()) 
    print(paquet_plein.est_vide(), main_j1.est_vide())

    paquet_plein.distribuer(main_j1, main_j2)

    print(paquet_plein.longueur(), main_j1.longueur(), main_j2.longueur())
    print(paquet_plein.est_vide())
    print(main_j1)
    print(main_j2)


if __name__ == '__main__':
    test_paquet()