"""
class : type
objet : instance, élément


int : type, class
str : type, class
float : type, class
list : type, class 



52 : objet de type int 
	objet de class int
	instance de la type int
	instance de la class int
	élément de la type int
	élément de la type int


attribut (propriete) : caractéristique
méthode : fonction (verbe)

	instance_metode <= fonction propre à une instance
	dunder_method <= fonction que l'on va coder pour reproduire certains comportements qu'on les objets natifs de python
	__str__ : print()
	__gt__ : >
	__ge__ : >=
	__lt__ : <
	__le__ : <=
	__eq__ : ==
	__ne__ : !=

	__add__ : +
	__sub__ : -
	__mul__: *
"""

class Voiture:
	def __init__(self, plaque, autonomie, marque, couleur, prix):
		self.plaque = plaque
		self.autonomie = autonomie
		self.marque = marque
		self.couleur = couleur
		self.prix = prix


	def rouler(self, distance):
		if distance > self.autonomie:
			print(f"la voiture immatriculée : {self.plaque} a roulé {self.autonomie} km et est tombée en panne")
			self.autonomie = 0 
		else:
			print(f"la voiture immatriculée : {self.plaque} a roulé {distance} km")
			self.autonomie -= distance


	def evaluation(self):
		return self.autonomie / self.prix

	def __str__(self):
		return f"la voiture immatriculée : {self.plaque}, de couleur {self.couleur} et de marque {self.marque}"

	def __repr__(self):
		return self.plaque

	def __gt__(self, other_voiture):
		return self.evaluation() > other_voiture.evaluation()


ma_voiture = Voiture(plaque="2f1997", autonomie=2500, marque="Vroumvroum", couleur="rouge", prix=4_000_001)
lucas_voiture = Voiture(plaque="Batman", autonomie=4000, marque="Batmobile", couleur="noir mat", prix=3_250_000)
elina_voiture = Voiture(plaque="Joker", autonomie=6000, marque="Bugati", couleur="jaune", prix=4_000_000)


list_de_voitures = [ma_voiture, lucas_voiture, elina_voiture]

# print(max(list_de_voitures))
print(sorted(list_de_voitures, reverse=True))