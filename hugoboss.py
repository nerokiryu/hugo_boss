import sys
import pygame
import os

sys._clear_type_cache()
sys.exc_clear()
# Importe la classe Invader and MyHero
# se trouvant dans les fichiers
# invader.py et myhero.py

sys.path.append(os.path.join('menu'))

pygame.init()
pygame.mixer.music.load('menu.mp3')
pygame.mixer.music.play(-1)

execfile("menu/menu.py")
