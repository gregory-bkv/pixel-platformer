import pygame
from scripts import settings,animation,level
import pytmx
import random

class Goblin:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speedx = settings.GOBLINSPEED
        self.scale = settings.GOBLINSCALE
        self.hp = 100
        self.anims = {
            "idle":animation.Animation("assets/enemies sprites/goblin/goblin_idle_anim_strip_4.png",9,4,5),
            "run":animation.Animation("assets/enemies sprites/goblin/goblin_run_anim_strip_6.png",9,6,5),
            "death":animation.Animation("assets/enemies sprites/goblin/goblin_death_anim_strip_6.png",9,6,5),
            "hit":animation.Animation("assets/enemies sprites/goblin/goblin_hit_anim_strip_3.png",9,3,4)
            

            
            
        }
        self.state = "idle"
        self.direction = "right"
        self.mr = False
        self.ml = False
        self.gravity = 1
        self.sd = 0
        self.timer = 100
        self.deathtimer = 30
        self.hittimer = 0

    def render(self,screen):

        self.anims[self.state].render(screen,self.x-level.camerax,self.y-level.cameray,self.direction)

    def update(self):
        self.anims[self.state].update()
        if self.hp > 0:
            if self.mr == True:
                self.direction = "right"
                self.x += self.speedx
                self.collisionx()
                self.state = "run"

            if self.ml == True:
                self.direction = "left"
                self.x -= self.speedx
                self.collisionx()
                self.state = "run"

            if self.mr == False and self.ml == False:
                self.state = "idle"
            self.sd += self.gravity
            self.y += self.sd
            self.collisiony()

        if self.hp <= 0:
            self.state = "death"
            self.deathtimer -= 1
            if self.deathtimer <= 0:
                enemylist.remove(self)

        if self.hittimer > 0 :
            self.state = "hit"
            self.hittimer -= 1

        


    def get_hitbox(self):
        return pygame.Rect(self.x,self.y,130,150).inflate(-20,-10)
    def collisionx(self):
            player_hitbox = self.get_hitbox()
            for i in level.hitboxes:
                  if player_hitbox.colliderect(i):
                        if self.direction == "right":
                            player_hitbox.right = i.left
                        else:
                            player_hitbox.left = i.right
            self.x = player_hitbox.x - 10
    def collisiony(self):
        player_hitbox = self.get_hitbox()
        for i in level.hitboxes:
             if player_hitbox.colliderect(i):
                if self.sd > 0 : #fall
                    player_hitbox.bottom = i.top
                    self.sd = 0
                    self.jumps = 0
                    self.timeinair = 0
                else:
                    player_hitbox.top = i.bottom
                    self.sd = 0
        self.y = player_hitbox.y -5

    def control(self):
        self.timer -= 1
        
        if self.timer == 0:
            if self.mr == True or self.ml ==True:
                self.mr = False
                self.ml = False
                self.timer = 100
            else:
                r = random.randint(0,1)
                if r == 1:
                    self.mr = True
                    self.timer = 100
                else:
                    self.ml = True
                    self.timer =100
        if self.state == "hit":
            self.mr = False
            self.ml = False

    def goblin_attack_area(self):
        if self.direction == "left":
            return pygame.Rect(self.x - 130-level.camerax,self.y-level.cameray,150,150)
        else:
            return pygame.Rect(self.x +130-level.camerax,self.y-level.cameray,150,150)

    def health_bar_enemy(self,screen):
        pygame.draw.rect(screen,[255,0,0],(self.x-10-level.camerax,self.y -40-level.cameray,1.5*self.hp,35))
        pygame.draw.rect(screen,[255,255,255],(self.x-10-level.camerax,self.y -40-level.cameray,150,35),5)



def load_enemys():
    world = pytmx.load_pygame("tiled/world.tmx")
    for i in world.get_layer_by_name("Goblins"):
        if i[2]!=0:
            goblin = Goblin(i[0]*32*3,i[1]*32*3)
            enemylist.append(goblin)

enemylist = []
