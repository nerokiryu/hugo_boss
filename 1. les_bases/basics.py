import pygame
import os

# Methode permettant de charger une image
# et renvoyant l'objet surface associee 
def load_image(name):
    image = pygame.image.load(name)
    return image

# Init modules pygames
pygame.init()

# Charge l'image de fond
background_image = load_image("background.jpg")
background_position = [0, 0]

# Affiche la fenetre
os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

# Lance la musique
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()

# Game loop
while 1:
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    		sys.exit()

	# Ajoute notre images a la file des affichages prevus
	screen.blit(background_image, background_position)

    # Affiche toute la liste FIFO (ici que notre image de fond)
    pygame.display.flip()
    screen.blit
