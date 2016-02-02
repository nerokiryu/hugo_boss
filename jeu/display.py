import sys
import pygame

# Methode permettant de charger une image
# et renvoyant l'objet surface associee
def load_image(name):
    image = pygame.image.load(name)
    return image

def display(screen, background_image, background_position, invader, my_hero):
    # Essai de changer l'image de nos personnages
    invader.change_img_arret()
    if my_hero.mouv == False:
        my_hero.change_img_arret()
    else:
        my_hero.change_img_mouvement()

    # Ajoute nos images a afficher
    screen.blit(background_image, background_position)
    screen.blit(invader.get_img(), invader.get_rect())
    screen.blit(my_hero.get_img(), my_hero.get_rect())

    # Affichage
    pygame.display.flip()
    screen.blit

    # Limite le nombre d'images par seconde
    pygame.time.wait(10)

def display_game_over(screen, background_image, background_position):
	# Cree un objet 'font' (police) necessaire pour afficher du texte
	basicfont = pygame.font.SysFont(None, 48)

	# Cree une 'surface' avec notre Font
	# Les parametres sont le texte, l'antialiasing, et la couleur RVB
	text = basicfont.render('Game Over', True, (255, 0, 0))

	# Affichage de la surface au centre
	textrect = text.get_rect()
	textrect.centerx = screen.get_rect().centerx
	textrect.centery = screen.get_rect().centery
	screen.blit(text, textrect)

	pygame.display.flip()
	screen.blit
	pygame.time.wait(1000)
