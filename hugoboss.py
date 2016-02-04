import sys
import pygame
import os



sys.path.append(os.path.join('menu'))

pygame.init()
pygame.mixer.music.load('menu.mp3')
pygame.mixer.music.play()

execfile("menu/menu.py")
