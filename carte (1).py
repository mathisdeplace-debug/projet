class Carte:
    def __init__(self, numero: int, signe: str):
        """Crée une carte avec son numéro (2 à 14) et son signe"""
        self.__numero = numero
        self.__signe = signe

    def __repr__(self):
        """Affiche la carte en texte"""
        numero = self.__numero
        signe = self.__signe

        if numero < 2 or numero > 14:
            return "Erreur sur le numéro de la carte"

        elif numero <= 10:
            return f"{numero} de {signe}"

        elif numero == 11:
            return f"Valet de {signe}"

        elif numero == 12:
            return f"Dame de {signe}"

        elif numero == 13:
            return f"Roi de {signe}"

        elif numero == 14:
            return f"As de {signe}"

    def __eq__(self, autre):
        """Retourne True si les deux cartes ont le même numéro"""
        if autre.numero() == self.numero():
            return True
        else:
            return False

    def __lt__(self, autre):
        """Retourne True si cette carte est plus petite que l'autre"""
        if autre.numero() > self.numero():
            return True
        else:
            return False

    def __gt__(self, autre):
        """Retourne True si cette carte est plus grande que l'autre."""
        if autre.numero() < self.numero():
            return True
        else:
            return False

    def numero(self) -> int:
        """Retourne le numéro de la carte."""
        return self.__numero

    def signe(self) -> str:
        """Retourne le signe de la carte."""
        return self.__signe


def test_carte():
    print(Carte(10, "pique") < Carte(14, "trefle"))


if __name__ == '__main__':
    test_carte()