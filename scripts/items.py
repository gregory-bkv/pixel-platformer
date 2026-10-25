import pygame
from scripts import animation,level
import pytmx
countcoin = 0
pygame.init()
font = pygame.font.Font(None,70)
imagecoin = pygame.image.load("assets/hud elements/coins_hud.png")
imagecoin = pygame.transform.scale_by(imagecoin,5)

class Coin:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.coinanim = animation.Animation("assets/miscellaneous sprites/coin_anim_strip_6.png",9,6,4)
        self.coinanimtaken = animation.Animation("assets/miscellaneous sprites/coin_pickup_anim_strip_6.png",9,6,4)
        self.state = "untaken"
        self.height = 60
        self.width = 60
        self.timer = 24
 


    def render(self,screen):
        if self.state == "untaken":
            self.coinanim.render(screen,self.x-level.camerax,self.y-level.cameray,"right")

        if self.state == "taken":
            self.coinanimtaken.render(screen,self.x-level.camerax,self.y-level.cameray-60,"right")
        self.hitbox = self.get_hitbox()


    def update(self):
        global countcoin
        if self.state == "untaken":
            self.coinanim.update()
        if self.state == "taken":
            self.coinanimtaken.update()
            self.timer -= 1
            if self.timer == 0:
                items.remove(self)
                countcoin += 1
                

    def get_hitbox(self):
       return pygame.Rect(self.x,self.y,self.width,self.height)

items = []
def loadcoins():
    world = pytmx.load_pygame("tiled/world.tmx")
    for i in world.get_layer_by_name("coins"):
        if i[2] != 0:
            coin = Coin(i[0]*32*3,i[1]*32*3)
            items.append(coin)
def render_count_coins(screen):
    image = font.render(f"{countcoin}",True,[255,255,255])
    screen.blit(image,[screen.get_width()-90,50])
    screen.blit(imagecoin,[screen.get_width()-150,50])
