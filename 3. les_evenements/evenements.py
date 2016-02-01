import sys
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
pygame.mixer.music.play(10)

# Charge sprite 
## INVADER ##   
speed = [1, 1]
invader = load_image("InvaderA_00.png")
invader_rect = invader.get_rect()

## MY_HERO ##
my_hero = load_image("InvaderB_00.png")
my_hero_rect = my_hero.get_rect()

# Boucle de jeu
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()

	## INVADER ##
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

	## MY_HERO ##
	# Recupere la touche pressee
	keys = pygame.key.get_pressed()

	# Test la touche pressee
	if keys[pygame.K_LEFT] and my_hero_rect.left > 0:
		my_hero_rect = my_hero_rect.move(-5, 0)
	
	if keys[pygame.K_RIGHT] and my_hero_rect.right < width:
		my_hero_rect = my_hero_rect.move(5, 0)

	if keys[pygame.K_UP] and my_hero_rect.top > 0:
		my_hero_rect = my_hero_rect.move(0, -5)

	if keys[pygame.K_DOWN] and my_hero_rect.bottom < height:
		my_hero_rect = my_hero_rect.move(0, 5)
	
	# Ajoute nos images a la file des affichages prevus
    # On ajoute le fond d'abord pour que notre invader soit "par dessus"
	screen.blit(background_image, background_position)
	screen.blit(invader, invader_rect)
	screen.blit(my_hero, my_hero_rect)

	# Affiche toute la liste
	pygame.display.flip()
	screen.blit

	# Limite le nombre d'images par secondes
	pygame.time.wait(10)