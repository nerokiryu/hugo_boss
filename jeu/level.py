from pygame import *
import sys
font.init()
from math import cos,radians
try: import GetEvent
except: from . import GetEvent

def generateLvl(num):
    #Utilisation des plateform
    #
    # D M E     H   JKL
    # O I N     F
    # B P C     G   A
    #
    # I P I
    # N   O
    # I M I
    if num == 1:
        lvl = [
            "IPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPI",
            "N                                                                       O",
            "N                                                                       O",
            "N                                                                       O",
            "N                                                                       O",
            "N                                                                       O",
            "N                                                                       O",
            "N                                                                       O",
            "N                                                                       O",
            "N                                                                       O",
            "N                                                                       O",
            "N                                                                       O",
            "N                                                                       O",
            "N                             JKKKKKKKKKKKL                             O",
            "N                                                                       O",
            "N         JKKKKKKKKKKKL                           JKKKKKKKKKKKL         O",
            "N                                                                       O",
            "N                                                                       O",
            "N                                                                       O",
            "IMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMI",]

    elif num == 2 :
        lvl = [
            "IPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPI",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N  DMMMMMMMMMMMMMMMME                                                        O",
            "N  F     OIIIIIIIIIIMMMMMMMME                                                O",
            "N  F     OIIIIIIIIIIIIIIIIIIIMMMMMMME                                        O",
            "N  F     BPPPPPPPPPPPPPPPPPPPPPPPPPPPKKKKKKKL                                O",
            "N  F                                                                         O",
            "N  F                                                    A                    O",
            "N  F                                                                         O",
            "N  F                                                                         O",
            "N  F                                                                         O",
            "N  F                                                                JKKKKKKKKI",
            "N  F                                                                         O",
            "N  F                                                                         O",
            "N  F                                                                         O",
            "N  F                                              JKKKKKKL                   O",
            "N  F                                                                         O",
            "N  F                                A                                        O",
            "N  F                                                                         O",
            "N  G     JKKKKKKKKKKKKL                                                      O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "IMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMI",]

    else :
        lvl = [
            "IPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPI",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "IMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMI",]

    return lvl;

def generateBg(num):
    if num == 1:
        bg = ("graphics/background/ice.png")
    if num == 2:
        bg = ("graphics/background/ice.png")
    elif num == 3:
        bg = ("graphics/background/hell.png")
    else :
        bg = ("graphics/background/darkness.png")
    return bg

def generateTypePlateform(num):
    if num == 1:
        typePl = "herbe"
    elif num == 2:
        typePl = "glace"
    else:
	typePl = "terre"
    return typePl
