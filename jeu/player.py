from pygame import *
import pygame
import sys
font.init()
from math import cos,radians
try: import GetEvent
except: from . import GetEvent
import os

sys.path.append(os.path.join('menu'))
sys.path.append(os.path.join('jeu'))
sys.path.append(os.path.join('hugo_boss.py'))

from entity import Entity
from level import *
from plateform import *
from arme import *
from camera import *
from exitBlock import *


img_heror="graphics/character/hero/heror.png"
img_herol="graphics/character/hero/herol.png"

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = x
        self.yvel = y
        self.onGround = False
        self.image = image.load(img_heror)
        (hauteur, largeur) = self.image.get_size()
        self.rect = Rect(x, y, hauteur, largeur)

    def realease(self):
        self.xvel = 8
        self.yvel = 8

    def update(self, up, down, left, right, running, platforms, boss, screen):
        if up:
            # Jump si sur le sol
            if self.onGround: self.yvel -= 9
        if down:
            #Rien ne se passe
            pass
        if running:
            self.xvel = 12
        if left:
            self.xvel = -8
            self.image = image.load(img_herol)
        if right:
            self.xvel = 8
            self.image = image.load(img_heror)
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100: self.yvel = 100
        if not(left or right):
            self.xvel = 0
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.yvel, platforms)

        return self.hitbox(0, self.yvel, boss, screen)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    event.post(event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

    def hitbox(self, xvel, yvel, boss, screen):
        if pygame.sprite.collide_rect(self, boss):
            if boss.inv <= 0:
                return True
            else:
                return False
