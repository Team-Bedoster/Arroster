#coding: utf-8
#A faire : fonction pour lister les bouteilles et allouer un ID [0-127], une bouteille est branchée par cordon, on vérifique qu'elle est branchée par 
#un appel système et si elle est branchée,
#On ajoute une bouteille à la liste des bouteilles courantes.
#Faire une liste de bouteille de bouteilles, la mettre à jour en récupérant les info (humidité,...)
#Fonction qui envoie les paramètres d'arrosage à l'arduino
#Changer les conditions d'arrosage. Utiliser des fonctions d'accès I2C
#	long[] read_i2c_block_data(int addr,char cmd)
#		Block Read transaction.
#	write_i2c_block_data(int addr,char cmd,long vals[])
#		Block Write transaction.


import json
import csv
import smbus
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)


class bouteille:
	def _init_(self, fichier):
		self.dict_test = lecture_fichier('data_conditions.json')
		self.id = attribID()
		while True:
			if scanReseau():
				break
		self.dict_data = lecture_fichier('data_capteurs.json')
	
	def attribID():
	#Fonction permettant d'allouer un ID à une bouteille branchée.
		i = 0
		with open('tabId.csv', r) as csvfile:
			reader = csv.reader(csvfile, delimiter = ',')
			while reader:
				tabId[i] = reader
				i+=1
				
	def lecture_fichier(self.id):
		with open(nom_fichier, "r") as json_data:
			dictionnaire = json.load(json_data)
		return dictionnaire


def scanReseau():
	#Scan les bouteilles présentes sur le réseau et retourne false tant qu'il n'y a pas de nouvelle bouteille
	#retourne l'adresse de la nouvelle bouteille si elle existe
	#les arduino possèdent un fichier contenant leur id, si une bouteille n'a pas ce fichier, c'est la nouvelle bouteille
	
	
	
def writeNumber(value):
#Fonction qui envoie les paramètres d'arrosage à l'arduino.
    #bus.write_byte(address, value)
    bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
#Fonction qui reçois les conditions courantes d'un pot.
    #number = bus.read_byte(address)
    number = bus.read_byte_data(address, 1)
    return number

def testBouteille():
	#Fonction pour lister les bouteilles et allouer un ID [0-127], une bouteille est branchée par cordon, on vérifique qu'elle est branchée par un appel système
	#On ajoute alors une bouteille à la liste des bouteilles courantes.
	

























class DonneesPlantesTest:
    """Classe définissant les paramètres de test fournis par l'utilisateur 
	ainsi que les données courantes des plantes analysées par les capteurs"""
    
    def __init__(self):
        """dict_data représente le dictionnaire de données lus dans le fichier Json,
		écrit par les capteurs, dict_test correcpond aux la valeurs donnée par 
		l'utilisateur, valeur conditionnelle de l'arrosage """
		
        self.dict_data = lecture_data('data_capteurs.json')
		self.dict_test = lecture_conditions('data_conditions.json')

class TestsArrosage:
 """Classe définissant les tests faisables par le programme.
 Permet de savoir si les conditions d'arrosage son remplies ou non
 et le cas échéant, déclencher un arrosage"""
 
	def test_humidite(dict_data, val_donnee):

		if (dict_data>=val_donnee):
			return True
		
		else:
			return False

	def test_temperature(dict_data, val_donnee):

		if (dict_data>=val_donnee):
			return True
		
		else:
			return False

	def test_debordement(dict_data):

		if (dict_data>=val_donnee):
			return True
		
		else:
			return False
		
	def test_luminosite(dict_data, val_donnee):

		if (dict_data>val_donnee):
			return True
		
		else:
			return False

	def test_heure(val_donnee):
	
		maintenant = datetime.now()
		#on fixe la date courante avec l'heure actuelle
		if (val_donnee>=maintenant.hour):
			return True
		
		else:
			return False

	def arrosage():
	#déclenche un arrosage immédiatement
	
	#Alimente la valve pour l'ouvrir et la fermer
	#on doit ouvrir la valve environ 5 secondes (ou autre) puis on referme la valve
	#quand la valve est refermee on relance des tests pour voir si la plante est assez arrosee ou non
	#on suppose que on doit remplir un peu plus que les conditions demandees par l'user
	#exemple il veut que le pot soit arrosee quand humidite<50% -> on arrose jusqu'a 75%
	#on peut supposer que l'user souhaite que l'humidite soit dans un intervalle
	#alors on fixe la limite d'arrosage a 5% pres de la borne superieur de l'intervalle

	def ecriture():
	

	def tests_choisis(dict_test, dict_data):
	"""Identifie les tests choisis par l'user et regarde si les conditions sont remplis pour l'arrosage"""
		tab_test=[2]
		#Ce tableau de booleens sert a garder les retours de fonctions de test en memoire
	
		if(dict_test[] == !None ):
			#l'utilisateur a choisis d'arroser à une certaine heure
			tab_test [0] = test_heure(dict_data[])
			#On verifie si la condition d'heure est validee ou non
			print "je test l'heure"
	
		if(dict_test[] == !None):
			#l'utilisateur a choisis d'arroser en fonction de l'humidité de la terre
			tab_test [1] = test_humidite(dict_data[])
			#On verifie si la condition d'humidite est valide ou non
			print "je test l'humidite"
		
		if(dict_test[] == !None):
			#l'utilisateur a choisis d'arroser en fonction de la température ambiante
			tab_test [2] = test_temperature([dict_data])
			#On verifie si la condition de temperature est validee ou non
			print "je test la temperature"
	
		for(i in tab_test):
		#On parcours le tableau de booleens, si il y a au moins un False, on arrose pas,
		#sinon on arrose
			if (i == False)
				return False
		arrosage()
		print"maintenant nous allons arroser"
			
print "Voici les tests"
premieres_data = DonneesPlantesTest()
#On stocke les donnees des fichiers JSON dans deux dictionnaires differents

tests_choisis(dict_test, dict_data)
#On appelle la fonction de test

print"Tests termines"
