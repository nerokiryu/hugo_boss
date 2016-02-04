from pygame import *
import pygame
import os
import sys

sys.path.append(os.path.join('menu'))
sys.path.append(os.path.join('jeu'))
sys.path.append(os.path.join('hugo_boss.py'))
font.init()
from math import cos,radians
try: import GetEvent
except: from . import GetEvent


from entity import Entity
from menu import *
from level import *
from plateform import *
from arme import *
from camera import *
from exitBlock import *

class Boss(Entity):
    img_bossf="graphics/character/boss/boss1/boss1r.png"
    coll = False
    inv =0
    hp = 3
    speed = 8
    max_inv=30

    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = x
        self.yvel = y
        self.onGround = False
        self.image = pygame.image.load(self.img_bossf)
        (hauteur, largeur) = self.image.get_size()
        self.rect = Rect(x, y, hauteur, largeur)

    def realease(self):
        self.xvel = self.speed
        self.yvel = self.speed


    def update(self, up, down, left, right, running, platforms, player, arme, screen, height):
        if self.inv > 0:
            self.inv-=1
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100: self.yvel = 100
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False
        # do y-axis collisions
        self.collide(0, self.yvel, platforms)

        self.coll = self.collide(self.xvel, 0, platforms)
        if self.coll:
            self.xvel = -self.xvel
            self.coll = False

        return self.hitbox(0, self.yvel, player, arme, screen)


    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    event.post(event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                    print "collide right"
                    return True
                if xvel < 0:
                    self.rect.left = p.rect.right
                    print "collide left"
                    return True
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    print "collide top"

    def hitbox(self, xvel, yvel, player,arme, screen):

        if sprite.collide_rect(self, player):
            basicfont = font.SysFont(None, 48)
            text = basicfont.render('Game Over', True, (255, 0, 0))
            textrect = text.get_rect()
            textrect.centerx = screen.get_rect().centerx
            textrect.centery = screen.get_rect().centery
            screen.blit(text, textrect)
            display.flip()
            screen.blit
            time.wait(1000)
            return True
        else:
            return False


class Boss2(Entity):
    img_bossf="graphics/character/boss/boss2/boss2r.png"
    coll = False
    inv =0
    hp = 3
    speed = 4
    max_inv=30

    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = x
        self.yvel = y
        self.onGround = False
        self.image = pygame.image.load(self.img_bossf)
        (hauteur, largeur) = self.image.get_size()
        self.rect = Rect(x, y, hauteur, largeur)

    def realease(self):
        self.xvel = self.speed
        self.yvel = self.speed


    def update(self, up, down, left, right, running, platforms, player, arme, screen, height):

        if self.inv > 0:
            self.inv-=1
        if self.onGround :
            self.yvel -= 9
        print(self.rect.top)
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100: self.yvel = 100
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        # increment in y direction
        self.rect.top += self.yvel
        if self.rect.top> height-32:
            self.rect.top=height-96
        # assuming we're in the air
        self.onGround = False

        # do y-axis collisions
        self.collide(0, self.yvel, platforms)

        self.coll = self.collide(self.xvel, 0, platforms)

        if self.coll:
            self.xvel = -self.xvel
            self.yvel = 0
            self.coll = False
        return self.hitbox(0, self.yvel, player, arme, screen)


    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    event.post(event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                    print "collide right"
                    return True
                if xvel < 0:
                    self.rect.left = p.rect.right
                    print "collide left"
                    return True
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    print "collide top"

    def hitbox(self, xvel, yvel, player,arme, screen):

        if sprite.collide_rect(self, player):
            basicfont = font.SysFont(None, 48)
            text = basicfont.render('Game Over', True, (255, 0, 0))
            textrect = text.get_rect()
            textrect.centerx = screen.get_rect().centerx
            textrect.centery = screen.get_rect().centery
            screen.blit(text, textrect)
            display.flip()
            screen.blit
            time.wait(1000)
            return True
        else:
            return False
