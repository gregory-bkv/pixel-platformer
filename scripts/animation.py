import pygame
from scripts import utilus



class Animation:
    def __init__(self,loadpath: str,scale: float,count: int,timer):
        self.images = utilus.loadimages(loadpath,scale,count)
        self.index = 0
        self.count = count
        self.starttimer = timer
        self.timer = timer


    def render(self,screen: pygame.Surface,x,y,direction):
        if direction == "right":
             screen.blit(self.images[self.index],[x,y])
        if direction == "left":
            invertimage = pygame.transform.flip(self.images[self.index],True,False)
            screen.blit(invertimage,[x,y])
    def update(self):
        self.timer -= 1
        if self.timer == 0:
            self.index += 1
            self.timer = self.starttimer
            if self.index >= self.count:
                self.index = 0
        