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

class Stats():
    def __init__(self, fichier, pv, vitesse):
        self.img_bossf = fichier
        self.coll = False
        self.inv = 0
        self.hp = pv
        self.speed = vitesse
        self.max_inv = 120

class Boss1(Entity, Stats):
    def __init__(self, x, y):
        Entity.__init__(self)
        Stats.__init__(self, "graphics/character/boss/boss1/boss1r.png", 3, 8)
        self.xvel = x
        self.yvel = y
        self.onGround = False
        self.image = pygame.image.load(self.img_bossf)
        (hauteur, largeur) = self.image.get_size()
        self.rect = Rect(x, y, hauteur, largeur)

    def realease(self):
        self.xvel = self.speed
        self.yvel = self.speed

    def update(self, up, down, left, right, running, platforms, player, arme, screen,width,height, entities):
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
                    return True
                if xvel < 0:
                    self.rect.left = p.rect.right
                    return True
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

    def hitbox(self, xvel, yvel, player,arme, screen):
        if sprite.collide_rect(self, player):
            if self.inv <= 0:
                return True
        else:
            return False

class Boss2(Entity, Stats):
    T1 = True
    T2 = True
    def __init__(self, x, y, img):
        Entity.__init__(self)
        Stats.__init__(self, "graphics/character/boss/boss4/boss_P" + str(img) + "_ecr0.png", 9, 3)
        self.xvel = x
        self.yvel = y
        self.onGround = False
        self.image = pygame.image.load(self.img_bossf)
        (hauteur, largeur) = self.image.get_size()
        self.rect = Rect(x, y, hauteur, largeur)

    def realease(self):
        self.xvel = self.speed
        self.yvel = self.speed

    def update(self, up, down, left, right, running, platforms, player, arme, screen,width, height, entities):
        if self.T1 and self.hp == 6:
            self.img_bossf = "graphics/character/boss/boss4/boss_P2_ecr0.png"
            self.image = pygame.image.load(self.img_bossf)
            (hauteur, largeur) = self.image.get_size()
            self.rect = Rect(self.rect.left, self.rect.top, hauteur, largeur)
            self.xvel = self.xvel*2
            self.T1 = False

        if self.T2 and self.hp == 3:
            self.img_bossf = "graphics/character/boss/boss4/boss_P3_ecr0.png"
            self.image = pygame.image.load(self.img_bossf)
            (hauteur, largeur) = self.image.get_size()
            self.rect = Rect(self.rect.left, self.rect.top, hauteur, largeur)
            self.xvel = self.xvel*1.5
            self.T2 = False

        if self.inv > 0:
            self.inv-=1
        if self.onGround :
            if self.rect.right < width-64 and self.rect.left > 64:
                self.yvel -= 9
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
                    return True
                if xvel < 0:
                    self.rect.left = p.rect.right
                    return True
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

    def hitbox(self, xvel, yvel, player,arme, screen):
        if sprite.collide_rect(self, player):
            if self.inv <= 0:
                return True
        else:
            return False

