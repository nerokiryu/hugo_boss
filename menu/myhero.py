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

	speed = 10
	# Stores if player is jumping or not.
	isjump = 0
	# Force (v) up and mass m.
	v = 8
	m = 2

	def __init__(self, pos_x, pos_y, image1, image2):
		MySprite.__init__(self, pos_x, pos_y, image1, image2)
		self.rect = pygame.Rect(pos_x, pos_y, 33, 100)
		self._running = True


	def on_execute(self, width, height):

		keys = pygame.key.get_pressed()

		if (keys[K_LSHIFT]):
			if (self.speed!=10*1.5):
				self.speed=self.speed*1.5
			else:
				self.speed=self.speed
		else:
			self.speed=10

		if (keys[K_RIGHT]):
			self.rect = self.rect.move(self.speed, 0)

		if (keys[K_LEFT]):
			self.rect = self.rect.move(-self.speed, 0)

		if (keys[K_UP]):
		# Calculate force (F). F = 0.5 * mass * velocity^2.
			if self.v > 0:
				F = ( 0.5 * self.m * (self.v*self.v) )
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
