# carte.py
class carte:
	def __init__(self,cartes: str, numero: str, signe: str):
		self.__cartes = cartes
		self.__numero = numero
		self.__signe = signe

	def __repr__(self):
		return f"carte({self.__numero}, {self.__signe})"

	def numero(self) -> int:
		return self.__numero

	def signe(self) -> str:
		self.__signe = ["coeur", "carreau", "pique", "trèfle"]
		return self.__signe

	def cartes(self, signe)->tuple:
		cartes = {}

		for i in self.__signe :
			for i_1 in range(13):
				print(i_1 + 2, " : ", i)
				cartes.append(i_1 + 2, " : ", i                                         )
			
def test_carte():
	print(carte)

if __name__ == '__main__':
	test_carte()


