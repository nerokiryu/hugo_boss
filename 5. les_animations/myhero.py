import sys
import pygame 
import os
from mysprite import MySprite
from display import *

# Class MyHero herite de 'MySprite'
class MyHero(MySprite):
	def __init__(self, pos_x, pos_y, image1, image2):
		MySprite.__init__(self, pos_x, pos_y, image1, image2)

	def movement(self, width, height):
		keys = pygame.key.get_pressed()

		# Test la touche pressee
		if keys[pygame.K_LEFT] and self.rect.left > 0:
			self.rect = self.rect.move(-5, 0)
		
		if keys[pygame.K_RIGHT] and self.rect.right < width:
			self.rect = self.rect.move(5, 0)

		if keys[pygame.K_UP] and self.rect.top > 0:
			self.rect = self.rect.move(0, -5)

		if keys[pygame.K_DOWN] and self.rect.bottom < height:
			self.rect = self.rect.move(0, 5)
