# paquet.py
import random
from carte import Carte

class Paquet:
	def __init__(self):
		self.cartes = []

	def remplir(self):
		for i in range(13):
			self.cartes.append(Carte(i + 2, "pique"))
			self.cartes.append(Carte(i + 2, "trefle"))
			self.cartes.append(Carte(i + 2, "coeur"))
			self.cartes.append(Carte(i + 2, "carreau"))

	def melanger(self):
		random.shuffle(self.cartes)

	def longueur(self):
		return len(self.cartes)

	def __repr__(self):
		return repr(self.cartes)


	def tirer(self):
		return self.cartes.pop()

	def ajouter(self, nouvelle_carte: Carte):
		self.cartes.append(nouvelle_carte)

	def distribuer(self):
		for i in paquet_plein:
			main_j1.ajouter(paquet_plein.tirer())
	
	

def test_paquet():
	paquet_plein = Paquet()
	paquet_plein.remplir()
	paquet_plein.melanger()
	print(paquet_plein)

	main_j1 = Paquet()
	print(main_j1)
	print(paquet_plein.longueur(), main_j1.longueur())

	

	print(paquet_plein.longueur(), main_j1.longueur())

if __name__ == '__main__':
	test_paquet()