import sys
import pygame
import os
from mysprite import MySprite
from display import *

# Class MyHero herite de 'MySprite'
class MyHero(MySprite):
	def __init__(self, pos_x, pos_y, image1, image2):
		MySprite.__init__(self, pos_x, pos_y, image1, image2)
		self.rect = pygame.Rect(pos_x, pos_y, 33, 80)

	def movement(self, width, height):
		keys = pygame.key.get_pressed()
		courir = pygame.K_LSHIFT
		mouvement = 10


		# Test la touche pressee pour le mouvement
		if keys[pygame.K_LEFT] and self.rect.left > 0:
			self.rect = self.rect.move(-5, 0)

		if keys[pygame.K_RIGHT] and self.rect.right < width:
			self.rect = self.rect.move(5, 0)

		if keys[pygame.K_UP] and self.rect.top > 0:
			self.rect = self.rect.move(0, -5)

		if keys[pygame.K_DOWN] and self.rect.bottom < height:
			self.rect = self.rect.move(0, 5)


		#Gestion de la touche courir
		if keys[courir] and keys[pygame.K_LEFT] and self.rect.left > 0:
			if self.rect.left < mouvement:
				self.rect = self.rect.move(-self.rect.left, 0)
			else:
				self.rect = self.rect.move(-mouvement, 0)

		if keys[courir] and keys[pygame.K_RIGHT] and self.rect.right < width:
			if self.rect.right > width-mouvement:
				self.rect = self.rect.move(width-self.rect.right, 0)
			else:
				self.rect = self.rect.move(mouvement, 0)

		if keys[courir] and keys[pygame.K_UP] and self.rect.top > 0:
			if self.rect.top < mouvement:
				self.rect = self.rect.move(0, -self.rect.top)
			else:
				self.rect = self.rect.move(0, -mouvement)

		if keys[courir] and keys[pygame.K_DOWN] and self.rect.bottom < height:
			if self.rect.bottom > height-mouvement:
				self.rect = self.rect.move(0, height-self.rect.bottom)
			else:
				self.rect = self.rect.move(0, mouvement)

		#Gestion de la touche attack
		"""if keys[attack] :
			self.rect ="""
