import sys
import pygame
import os

# Methode permettant de charger une image
# et renvoyant l'objet surface associee
def load_image(name):
	image = pygame.image.load(name)
	return image

class MySprite():
	# Constructeur, self correspond plus ou moins au 'this'
	def __init__(self, pos_x, pos_y, image1):

		# Initialisation et affectation de l'attribut image
		self.image = load_image(image1)

		# On part du principe que la taille de l'image est 48x48
		self.rect = pygame.Rect(pos_x, pos_y, 48, 48)

	# Retourne le rectangle (position)
	def get_rect(self):
		return self.rect

	# Retourne la 'surface'
	def get_img(self):
		return self.image

# Class MyHero herite de 'MySprite'
class MyHero(MySprite):
	def __init__(self, pos_x, pos_y, image1):
		MySprite.__init__(self, pos_x, pos_y, image1)

	def movement(self):
		keys = pygame.key.get_pressed()

		courir = pygame.K_LSHIFT
		# Test la touche pressee
		if keys[pygame.K_LEFT] and self.rect.left > 0:
			self.rect = self.rect.move(-5, 0)

		if keys[pygame.K_RIGHT] and self.rect.right < width:
			self.rect = self.rect.move(5, 0)

		if keys[pygame.K_UP] and self.rect.top > 0:
			self.rect = self.rect.move(0, -5)

		if keys[pygame.K_DOWN] and self.rect.bottom < height:
			self.rect = self.rect.move(0, 5)


		if keys[courir] and keys[pygame.K_LEFT] and self.rect.left > 0:
			if self.rect.left < 50:
				self.rect = self.rect.move(-self.rect.left, 0)
			else:
				self.rect = self.rect.move(-50, 0)

		if keys[courir] and keys[pygame.K_RIGHT] and self.rect.right < width:
			if self.rect.right > width-50:
				self.rect = self.rect.move(width-self.rect.right, 0)
			else:
				self.rect = self.rect.move(50, 0)

		if keys[courir] and keys[pygame.K_UP] and self.rect.top > 0:
			if self.rect.top < 50:
				self.rect = self.rect.move(0, -self.rect.top)
			else:
				self.rect = self.rect.move(0, -50)

		if keys[courir] and keys[pygame.K_DOWN] and self.rect.bottom < height:
			if self.rect.bottom > height-50:
				self.rect = self.rect.move(0, height-self.rect.bottom)
			else:
				self.rect = self.rect.move(0, 50)


# Class Invader herite de 'MySprite'
class Invader(MySprite):
	def __init__(self, pos_x, pos_y, image1, speed):
		MySprite.__init__(self, pos_x, pos_y, image1)
		self.speed = speed

	def movement(self):
		self.rect = self.rect.move(self.speed)
		# Test la position de ce rectangle pour savoir si il a touche
		# un mur : les attributs left, right, bottom, top correspondent
		# au cordonnees en x ou y du carre
		if self.rect.left < 0 or self.rect.right > width:
			self.speed[0] = -self.speed[0]

		if self.rect.top < 0 or self.rect.bottom > height:
			self.speed[1] = -self.speed[1]

def display(invader, my_hero):
	# Ajoute nos images a afficher
	screen.blit(background_image, background_position)
	screen.blit(invader.get_img(), invader.get_rect())
	screen.blit(my_hero.get_img(), my_hero.get_rect())

	# Affichage
	pygame.display.flip()
	screen.blit

	# Limite le nombre d'images par seconde
	pygame.time.wait(10)



######################## LE JEU #########################
def game_loop():
	# On cree notre objet Invader qui herite de MySprite
	speed = [1, 1]
	invader = Invader(70, 70, "InvaderA_00.png", speed)

	# Idem, on cree notre hero en tant qu'objet MyHero
	my_hero = MyHero(400, 400, "InvaderB_00.png")

	# Boucle de jeu
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# Deplacement
		invader.movement()
		my_hero.movement()

		# Affichage
		display(invader, my_hero)

#########################################################
## POINT D ENTREE DU CODE ##
# A NOTER : toutes les variables declarees
# dans une partie non indentee sont globales

# Init pygame modules
pygame.init()

# Affiche la fenetre
os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 640,480
screen = pygame.display.set_mode(size)

# Lance la musique
"""pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(10)"""

# Charge l'image de fond
background_image = load_image("background.jpg")
background_position = [0, 0]

# lance la boucle de jeu
game_loop()
