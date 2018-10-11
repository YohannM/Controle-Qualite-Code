import os
import sys
# import de 2 modules


def estRobuste(nom_variable):
	"""Prend en paramètre une str et vérifie sa conformité aux normes
		d'identifiant java"""

	rob = 1  # booléen : par défaut, le mot est robuste

	if nom_variable[0] > 'A' and nom_variable[0] < 'Z':
	# si la première lettre est une majuscule

		print("Ligne", i+1,": la variable", nom, "commence par une majuscule")
		# i fait référence au i qui enumère les cases de la liste prog (enumère les lignes)

		rob = 0
		#dans ce cas le nom n'est pas robuste

	for symb in symb_camel_case:
	# pour tous les éléments de la liste 

		if symb in nom_variable:
			# si un de ces éléments est dans la liste

			print("Ligne", i+1,": la variable", nom,"comporte un caractere de nommage decourage :" ,symb)
			rob = 0

	# on retourne le booléen
	return rob

	
types_java = {"boolean", "byte", "char", "short", "int", "long", "float", "double"}
# liste : définit les types primitifs java

symb_camel_case = {'_', '$'}
# liste : caractères decouragés (camel_case est le nom de la norme de nommage java)

commit_block = 0
# booleen : par défaut on bloque pas le commit


nb_fichier = 0
# nombre de fichier traités


