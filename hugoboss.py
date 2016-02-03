import sys
import pygame
import os

# Importe la classe Invader and MyHero
# se trouvant dans les fichiers
# invader.py et myhero.py

sys.path.append(os.path.join('menu'))

pygame.init()
pygame.mixer.music.load('menu.mp3')
pygame.mixer.music.play()

execfile("menu/menu.py")
