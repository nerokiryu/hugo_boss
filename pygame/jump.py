from pygame.locals import *
import pygame
import math
from time import sleep
 
class Player:
    x = 10
    y = 500
    speed = 10
 
    # Stores if player is jumping or not.
    isjump = 0     
    
    # Force (v) up and mass m.
    v = 8 
    m = 2
            
    def moveRight(self):
        self.x = self.x + self.speed
 
    def moveLeft(self):
        self.x = self.x - self.speed
 
    def jump(self):
        self.isjump = 1
 
    def update(self):
        if self.isjump:
            # Calculate force (F). F = 0.5 * mass * velocity^2.
            if self.v > 0:
                F = ( 0.5 * self.m * (self.v*self.v) )
            else:
                F = -( 0.5 * self.m * (self.v*self.v) )
    
            # Change position
            self.y = self.y - F
 
            # Change velocity
            self.v = self.v - 1
 
            # If ground is reached, reset variables.
            if self.y >= 500:
                self.y = 500
                self.isjump = 0
                self.v = 8              
          
 
class App:
 
    windowWidth = 1000
    windowHeight = 600
    player = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player = Player() 
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        
        pygame.display.set_caption('test')
        self._running = True
        self._image_surf = pygame.image.load("this_is_8bit.jpg").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
    
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
        self.player.update()
        pygame.display.flip()
        sleep(0.03)
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
            
            if (keys[K_RIGHT]):
                self.player.moveRight()
 
            if (keys[K_LEFT]):
                self.player.moveLeft()
 
            if (keys[K_UP]):
                self.player.jump()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