for fichier in os.listdir(os.getcwd()):
# os.getcwd() -> répertoire courant
# os.listdir() -> liste le contenu du rép en paramètre (en fait une liste)
# fichier parcourt cette liste en prenant le nom de chaque fichier (un str)

	if "java" == fichier.split('.')[-1]:
	# split coupe une str selon un paramètre : ici on sépare la str dès qu'on trouve un point
	# cela nous donne une liste
	# puis on prend la dernière case (indice -1)
	# cad qu"on compare l'extension

		print("\nVerification", fichier, ":\n")
		nb_fichier += 1

		with open(fichier, 'r') as f:
		# with est un context manager : si le code dans le bloc plante 
		# alors le fichier sera quand même fermé (normalement il faut faire fichier.close() mais
		# si erreur et qu'on ferme pas le fichier, cela peut l'endommager et le bloquer)
		# open ouvre le fichier en lecture ('r') et on le renomme f

			prog = f.read().split('\n')
			# on lit le fichier avec read() (renvoie une str) 
			# puis on split la str sur la base du '\n'
			# prog est donc une liste qui contient une ligne du programme
			# par case (sous forme de str)

			for i, ligne in enumerate(prog):
			# enumerate renvoie un couple : elle place le numero d'index devant chaque case
			# la 1ère valeur est donc (0, première case de prog)
			# on stocke l'index dans i et la case de prog dans ligne 

				try:
				# sert à executer du code et à envoyer les erreurs 
				# qui peuvent survenir dans le bloc except qui suivra


					if ligne[-1] == ' ':
					# on essaye de lire la dernière case de la ligne
					# pour détecter un espace inutile
						print("La ligne", i+1, "comporte un/des espaces inutiles en fin de ligne.")
						commit_block = 1
						# on bloque le commit
				except IndexError:
				# si on tombe sur une ligne vide, la str sera vide et on aura essayé
				# de lire une case inexistante : cela renvoie un IndexError qu'on intercepte
					continue
					# pas de traitements particulier


				if len(ligne) > 82:
				# len() renvoie la taille d'une str (marche pour liste)
					print("La ligne", i+1, "fait plus de 80 caracteres :", len(ligne), "caracteres.")
					commit_block = 1

				if ligne[-1] == ';':
				# dernier caractère de ligne 
				# on vérifie qu'on a bien affaire à une instruction 

					if ligne.find(';') != len(ligne) - 1:
					# si le premier ';' trouvé est à un index différent que le dernier caractère
					# à noter qu'on ne gère pas les cas de ';' dans une String ou un sysout par ex
					# trop compliqué et pas le temps 
						print("La ligne", i+1, "comporte plusieurs instructions.")
						commit_block = 1

				for mot in types_java:
				# mot contiendra les str de la liste types_java à tour de role 
					if mot in ligne:
					# si un de ces mots est dans la ligne
						j = 0

						while ligne[ligne.find(mot) + len(mot) + j] == ' ':
						# find renvoie l'index de la première occurence de mot dans ligne
						# on ajoute la taille du mot + j qui vaut 0 au début
						# en gros on va chercher le prochain caractère autre qu'un ' '
							j += 1

						
						if ligne[ligne.find(mot) + len(mot)  + j] != ')':  # cast détecté
						# si ce prochain caractère est un ')' : alors on a détecté un cast
						# de la forme : (int) nombre;
						# ou bien : (int   ) nombre;


							if ligne[ligne.find(mot) + len(mot)] == ' ' or ligne[ligne.find(mot) + len(mot)] == '[':
							# on va chercher le caractère juste après le mot clé :
							# si c'est pas un espace ou un '[' alors on a affaire a un mot dans un String
							# exemple : System.out.prINT("coucou");
							# par contre on accepte :
							# int i = 5;
							# ou bien : int[] tab = new int[5];

								# à partir de là, on essaye de récupérer le nom de la variable

								nom = ""
								# on initialise le nom à une str vide 

								k = ligne.find(mot) + len(mot) + j
								# k vaut l'index du prochain caractère autre que ' ' (voir précédemment)

								tabBool = 0
								# expliqué juste après 

								try:
									passe = 0
									# expliqué juste après

									while (ligne[k] != ' ' or tabBool) and ligne[k] != '=' and ligne[k] != ';' and ligne[k] != '(' and ligne[k] != ',' and ligne[k] != ')':
										# si le caractère étudié est un espace on sort sauf si tabBool est à 1
										# en effet, tabBool à 1 signifie qu'on a détecté une syntaxe type tableau
										# exemple : int[][] tab = {1,2};
										# dans l'exemple on veut pas s'arrêter ni à '[' ni à ']' car on veut récuperer 'tab'
										# 
										# par contre on s'arrête dès qu'on trouve :
										# ';' : on est arrivé à une fin de déclaration (ex: "int i;")
										# '=' : on arrive à une affectation (ex: "int i= 0;")
										# '(' : on a trouvé un nom de méthode (ex: "public int getPrix()")
										# ',' : on a trouvé un nom d'argument de méthode ("ex : public void getPrix(int nomProd, ...)")
										# ')' : on a trouvé un nom d'argument de méthode ("ex : public void getPrix(int nomProd)")

										# Mais dans la plupart des cas, la boucle s'arrête car elle détecte un espace.
										# exemple : int i ;
										# int i = 0;


										if ligne[k] != '[' and ligne[k] != ']' and ligne[k] != ' ':
										# si on détecte autre chose qu'un ' ' ou qu'un '[' ou ']'
											nom += ligne[k]
											# on ajoute le caractère au nom
											tabBool = 0
											# et on met tabBool à zero (si jamais il était à 1 de l'itération d'avant)

										elif ligne[k] != ' ':
										# si il détecte un des trois caractères et que ce n'est pas un espace
										# alors c'est '[' ou ']' et on a détecté un tableau (tabBool à 1)
											tabBool = 1

										# on augmente l'index
										k += 1

								except IndexError:
								# une erreur peut survenir dans certains cas particuliers, exemple : 
								# System.out.print.ln("J'adore manipuler des int
								#					et faire des phrases sur 2 lignes")
								# Dans ce cas on va esayer de lire un caractère inexistant dans la str ligne
								
									passe = 1
									# dans ce cas la str nom est vide ou contient une valeur chelou en fct des cas
									# on utilise donc passe pour pouvoir passer juste après même si la fct est robuste 
									# renvoie peut être faux
									
								# print("id detecte", nom)

								if not estRobuste(nom) or passe:
								# on teste le nommage 
								# si pas bon on bloque le commit 
								# à moins qu'il y ait eu une erreur au dessus 

									commit_block = 1
				
				
								
									
if commit_block:
# si le cmmit a été bloqué

	print("\nVos programmes java ne remplissent pas les conditions de qualite du code.\n")
	print("Vous pouvez lancer le programme python 'correction.py' \ndans le dossier .git/hooks pour une correction automatique.\n")
	
	# on sort du script python on mettant la valeur 1 dans la varaible d'envt ERRORLEVEL
	sys.exit(1)
else:
	# Autrement on ne fait rien et ERRORLEVEL est à 0 
	print(nb_fichier, "verifies. Aucun defaut de qualite.")

