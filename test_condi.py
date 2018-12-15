#coding: utf-8
import json

"""dict_data représente le dictionnaire de données lus dans le fichier Json, écrit par les capteurs
val données correcpond à la valeur donnée par l'utilisateur, valeur conditionnelle de l'arrosage """


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


def lecture_data():
	with open('data_capteurs.json') as json_data:
		data_dict = json.load(json_data)
    return data_dict
	
def lecture_conditions():
	with open('data_conditions.json') as json_data:
		data_dict = json.load(json_data)
    return data_dict

def ecriture():
	

def tests_choisis(dict_test, dict_data):
	
	tab_test=[2]
	#Ce tableau de booleens sert a garder les retours de fonctions de test en memoire
	
	if(dict_test[]==True):
		#l'utilisateur a choisis d'arroser à une certaine heure
		tab_test [0] = test_heure(dict_data[])
		#On verifie si la condition d'heure est validee ou non
		print "je test l'heure"
	
	if(dict_test[]==True):
		#l'utilisateur a choisis d'arroser en fonction de l'humidité de la terre
		tab_test [1] = test_humidite(dict_data[])
		#On verifie si la condition d'humidite est valide ou non
		print "je test l'humidite"
		
	if(dict_test[]==True):
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
dict_data = lecture_data()
dict_test = lecture_conditions()
#On stocke les donnees des fichiers JSON dans deux dictionnaires differents

tests_choisis(dict_test, dict_data)
#On appelle la fonction de test

print"Tests termines"
