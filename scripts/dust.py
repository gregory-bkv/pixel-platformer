import pygame
from scripts import animation,level


class Dust:
    def __init__(self,x,y):
        self.x = x
        self.y = y+60
        self.anim = animation.Animation("assets/herochar sprites(new)/herochar_after_jump_dust_anim_strip_4.png",5,4,3)
        self.lifetimer = 12
    def render(self,screen):
        self.anim.render(screen,self.x-level.camerax,self.y-level.cameray,"right")

    def update(self):
        self.anim.update()
        self.lifetimer -= 1
        if self.lifetimer == 0:
            dusts.remove(self)
            
dusts = []