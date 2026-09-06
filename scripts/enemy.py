import pygame
from scripts import settings,animation,level

class Goblin:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speedx = settings.GOBLINSPEED
        self.scale = settings.GOBLINSCALE
        self.anims = {
            "idle":animation.Animation("assets/enemies sprites/goblin/goblin_idle_anim_strip_4.png",9,4,10),
            "run":animation.Animation("assets/enemies sprites/goblin/goblin_run_anim_strip_6.png",9,6,5),
            

            
            
        }
        self.state = "idle"
        self.direction = "right"
        self.mr = False
        self.ml = False
        self.gravity = 1
        self.sd = 0

    def render(self,screen):

        self.anims[self.state].render(screen,self.x-level.camerax,self.y-level.cameray,self.direction)

    def update(self):
        self.anims[self.state].update()
        if self.mr == True:
            self.direction = "right"
            self.x += self.speedx
            self.state = "run"

        if self.ml == True:
            self.direction = "left"
            self.x -= self.speedx
            self.state = "run"

        if self.mr == False and self.ml == False:
            self.state = "idle"
        self.sd += self.gravity
        self.y += self.sd

enemylist = []
