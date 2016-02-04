#! /usr/bin/python
import sys
from random import randint
from pygame import *
import math
from time import sleep

sys.path.append(os.path.join('menu'))
sys.path.append(os.path.join('jeu'))
sys.path.append(os.path.join('hugo_boss.py'))

from boss import *
from player import *
from entity import *
from level import *
from plateform import *
from arme import *
from camera import *
from exitBlock import *


WIN_WIDTH = 800
WIN_HEIGHT = 640


DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30


def end(num,win):
    while True:
        scr.blit(bg,bg.get_rect(center=scr.get_rect().center))
        #~ scr.fill(-1)
        display.flip();print(menu.__doc__)
        if win:
            resp = menu([u'rejouer::Faire une nouvelle boucle_de_jeu',
                         u'retour au menu::Retourner au menu',
                         u'continuer::Niveau suivant',
                         u'quitter::Quitter le Jeu'])
        else:
            resp = menu([u'rejouer::Faire une nouvelle boucle_de_jeu',
                         u'retour au menu::Retourner au menu',
                         u'quitter::Quitter le Jeu'])

        if resp[0] == u'retour au menu':
                execfile("hugoboss.py")
        elif resp[0] == u'rejouer':
            execfile("jeu/jeu.py")
        elif resp[0] == u'continuer':
            num += 1
            sys.argv=["jeu.py",num]
            execfile("jeu/jeu.py")
        else:
		sys.exit()

def main():
    # Numero du niveau #
    num = sys.argv[1]

    # Generation des elements du niveau #
    level = generateLvl(num)
    lvlBg = generateBg(num)

    print(num)
    global cameraX, cameraY
    init()
    screen = display.set_mode(DISPLAY, FLAGS, DEPTH)
    display.set_caption("Hugo Boss")
    timer = time.Clock()
    pygame.key.set_boucle_de_jeueat(1,1000)
    up = down = left = right = running = False
    atk = 0

    ########################CREATION LVL##########################
    bg = Surface((32,32))
    bg.convert()
    bg.fill(Color("#000000"))
    entities = sprite.Group()
    arme = Arme(32, 32)
    arme.realease()
    if num == 1 :
        boss = Boss1(500, 32)
    elif num == 2 :
        boss = Boss2(500, 32)
    elif num == 3 :
        boss = Boss4(500, 500)
    else:
        boss = Boss3(500, 32)

    boss.realease()
    player = Player(32, 32)
    player.realease()
    platforms = []

    x = y = 0

    #############################################################################

    # build the level
    for row in level :
        for col in row :
            if col >= "A" and col <= "P":
                p = Platform(x, y, col)
                platforms.append(p)
                entities.add(p)
            if col == "Z":
                e = ExitBlock(x, y)
                platforms.append(e)
                entities.add(e)

            x += 32
        y += 32
        x = 0
    #############################################################################


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
    win = False
    boucle_de_jeu = True
    while boucle_de_jeu:
        timer.tick(60)

        for e in event.get():
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
            if e.type == KEYDOWN and e.key == K_v :
                running = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_v or atk !=0:
                running = False

        # Dessine background
        screen.blit(pygame.image.load(lvlBg), (0,0))

        camera.update(player)

        # update player, draw everything else
        if player.update(up, down, left, right, running, platforms, boss, screen):
            boucle_de_jeu = False
        if boss.update(up, down, left, right, running, platforms, player, arme, screen,total_level_width,total_level_height) and boucle_de_jeu == True:
            boucle_de_jeu = False
        if arme.update(up, down, left, right, running, platforms,boss, player, screen) and boucle_de_jeu == True:
            #Si le update de l'arme devient vraie alors la cause de la sortie de la boucle sera une victoire
            boucle_de_jeu = False
            win = True
        else:
            atk = arme.atk

        for e in entities:
            screen.blit(e.image, camera.apply(e))

        display.update()

    end(num,win)

if __name__ == "__main__":
    main()
