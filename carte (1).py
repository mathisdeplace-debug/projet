class Carte:
    def __init__(self, numero: int, signe: str):
        self.__numero = numero
        self.__signe = signe

    def __repr__(self):
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

    def __eq__(self,autre):
        if autre.numero() == self.numero() :
            return True
        else:
            return False

    def __lt__(self,autre):
        if autre.numero() > self.numero() :
            return True
        else:
            return False

    def __gt__(self,autre):
        if autre.numero() < self.numero() :
            return True
        else:
            return False

    def numero(self) -> int:
        return self.__numero

    def signe(self) -> str:
        return self.__signe

        
def test_carte():
    print(Carte(10, "pique") < Carte(14, "trefle"))


if __name__ == '__main__':
    test_carte()