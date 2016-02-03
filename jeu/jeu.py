#! /usr/bin/python

import pygame
import sys
import os
from pygame import *
import math
from random import randint
from time import sleep

sys.path.append(os.path.join('menu'))
sys.path.append(os.path.join('jeu'))
sys.path.append(os.path.join('hugo_boss.py'))

# Gestion des images #
# Gestion du hero #
img_herof="graphics/character/hero/hero.png"
# Gestion des images #

WIN_WIDTH = 800
WIN_HEIGHT = 640
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30

def main():
    global cameraX, cameraY
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Use arrows to move!")
    timer = pygame.time.Clock()

    up = down = left = right = running = False

    ########################CREATION LVL##########################
    bg = Surface((32,32))
    bg.convert()
    bg.fill(Color("#000000"))
    entities = pygame.sprite.Group()
    arme = Arme(32, 32)
    boss = Boss(200, 32)
    boss.realease()
    player = Player(32, 32)
    platforms = []

    x = y = 0
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                          P",
        "P                                          P",
        "P       PPPPPPPP                           P",
        "P                                          P",
        "P                    PPPPPPPPPPP           P",
        "P                                          P",
        "P                                          P",
        "P    PPPPPPPPPPPPPP                        P",
        "P                                   PPPPPPPP",
        "P                          PPPPPPPPP       P",
        "P                        P                 P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P         CPPPPPPPD                        P",
        "P                                          P",
        "P                                PPPPPPPPPPP",
        "P                                          P",
        "P                                          P",
        "P            PPP                           P",
        "P                                          P",
        "P                                          P",
        "PPPP                                       P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "E":
                e = ExitBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "C":
                e = Platform_Left(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "D":
                e = Platform_Right(x, y)
                platforms.append(e)
                entities.add(e)

            x += 32
        y += 32
        x = 0

    total_level_width  = len(level[0])*32
    total_level_height = len(level)*32
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)
    entities.add(boss)
    entities.add(arme)

    #############################################################################

    total_level_width  = len(level[0])*32
    total_level_height = len(level)*32
    #############################MOUVEMENT#######################################

    while 1:
        timer.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                running = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_SPACE:
                running = True

        # draw background
        """for y in range(32):
            for x in range(32):"""
        screen.blit(pygame.image.load("graphics/background/hell.png"), (0,0))

        camera.update(player)

        # update player, draw everything else
        player.update(up, down, left, right, running, platforms, boss, screen)
        boss.update(up, down, left, right, running, platforms, player, arme, screen)
        arme.update(up, down, left, right, running, platforms,boss, player, screen)
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Boss(Entity):
    coll = False
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32,32))
        self.image.fill(Color("#FF0000"))
        self.onGround = False
        self.image.convert()
        self.xvel = x
        self.yvel = y
        self.rect = Rect(x, y, 32, 32)

    def realease(self):
        self.xvel = 8

    def update(self, up, down, left, right, running, platforms, player, arme, screen):

        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100: self.yvel = 100
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        rand=randint(0,100)
        if rand<=15:
            if self.onGround: self.yvel -= 8
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

        self.hitbox(0, self.yvel, player, arme, screen)


    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
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
        if pygame.sprite.collide_rect(self, player):
            basicfont = pygame.font.SysFont(None, 48)
            text = basicfont.render('Game Over', True, (255, 0, 0))
            textrect = text.get_rect()
            textrect.centerx = screen.get_rect().centerx
            textrect.centery = screen.get_rect().centery
            screen.blit(text, textrect)
            pygame.display.flip()
            screen.blit
            pygame.time.wait(1000)
	    while True:
		scr.blit(bg,bg.get_rect(center=scr.get_rect().center))
		#~ scr.fill(-1)
		display.flip();print(menu.__doc__)
		resp = menu([u'rejouer::Faire une nouvelle partie',
		             u'retour au menu::Quitter le jeu'])

		if resp[0] == u'retour au menu':
           		execfile("hugoboss.py")
		elif resp[0] == u'rejouer':
			execfile("jeu/jeu.py")
        if pygame.sprite.collide_rect(self, arme):
            basicfont = pygame.font.SysFont(None, 48)
            text = basicfont.render('Win', True, (255, 0, 0))
            textrect = text.get_rect()
            textrect.centerx = screen.get_rect().centerx
            textrect.centery = screen.get_rect().centery
            screen.blit(text, textrect)
            pygame.display.flip()
            screen.blit
            pygame.time.wait(1000)
	    while True:
		scr.blit(bg,bg.get_rect(center=scr.get_rect().center))
		#~ scr.fill(-1)
		display.flip();print(menu.__doc__)
		resp = menu([u'rejouer::Faire une nouvelle partie',
		             u'retour au menu::Quitter le jeu'])

		if resp[0] == u'retour au menu':
           		execfile("hugoboss.py")
		elif resp[0] == u'rejouer':
			execfile("jeu/jeu.py")

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.image = load_image(img_herof).convert()
        (hauteur, largeur) = self.image.get_size()
        self.rect = Rect(x, y, hauteur, largeur)

    def update(self, up, down, left, right, running, platforms, boss, screen):
        if up:
            # Jump si sur le sol
            if self.onGround: self.yvel -= 8
        if down:
            #Rien ne se passe
            pass
        if running:
            self.xvel = 12
        if left:
            self.xvel = -8
        if right:
            self.xvel = 8
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

        self.hitbox(0, self.yvel, boss, screen)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                    print "collide right"
                if xvel < 0:
                    self.rect.left = p.rect.right
                    print "collide left"
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    print "collide top"

    def hitbox(self, xvel, yvel, boss, screen):
        if pygame.sprite.collide_rect(self, boss):
            basicfont = pygame.font.SysFont(None, 48)
            text = basicfont.render('Game Over', True, (255, 0, 0))
            textrect = text.get_rect()
            textrect.centerx = screen.get_rect().centerx
            textrect.centery = screen.get_rect().centery
            screen.blit(text, textrect)
            pygame.display.flip()
            screen.blit
            pygame.time.wait(1000)
	    while True:
		scr.blit(bg,bg.get_rect(center=scr.get_rect().center))
		#~ scr.fill(-1)
		display.flip();print(menu.__doc__)
		resp = menu([u'rejouer::Faire une nouvelle partie',
		             u'retour au menu::Quitter le jeu'])

		if resp[0] == u'retour au menu':
           		execfile("hugoboss.py")
		elif resp[0] == u'rejouer':
			execfile("jeu/jeu.py")

class Arme(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((30,30))
        self.image.fill((255,255,255,128), None, pygame.BLEND_RGBA_MULT)
        self.image.set_alpha(0)
        self.onGround = False
        self.image.convert()
        self.xvel = 0
        self.yvel = 0
        self.rect = Rect(x, y, 32, 32)

    def update(self, up, down, left, right, running, platforms, boss, player, screen):
        self.rect.top = player.rect.top
        self.rect.left = player.rect.left

        self.hitbox(0, self.yvel, boss, screen)

    def hitbox(self, xvel, yvel, boss, screen):
        if pygame.sprite.collide_rect(self, boss):
            basicfont = pygame.font.SysFont(None, 48)
            text = basicfont.render('Win', True, (255, 0, 0))
            textrect = text.get_rect()
            textrect.centerx = screen.get_rect().centerx
            textrect.centery = screen.get_rect().centery
            screen.blit(text, textrect)
            pygame.display.flip()
            screen.blit
            pygame.time.wait(1000)
	    while True:
		scr.blit(bg,bg.get_rect(center=scr.get_rect().center))
		#~ scr.fill(-1)
		display.flip();print(menu.__doc__)
		resp = menu([u'rejouer::Faire une nouvelle partie',
		             u'retour au menu::Quitter le jeu'])

		if resp[0] == u'retour au menu':
           		execfile("hugoboss.py")
		elif resp[0] == u'rejouer':
			execfile("jeu/jeu.py")

class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.blit(pygame.image.load("graphics/decor/plateforme.png"), (0,0))
        #screen.blit(pygame.image.load("fond.png"), (0,0))
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))

class Platform_Left(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.blit(pygame.image.load("graphics/decor/plateforme.png"), (0,0))
        self.rect = Rect(x, y, 32, 32)

class Platform_Right(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.blit(pygame.image.load("graphics/decor/plateforme.png"), (0,0))
        self.rect = Rect(x, y, 32, 32)

if __name__ == "__main__":
    main()
