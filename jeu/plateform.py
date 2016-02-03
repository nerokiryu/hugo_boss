import sys
from random import randint
from pygame import *
import math

from time import sleep

from entity import Entity

class Platform(Entity):
    def __init__(self, x, y, col):
        Entity.__init__(self)
        name = "graphics/decor/glace/"+ col +".png"
        self.image = image.load(name)
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass
