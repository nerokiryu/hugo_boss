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

		if keys[pygame.K_RIGHT] and self.rect.right < width:
			self.rect = self.rect.move(5, 0)

		if (keys[K_LSHIFT]):
			if (self.speed!=10*1.5):
				self.speed=self.speed*1.5
			else:
				self.speed=self.speed
		else:
			self.speed=10

		if (keys[K_RIGHT]):
			self.rect = self.rect.move(self.speed, 0)

		#-------------------------Fonctions COURRIR-------------------#
		if keys[courir] and keys[pygame.K_LEFT] and self.rect.left > 0:
			if self.rect.left < mouvement:
				self.rect = self.rect.move(-self.rect.left, 0)
			else:
				F = -( 0.5 * self.m * (self.v*self.v) )

			# Change position
			self.rect = self.rect.move(0, -F)

			# Change velocity
			self.v = self.v - 1

			# If ground is reached, reset variables.
			if  self.rect.bottom <= width:
				self.rect.bottom = width
				self.isjump = 0
				self.v = 8

				pygame.display.flip()
				sleep(0.03)
