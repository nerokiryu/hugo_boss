import sys
from random import randint
from pygame import *
import math

from time import sleep

from plateform import *

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))
