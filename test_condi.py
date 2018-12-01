#coding: utf-8
import json

"""dict_data représente le dictionnaire de données lus dans le fichier Json, écrit par les capteurs
val données correcpond à la valeur donnée par l'utilisateur, valeur conditionnelle de l'arrosage """


def test_humidite(dict_data, val_donnee):
	if (dict_data>=val_donnee):
		return True
	else:
		return False

def test_temperature(dict_data):
	if (dict_data>=val_donnee):
		return True
	else:
		return False

def test_debordement(dict_data):
	if (dict_data>=val_donnee):
		return True
	else:
		return False

def test_heure(val_donnee):
	#on fixe la date courante avec l'heure actuelle
	maintenant = datetime.now()
	if (val_donnee>=maintenant.hour):
		return True
	else:
		return False

def mode_arro(dict_test):
	#on définit si l'utilisateur souhaite arroser avec un test conditionnel ou non(alors
	#arrosage périodique)
	

def type_arro(dict_test):
	#on définit si l'utilisateur souhaite arroser un volume ou pendant une durée

def arrosage(dict_test):
	#déclenche un arrosage immédiatement


def lecture_data():
	with open('data_capteurs.json') as json_data:
		data_dict = json.load(json_data)
    return data_dict
	
def lecture_condition():
	with open('data_conditions.json') as json_data:
		data_dict = json.load(json_data)
    return data_dict

def ecriture():
	

def tests_choisis(dict_test):
	if mode_arro(dict_test)==1:
	#l'utilisateur a choisis l'arrosage conditionnel
		tab_test=[2]
		if(dict_test[]==True):
			tab_test [0] = test_heure()
		if(dict_test[]==True):
			tab_test [1] = test_humidite()
		if(dict_test[]==True):
			tab_test [2] = test_temperature()
		if(dict_test[]==True):
			
		if(dict_test[]==True):
	else:
	#l'utilisateur a choisis l'arrosage périodique
		
		
	


print "Voici les tests"


