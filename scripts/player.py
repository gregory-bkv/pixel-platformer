import pygame
from scripts import settings
from scripts import animation
from scripts import level,dust
lefthealthbar = pygame.image.load("assets/hud elements/health_hud_left.png")
lefthealthbar = pygame.transform.scale_by(lefthealthbar,4)
midhealthbar = pygame.image.load("assets/hud elements/health_hud_middle.png")
midhealthbar = pygame.transform.scale_by(midhealthbar,4)
righthealthbar = pygame.image.load("assets/hud elements/health_hud_right.png")
righthealthbar = pygame.transform.scale_by(righthealthbar,4)

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hp = 100
        self.speedx = settings.PLAYERSPEED
        self.scale = settings.PLAYERSCALE
        self.anims = {
            "idle":animation.Animation("assets/herochar sprites(new)/herochar_idle_anim_strip_4.png",9,4,10),
            "run":animation.Animation("assets/herochar sprites(new)/herochar_run_anim_strip_6.png",9,6,5),
            "jumpup":animation.Animation("assets/herochar sprites(new)/herochar_jump_up_anim_strip_3.png",9,3,10),
            "jumpdown":animation.Animation("assets/herochar sprites(new)/herochar_jump_down_anim_strip_3.png",9,3,10),
            "doublejump":animation.Animation("assets/herochar sprites(new)/herochar_jump_double_anim_strip_3.png",9,3,3),
            "heroattack":animation.Animation("assets/herochar sprites(new)/herochar_sword_attack_anim_strip_4.png",9,4,3)

            
            
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
        if self.state == "heroattack" and self.direction == "left":
            self.anims[self.state].render(screen,self.x-130-level.camerax,self.y-level.cameray,self.direction)
        else:
            self.anims[self.state].render(screen,self.x-level.camerax,self.y-level.cameray,self.direction)

        pygame.draw.rect(screen,[255,0,0],[50,50,275/100*self.hp,43])
        screen.blit(lefthealthbar,(45,40))
        for i in range(4):
            screen.blit(midhealthbar,(90+45*i,40))
        screen.blit(righthealthbar,(90+45*4,40))
        pygame.draw.rect(screen,[255,0,0],self.get_attack_area().move(-level.camerax,-level.cameray),2)

        
       
        

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

    def get_attack_area(self):
        if self.direction == "left":
            return pygame.Rect(self.x - 130,self.y,150,150)
        else:
            return pygame.Rect(self.x +130,self.y,150,150)
    
        
hero = Player(400,500)

