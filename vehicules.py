class Voiture:
    counter = 0
    def __init__(self, modele, marque, vitesse_max,km):
        self.modele = modele
        self.marque = marque
        self.vitesse_max = vitesse_max
        self.km = km

Voiture.counter +=1 
voiture1 = Voiture('class A', 'Mercedes', '240','450000')
voiture2 = Voiture('class A', 'Mercedes', '240','450000')
voiture3 = Voiture('class A', 'Mercedes', '240','450000')



class Bateau:
    counter = 0
    def __init__(self, modele, marque, vitesse_max,km):
        self.modele = modele
        self.marque = marque
        self.vitesse_max = vitesse_max
        self.km = km
bateau = Bateau('class A', 'Clio', '240','450000')
Bateau.counter +=1 

class Moto:
    counter = 0
    def __init__(self, modele, marque, vitesse_max, km):
        self.modele = modele
        self.marque = marque
        self.vitesse_max = vitesse_max
        self.km = km
moto = Moto('class A', 'Mercedes', '240','450000')
Moto.counter +=1 

class Avion:
    counter = 0
    def __init__(self, modele, marque, vitesse_max,km):
        self.modele = modele
        self.marque = marque
        self.vitesse_max = vitesse_max
        self.km = km
avion = Avion('class A', 'Mercedes', '240','450000')
Avion.counter +=1 
