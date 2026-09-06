import pygame


def loadimage(filepath: str,scale: float) -> pygame.Surface:
    file=pygame.image.load(filepath)
    transscale=pygame.transform.scale(file,(file.get_width()*scale,file.get_height()*scale))

    return transscale

def loadimages(filepath: str,scale: float,count: int) -> list[pygame.Surface]:
    spritesheet = loadimage(filepath,scale)
    w = spritesheet.get_width() // count
    h = spritesheet.get_height()
    sprites = []
    x = 0
    for i in range(count):
        sprite = spritesheet.subsurface(x,0,w,h)
        sprites.append(sprite)
        x += w

    return sprites 

