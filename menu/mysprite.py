import sys
import pygame
import os
from display import *

class MySprite():
	# Constructeur, self correspond +- au 'this'
    def __init__(self, pos_x, pos_y, image1, image2):
    	# On cree un attribut tableau stockant les 2
    	# images que notre objet pourra prendre
    	self.images = []
        self.images.append(load_image(image1))
        self.images.append(load_image(image2))

        # Correspond a l'indice de l'image courante
        # dans notre tableau images[]
        self.index = 0

        # Initialisation et affectation de l'attribut image
        # avec notre premiere image
        self.image = self.images[self.index]

		# On part du principe que la taille de l'image est 48x48


        # Utilise pour savoir quand changer notre image
        self.timeToUpdate = 0

   	# Retourne le rectangle (position)
    def get_rect(self):
    	return self.rect

    # Retourne la 'surface'
    def get_img(self):
    	return self.image

    # Cette methode parcours notre tableau d'images pour
    # changer l'image affichee de l'objet
    # De plus on utilise un timer pour ne pas changer
    # cette image a chaque iteration de notre boucle de jeu
    def change_img(self):
        if self.timeToUpdate > 2000:
        	# On remet le compteur a 0
        	self.timeToUpdate = 0

        	# on prend la prochaine image du tableau
        	# en verifiant de ne pas depasser sa taille
        	self.index = (self.index + 1) % 2

        	# On change l'image qui va s'afficher
        	self.image = self.images[self.index]

        # On incremente le timer a chaque iteration
        self.timeToUpdate += 100
