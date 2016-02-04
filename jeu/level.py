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
            "IMMMMMME  DMMMMMME  DMMMMMME  DMMMMMME  DMMMMMME  DMMMMMME  DMMMMMME  DMMMMMMI",
            "IIIIIIIN  OIIIIIIN  OIIIIIIN  OIIIIIIN  OIIIIIIN  OIIIIIIN  OIIIIIIN  OIIIIIII",
            "IIIIIIIN  OIIIIIIN  OIIIIIIN  OIIIIIIN  OIIIIIIN  OIIIIIIN  OIIIIIIN  OIIIIIII",
            "IIIIIIIIMMIIIIIIIIMMIIIIIIIIMMIIIIIIIIMMIIIIIIIIMMIIIIIIIIMMIIIIIIIIMMIIIIIIII",]

    elif num == 3 :
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
            "N      MMMMMM      MMMMMM      MMMMMM      MMMMMM      MMMMMM      MMMMMM    O",
            "IMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMI",]

    else :
        lvl = [
            "IPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPI",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                          JKKKKKKKKKKKKKKKKKKKKKKL                          O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N        JE         JE                                  DL         DL        O",
            "N         BE         BE                                DC         DC         O",
            "N          BE         BE                              DC         DC          O",
            "N           BE         BE                            DC         DC           O",
            "N            BL         BL           JKKL           JC         JC            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N              DL         DL                      JE         JE              O",
            "N             DC         DC                        BE         BE             O",
            "N            DC         DC                          BE         BE            O",
            "N           DC         DC            DKKE            BE         BE           O",
            "N          JC         JC            JC  BL            BL         BL          O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "IMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMI",]

    return lvl;

def generateBg(num):
    if num == 1:
        bg = ("graphics/background/forest.png")
    elif num == 2:
        bg = ("graphics/background/ice.png")
    elif num == 3:
        bg = ("graphics/background/darkness.png")
    else :
        bg = ("graphics/background/hell.png")
    return bg

def generateTypePlateform(num):
    if num == 1:
        typePl = "herbe"
    elif num == 2:
        typePl = "glace"
    elif num == 4:
        typePl = "terre"
    else:
        typePl = "brique"
    return typePl
