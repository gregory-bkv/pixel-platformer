import pygame
from scripts import utilus
import pytmx

camerax = 0
cameray = 0
worldimage = utilus.loadimage("tiled/world.png",3)
hitboxes = []
def loadground():
    world = pytmx.load_pygame("tiled/world.tmx")
    for i  in world.get_layer_by_name("ground"):
        if i[2] != 0:
            hitbox = pygame.Rect([i[0]*32*3,i[1]*32*3],[32*3,32*3])
            hitboxes.append(hitbox)
def render(screen:pygame.Surface):
    screen.blit(worldimage,[0-camerax,0-cameray])

def get_goblincoards():
    goblincoards = []
    world = pytmx.load_pygame("tiled/world.tmx")
    for i in world.get_layer_by_name("goblins"):
        if i[2]!=0:
            goblincoards.append([i[0]*32*3,i[1]*32*3])
    return goblincoards