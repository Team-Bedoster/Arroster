#coding: utf-8
#A faire : une bouteille est branchée par cordon
#Le sit informe qu'il y a une nouvelle boutelle et on l'ajoute à la liste des bouteilles courantes dans un CSV.
#Changer les conditions d'arrosage. Utiliser des fonctions d'accès I2C
#	long[] read_i2c_block_data(int addr,char cmd)
#		Block Read transaction.
#	write_i2c_block_data(int addr,char cmd,long vals[])
#		Block Write transaction.
#fonction de convetion binair/hexa

import json
import csv
import smbus
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)


class bouteille:
	def _init_(self, fichier):
		self.dict_test = lecture_fichier(fichier)
		self.id = self.dict.get("id")

		self.dict_data = lecture_fichier('data_capteurs'+self.id+'.json')
	
				
	def lecture_fichier(self.id):
	#le fichier est ecrit par le sit il contien les condition d'arrosage te l'addresse de l'arduino
		with open(nom_fichier, "r") as json_data:
			dictionnaire = json.load(json_data)
		return dictionnaire
	
	
def writeNumber(value, address):
#Fonction qui envoie les paramètres d'arrosage à l'arduino.
    #bus.write_byte(address, value)
    bus.write_byte_data(address, 0, value)
    return -1

def readNumber(address):
#Fonction qui reçois les conditions courantes d'un pot.
    #number = bus.read_byte(address)
    number = bus.read_byte_data(address, 1)
    return number
	
def binairHexa(leBinair):
#fonction de convetion binair a hexadecimal	
	return hex(int(leBinair,2))
	
def decimalHexa(leDecimal):
#fonction de convetion binair a hexadecimal
	return hex(int(leDecimal))























class DonneesPlantesTest:
    """Classe définissant les paramètres de test fournis par l'utilisateur 
	ainsi que les données courantes des plantes analysées par les capteurs"""
    
    def __init__(self):
        """dict_data représente le dictionnaire de données lus dans le fichier Json,
		écrit par les capteurs, dict_test correcpond aux la valeurs donnée par 
		l'utilisateur, valeur conditionnelle de l'arrosage """
		
        self.dict_data = lecture_data('data_capteurs.json')
		self.dict_test = lecture_conditions('data_conditions.json')


	def preparationMessage(dict_test, dict_data):
	"""Identifie les tests choisis par l'user et retourne un message a donner a la fonction write"""
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