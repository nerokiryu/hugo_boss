import sys
import os
from random import randint
from pygame import *
import math

sys.path.append(os.path.join('jeu'))

from level import *

from time import sleep

from entity import Entity

class Platform(Entity):

    def __init__(self, x, y, col):
        # Numero du niveau #
        num = sys.argv[1]
        lvlPf = generateTypePlateform(num)
        Entity.__init__(self)
        name = "graphics/decor/"+lvlPf+"/"+ col +".png"
        self.image = image.load(name)
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass
