import sys
import pygame
import os
from mysprite import MySprite
from display import *
from pygame.locals import *
import math
from time import sleep
# Class MyHero herite de 'MySprite'




class MyHero(MySprite):
	mouv = False;
#--------------------------------------Initialisation--------------------------------------#
	def __init__(self, pos_x, pos_y, image1, image2, image3): #Initialise MyHero avec une position (x, y), deux images et l'objet lui-meme.
		MySprite.__init__(self, pos_x, pos_y, image1, image2, image3)
		self.rect = pygame.Rect(pos_x, pos_y, 33, 80)

#--------------------------------------Fonctions du mouvement--------------------------------------#
	def movement(self, width, height):
		keys = pygame.key.get_pressed()
		courir = pygame.K_LSHIFT
		mouvement = 10

		#------------------------Fonctions AVANCER----------------------#
		# Test la touche pressee
		if keys[pygame.K_LEFT] and self.rect.left > 0:
			self.rect = self.rect.move(-5, 0)
			self.mouv = True;

		if keys[pygame.K_RIGHT] and self.rect.right < width:
			self.rect = self.rect.move(5, 0)
			self.mouv = True;

		if keys[pygame.K_UP] and self.rect.top > 0:
			self.rect = self.rect.move(0, -5)
			self.mouv = True;

		if keys[pygame.K_DOWN] and self.rect.bottom < height:
			self.rect = self.rect.move(0, 5)
			self.mouv = True;

		if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
			self.mouv = False;

		if (keys[K_LSHIFT]):
			if (self.speed!=10*1.5):
				self.speed=self.speed*1.5
			else:
				self.speed=self.speed
		else:
			self.speed=10

		#-------------------------Fonctions COURRIR-------------------#
		if keys[courir] and keys[pygame.K_LEFT] and self.rect.left > 0:
			self.mouv = True;
			if self.rect.left < mouvement:
				self.rect = self.rect.move(-self.rect.left, 0)
			else:
				self.rect = self.rect.move(-mouvement, 0)

		if keys[courir] and keys[pygame.K_RIGHT] and self.rect.right < width:
			mouv = True;
			if self.rect.right > width-mouvement:
				self.rect = self.rect.move(width-self.rect.right, 0)
			else:
				self.rect = self.rect.move(mouvement, 0)

		if keys[courir] and keys[pygame.K_UP] and self.rect.top > 0:
			mouv = True;
			if self.rect.top < mouvement:
				self.rect = self.rect.move(0, -self.rect.top)
			else:
				self.rect = self.rect.move(0, -mouvement)

		if keys[courir] and keys[pygame.K_DOWN] and self.rect.bottom < height:
			mouv = True;
			if self.rect.bottom > height-mouvement:
				self.rect = self.rect.move(0, height-self.rect.bottom)
			else:
				self.rect = self.rect.move(0, mouvement)
