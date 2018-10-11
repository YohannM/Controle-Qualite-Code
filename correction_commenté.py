import os
import sys
import math

nb_fichier = 0

for fichier in os.listdir(os.getcwd() + "/../.."):
# os.getcwd() -> répertoire courant
# on concatène une str pour reculer de 2 rép car le répertiore courant est hook 
# lorsque on execute correction.py
# os.listdir() -> liste le contenu du rép en paramètre (en fait une liste)
# fichier parcourt cette liste en prenant le nom de chaque fichier (un str)


	if "java" == fichier.split('.')[-1]:
	# split coupe une str selon un paramètre : ici on sépare la str dès qu'on trouve un point
	# cela nous donne une liste
	# puis on prend la dernière case (indice -1)
	# cad qu"on compare l'extension
		nb_fichier += 1


		with open("../../" + fichier, 'r') as f:
		# with est un context manager : si le code dans le bloc plante 
		# alors le fichier sera quand même fermé (normalement il faut faire fichier.close() mais
		# si erreur et qu'on ferme pas le fichier, cela peut l'endommager et le bloquer)
		# open ouvre le fichier en lecture ('r') et on le renomme f
		# on concatène une str pour reculer car rép courant = hooks

			prog = f.read().split('\n')
			# on lit le fichier avec read() (renvoie une str) 
			# puis on split la str sur la base du '\n'
			# prog est donc une liste qui contient une ligne du programme
			# par case (sous forme de str)
			# on stocke le contenu du fichier dans prog pour la suite


		with open("../../" + fichier, 'w') as f:	
		# ici, on ouvre toujours le même fichier mais en écriture cette fois 
		# Cela efface tout le contenu du fichier, c'est pour ca qu'on l'a d'abord
		# ouvert en lecture pour en récuperer le contenu (stocké dans prog)


			for i, ligne in enumerate(prog):
			# enumerate renvoie un couple : elle place le numero d'index devant chaque case
			# la 1ère valeur est donc (0, première case de prog)
			# on stocke l'index dans i et la case de prog dans ligne 

				try:
					while ligne[-1] == ' ':
						# tant que le dernier caractère est un espace 

						ligne = ligne[:-1]
						# on prend les caractères de ligne depuis l'index 0 (non precisée mais valeur par défaut)
						# jusqu'à la dernière case (non comprise)
						# et on le met dans ligne


				except IndexError:
				# # si on tombe sur une ligne vide, la str sera vide et on aura essayé
				# de lire une case inexistante : cela renvoie un IndexError qu'on intercepte

					pass


				# tous le contenu de la boucle conditionnelle en dessous ne fonctionne pas 
				# encore. Si j'y arrive je vous expliquerai
				
				
				"""
				if len(ligne) > 82:
					
					nbDecoupe = math.ceil((len(ligne) / 80))
					pas = (math.ceil((len(ligne)/ nbDecoupe)))
					print(nbDecoupe)
					print( pas * nbDecoupe)
					lignetemp = ligne 
					del prog[i]
					ligne2 = []
					
					for k in range(nbDecoupe):
						for j in range(pas * k, pas * k+1):
							ligne2.append(ligne[j])
							print(ligne2)
							prog.insert(i + k, ' '.join(ligne2))
					

				
				print(ligne)
				
				"""



				f.write(ligne + "\n")
				# dans le fichier f on écrit la ligne parcourue actuellement 
				# (on a du corriger les erreurs qu'elle contenait)
				# on rajoute un '\n' car on avait split le programme avec pour séparateur 
				# les '\n' : il faut donc les rajouter.