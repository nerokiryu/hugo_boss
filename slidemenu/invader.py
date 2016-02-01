import sys
import pygame 
import os
from mysprite import MySprite
from display import *

# Class Invader herite de 'MySprite'
class Invader(MySprite):
	def __init__(self, pos_x, pos_y, image1, image2, speed):
		MySprite.__init__(self, pos_x, pos_y, image1, image2)
		self.speed = speed

	def movement(self, width, height):
		self.rect = self.rect.move(self.speed)
		# Test la position de ce rectangle pour savoir si il a touche
	    # un mur : les attributs left, right, bottom, top correspondent
	    # au cordonnees en x ou y du carre
		if self.rect.left < 0 or self.rect.right > width:
			self.speed[0] = -self.speed[0]
			self.flip_transfo()

		if self.rect.top < 0 or self.rect.bottom > height:
			self.speed[1] = -self.speed[1]
			self.flip_transfo()

	# On 'flip' l'image courante sans oublier les images
	# stockees qui seront ensuite utilisee
	def flip_transfo(self):
		self.image = pygame.transform.flip(self.image, False, True)
		self.images[0] = pygame.transform.flip(self.images[0], False, True)
		self.images[1] = pygame.transform.flip(self.images[1], False, True)