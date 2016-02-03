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
    if num == 1:
        lvl = [
            "DKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKI",
            "F                                                                       F",
            "F                                                                       F",
            "F                                                                       F",
            "F                                                                       F",
            "F                                                                       F",
            "F                                                                       F",
            "F                                                                       F",
            "F                                                                       F",
            "F                                                                       F",
            "F                                                                       F",
            "F                                                                       F",
            "F                                                                       F",
            "F                             JKKKKKKKKKKKL                             F",
            "F                                                                       F",
            "F         JKKKKKKKKKKKL                           JKKKKKKKKKKKL         F",
            "F                                                                       F",
            "F                                                                       F",
            "F                                                                       F",
            "BKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKC",]

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
            "N  F     OPPPPPPPPPPPPPPPPPPPPPPPPPPPKKKKKKKL                                O",
            "N  F                                                                         O",
            "N  F                                                    A                    O",
            "N  F                                                                         O",
            "N  F                                                                         O",
            "N  F                                                                         O",
            "N  F                                                                JKKKKKKKKO",
            "N  F                                                                         O",
            "N  F                                                                         O",
            "N  F                                                                         O",
            "N  F                                              JKKKKKKL                   O",
            "N  F                                                                         O",
            "N  F                                A                                        O",
            "N  F                                                                         O",
            "N  F     BKKKKKKKKKKKKL                                                      O",
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
    elif num == 2:
        bg = ("graphics/background/hell.png")
    else :
        bg = ("graphics/background/darkness.png")
    return bg

def generateTypePlateform(num):
    if num == 1:
        typePl = "glace"
    else:
        typePl = "terre"
    return typePl