class Boss3(Entity, Stats):
    dec =False
    dec_speed=16

    def __init__(self, x, y):
        Entity.__init__(self)
        Stats.__init__(self, "graphics/character/boss/boss5/spider.png", 6, 6)
        self.xvel = x
        self.yvel = 0
        self.onGround = False
        self.image = pygame.image.load(self.img_bossf)
        (hauteur, largeur) = self.image.get_size()
        self.rect = Rect(x, 32, hauteur, largeur)

    def realease(self):
        self.xvel = self.speed
        self.yvel = 0

    def update(self, up, down, left, right, running, platforms, player, arme, screen,width,height, entities):

        if self.inv > 0:
            self.inv-=1
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        if not self.dec:
            if self.rect.left <= player.rect.left and self.rect.right >= player.rect.right:
                self.yvel=self.dec_speed
                self.speed=self.xvel
                self.xvel=0
                self.dec=True
            """if player.xvel > 0 and self.xvel>0:
                if self.rect.left == player.rect.left:
                    self.yvel=self.dec_speed
                    self.dec=True
            elif player.xvel > 0 and self.xvel<0:
                if self.rect.left+50 == player.rect.left:
                    self.yvel=self.dec_speed
                    self.dec=True
            elif player.xvel < 0 and self.xvel<0:
                if self.rect.right == player.rect.right:
                    self.yvel=self.dec_speed
                    self.dec=True
            elif player.xvel < 0 and self.xvel>0:
                if self.rect.right+50 == player.rect.right:
                    self.yvel=self.dec_speed
                    self.dec=True"""
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        if self.rect.bottom >= player.rect.bottom and self.dec:
            self.yvel=-self.dec_speed/2
        if self.rect.top ==32 and self.dec:
            self.yvel=0
            self.dec=False
            self.xvel=self.speed
        if self.rect.left<=32 or self.rect.right>=width-32:
            self.xvel = -self.xvel
        return self.hitbox(0, self.yvel, player, arme, screen)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    event.post(event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                    return True
                if xvel < 0:
                    self.rect.left = p.rect.right
                    return True
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

    def hitbox(self, xvel, yvel, player,arme, screen):
        if sprite.collide_rect(self, player):
            if self.inv <= 0:
                return True
        else:
            return False

class Boss4(Entity, Stats):
    delay=0
    delay_max=100
    tir=0
    res=False

    def __init__(self, x, y):
        Entity.__init__(self)
        Stats.__init__(self, "graphics/character/boss/boss3/boss_eye.png", 6, 5)
        self.xvel = x
        self.yvel = y
        self.onGround = False
        self.image = pygame.image.load(self.img_bossf)
        (hauteur, largeur) = self.image.get_size()
        self.rect = Rect(x, y, hauteur, largeur)

    def realease(self):
        self.xvel = self.speed
        self.yvel = self.speed

    def update(self, up, down, left, right, running, platforms, player, arme, screen,width,height, entities):
        if self.inv > 0:
            self.inv-=1
        """if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100: self.yvel = 100"""
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        #self.onGround = False
        # do y-axis collisions

        if self.delay<=0:
            if isinstance(self.tir, Tir):
                self.tir.image = pygame.image.load(self.tir.img_bossf).convert()
                self.tir.image.set_alpha(0)
            self.tir = Tir(self.rect.right-((self.rect.right-self.rect.left)/2),self.rect.bottom-((self.rect.bottom-self.rect.top)/2))
            self.tir.realease(randint(-4,4),randint(-4,4))
            entities.add(self.tir)
            self.delay=self.delay_max
        else:
            self.delay-=0.5
            self.res = self.tir.update(up, down, left, right, running, platforms, player, arme, screen,width,height,entities)


        if self.rect.top <=32 or self.rect.bottom >= height-32:
            self.yvel = -self.yvel

        if self.rect.left<=32 or self.rect.right>=width-32:
            self.xvel = -self.xvel

        return self.hitbox(0, self.yvel, player, arme, screen) or self.res

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    event.post(event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                    return True
                if xvel < 0:
                    self.rect.left = p.rect.right
                    return True
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                    return True
                if yvel < 0:
                    self.rect.top = p.rect.bottom

    def hitbox(self, xvel, yvel, player,arme, screen):
        if sprite.collide_rect(self, player):
            if self.inv <= 0:
                return True
        else:
            return False

class Tir(Entity):
    img_bossf="graphics/bullet.gif"
    coll = False
    inv =0
    hp = 6
    max_inv=30

    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = x
        self.yvel = y
        self.onGround = False
        self.image = pygame.image.load(self.img_bossf)
        (hauteur, largeur) = self.image.get_size()
        self.rect = Rect(x, y, hauteur, largeur)

    def realease(self,x,y):
        self.xvel = x
        self.yvel = y

    def update(self, up, down, left, right, running, platforms, player, arme, screen,width,height,entities):
        if self.inv > 0:
            self.inv-=1
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        # do y-axis collisions
        return self.hitbox(0, self.yvel, player, arme, screen)

    def hitbox(self, xvel, yvel, player,arme, screen):
        if sprite.collide_rect(self, player):
            return True
        else:
            return False
