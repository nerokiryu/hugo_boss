import sys
import pygame 
import os

# Importe la classe Invader and MyHero
# se trouvant dans les fichiers
# invader.py et myhero.py
from invader import Invader
from myhero import MyHero

# Importe toute les methodes du module display
from display import *

def game_loop():
	speed = [1, 1]
	invader = Invader(0, 0, "InvaderA_00.png", "InvaderA_01.png", speed)

	# Idem, on cree notre hero en tant qu'objet MyHero
	my_hero = MyHero(width/2, height/2, "../Graphics/Character/V2/Walk_1.png", "../Graphics/Character/V2/Walk_2.png")

	# Boucle de jeu
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()

		# Deplacement
		invader.movement(width, height)
		my_hero.movement(width, height)

		# Test de collision
		# On utilise 'collidepoint', qui test si le centre de 
		# My_Hero est convenu dans le rectangle de l'Invader
		if invader.get_rect().collidepoint(my_hero.get_rect().center):
			display_game_over(screen, background_image, background_position)
			sys.exit()
		else:
			# Affichage
			display(screen, background_image, background_position, invader, my_hero)

############################################
## POINT D ENTREE DU CODE ##
# A NOTER : toutes les variables declarees 
# dans une partie non indentee sont globales

# Init pygame modules
pygame.init()

# Affiche la fenetre
os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

# Lance la musique
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(10)

# Charge l'image de fond
background_image = load_image("background.jpg")
background_position = [0, 0]

# lance la boucle de jeu
game_loop()
