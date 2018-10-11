import os
import sys


def estRobuste(nom_variable):
	"""Prend en paramètre une str et vérifie sa conformité aux normes
		d'identifiant java"""

	rob = 1 

	if nom_variable[0] > 'A' and nom_variable[0] < 'Z':
		print("Ligne", i+1,": la variable", nom, "commence par une majuscule")
		rob = 0

	for symb in symb_camel_case:

		if symb in nom_variable:
			print("Ligne", i+1,": la variable", nom,"comporte un caractere de nommage decourage :" ,symb)
			rob = 0

	return rob

	
types_java = {"boolean", "byte", "char", "short", "int", "long", "float", "double"}

symb_camel_case = {'_', '$','@'}

commit_block = 0

nb_fichier = 0



for fichier in os.listdir(os.getcwd()):

	if "java" == fichier.split('.')[-1]:

		print("\nVerification", fichier, ":\n")
		nb_fichier += 1

		with open(fichier, 'r') as f:

			prog = f.read().split('\n')

			for i, ligne in enumerate(prog):

				try:
					if ligne[-1] == ' ':
						print("La ligne", i+1, "comporte un/des espaces inutiles en fin de ligne.")
						commit_block = 1
				except IndexError:
					continue


				if len(ligne) > 82:
					print("La ligne", i+1, "fait plus de 80 caracteres :", len(ligne), "caracteres.")
					commit_block = 1

				if ligne[-1] == ';':

					if ligne.find(';') != len(ligne) - 1:
						print("La ligne", i+1, "comporte plusieurs instructions.")
						commit_block = 1

				for mot in types_java:
					if mot in ligne:
						j = 0

						while ligne[ligne.find(mot) + len(mot) + j] == ' ':
							j += 1
						
						if ligne[ligne.find(mot) + len(mot)  + j] != ')':  


							if ligne[ligne.find(mot) + len(mot)] == ' ' or ligne[ligne.find(mot) + len(mot)] == '[':

								nom = ""

								k = ligne.find(mot) + len(mot) + j

								tabBool = 0

								try:
									passe = 0

									while (ligne[k] != ' ' or tabBool) and ligne[k] != '=' and ligne[k] != ';' and ligne[k] != '(' and ligne[k] != ',' and ligne[k] != ')':

										if ligne[k] != '[' and ligne[k] != ']' and ligne[k] != ' ':
											nom += ligne[k]
											tabBool = 0

										elif ligne[k] != ' ':
											tabBool = 1

										k += 1

								except IndexError:
									passe = 1

								if not estRobuste(nom) or passe:
									commit_block = 1
				
				
								
									
if commit_block:

	print("\nVos programmes java ne remplissent pas les conditions de qualite du code.\n")
	print("Vous pouvez lancer le programme python 'correction.py' \ndans le dossier .git/hooks pour une correction automatique.\n")
	
	sys.exit(1)
else:
	print(nb_fichier, "verifies. Aucun defaut de qualite.")

