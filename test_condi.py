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

def arrosage(dict_test):
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
	

def tests_choisis(dict_test):
	
	tab_test=[2]
	if(dict_test[]==True):
		tab_test [0] = test_heure()
		#l'utilisateur a choisis d'arroser à une certaine heure
	
	if(dict_test[]==True):
		tab_test [1] = test_humidite()
		#l'utilisateur a choisis d'arroser en fonction de l'humidité de la terre
			
	if(dict_test[]==True):
		tab_test [2] = test_temperature()
		#l'utilisateur a choisis d'arroser en fonction de la température ambiante
			
			
print "Voici les tests"


