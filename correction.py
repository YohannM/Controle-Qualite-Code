import os
import sys
import math

nb_fichier = 0

for fichier in os.listdir(os.getcwd() + "/../.."):

	if "java" == fichier.split('.')[-1]:
		nb_fichier += 1

		with open("../../" + fichier, 'r') as f:
			prog = f.read().split('\n')


		with open("../../" + fichier, 'w') as f:

			for i, ligne in enumerate(prog):
				
				try:
					while ligne[-1] == ' ':
						ligne = ligne[:-1]


				except IndexError:
					pass

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