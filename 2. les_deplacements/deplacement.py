import sys
import pygame 
import os

# Methode permettant de charger une image
# et renvoie l'objet surface associee 
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

# Charge sprite    
speed = [1, 1]
invader = load_image("InvaderA_00.png")

# On charge le rectangle d'invader, correspondant a
# un tableau definissant sa position
invader_rect = invader.get_rect()

# Boucle de jeu
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()

	# Deplacement de la position (cordonnees du rectangle) de l'invader
    # en fonction du tableau speed
	invader_rect = invader_rect.move(speed)

	# Test la position de ce rectangle pour savoir si il a touche
    # un mur : les attributs left, right, bottom, top correspondent
    # au cordonnees en x ou y du carre
	if invader_rect.left < 0 or invader_rect.right > width:
		speed[0] = -speed[0]

	if invader_rect.top < 0 or invader_rect.bottom > height:
		speed[1] = -speed[1]
	
	# Ajoute nos images a la file des affichages prevus
    # On ajoute le fond d'abord pour que notre invader soit "par dessus"
	screen.blit(background_image, background_position)
	screen.blit(invader, invader_rect)

	# Affiche toute la file
	pygame.display.flip()
	screen.blit

	# Limite le nombre d'images par secondes
	pygame.time.wait(10)