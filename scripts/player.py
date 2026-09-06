import pygame
from scripts import settings
from scripts import animation
from scripts import level,dust


class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speedx = settings.PLAYERSPEED
        self.scale = settings.PLAYERSCALE
        self.anims = {
            "idle":animation.Animation("assets/herochar sprites(new)/herochar_idle_anim_strip_4.png",9,4,10),
            "run":animation.Animation("assets/herochar sprites(new)/herochar_run_anim_strip_6.png",9,6,5),
            "jumpup":animation.Animation("assets/herochar sprites(new)/herochar_jump_up_anim_strip_3.png",9,3,10),
            "jumpdown":animation.Animation("assets/herochar sprites(new)/herochar_jump_down_anim_strip_3.png",9,3,10),
            "doublejump":animation.Animation("assets/herochar sprites(new)/herochar_jump_double_anim_strip_3.png",9,3,3),
            "heroattack":animation.Animation("assets/herochar sprites(new)/herochar_attack_anim_strip_4(new).png",9,4,3)

            
            
        }
        self.state = "idle"
        self.mr = False
        self.ml = False
        self.direction = "right"
        self.gravity = 1
        self.sd = 0
        self.maxjumps = 2
        self.jumps = 0
        self.timeinair = 0
        self.attacktimer  = 0

    def render(self,screen):

        self.anims[self.state].render(screen,self.x-level.camerax,self.y-level.cameray,self.direction)
        

    def update(self):
        self.timeinair += 1
        self.anims[self.state].update()
        self.sd += self.gravity
        self.y += self.sd
        self.collisiony()
        if self.ml == True:
            self.x -= self.speedx
            self.collisionx()
            self.state = "run"
            self.direction = "left"
        if self.mr == True:
            self.x += self.speedx
            self.collisionx()
            self.state = "run"
            self.direction = "right"
        if self.mr == False and self.ml == False:
                self.state = "idle"
        if self.timeinair > 5:
            if self.sd > 0 : #fall
                self.state =  "jumpdown"
            else:
                self.state = "jumpup"
        if self.jumps == 2:
            self.state = "doublejump"
        if self.attacktimer > 0 :
            self.state = "heroattack"
            self.attacktimer -= 1           
        

    def get_hitbox(self):
        player_hitbox = pygame.Rect([self.x+20,self.y,100,150])
        return player_hitbox
        
    def collisionx(self):
        player_hitbox = self.get_hitbox()
        for i in level.hitboxes:
              if player_hitbox.colliderect(i):
                    if self.direction == "right":
                        player_hitbox.right = i.left
                    else:
                        player_hitbox.left = i.right
        self.x = player_hitbox.x - 20
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
        self.y = player_hitbox.y

    def jump(self):
        if self.jumps < self.maxjumps:
            self.sd = -20
            self.jumps += 1
            if self.state != "doublejump" and self.state != "jumpup" and self.state != "jumpdown":
                dd =dust.Dust(self.x,self.y)
                dust.dusts.append(dd) 
    
        
hero = Player(400,500)

