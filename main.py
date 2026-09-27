import pygame
import random
from scripts import utilus
from scripts import animation
from scripts import player
from scripts import level
from scripts import settings,dust,enemy

screen = pygame.display.set_mode([0,0],pygame.FULLSCREEN)
clock = pygame.time.Clock()
enemy.load_enemys()


level.loadground()
while True:
    clock.tick(60)
    events = pygame.event.get()
    level.render(screen)
    level.camerax += (player.hero.x - screen.get_width() // 2 - level.camerax) // settings.CAMERASENSIVITY 
    level.cameray += (player.hero.y - screen.get_height() // 2 - level.cameray) // settings.CAMERASENSIVITY 
    if level.camerax <= 0:
        level.camerax = 0
    if level.cameray <= 0:
        level.cameray = 0
    player.hero.render(screen)
    player.hero.update()
    for i in enemy.enemylist:
        i.render(screen)
        i.update()
        i.control()
    for i in dust.dusts:
        i.render(screen)
        i.update()
    for i in events:
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                exit()
            if i.key == pygame.K_a:
                player.hero.ml = True
                player.hero.mr = False
            if i.key == pygame.K_d:
                player.hero.mr = True
                player.hero.ml = False
            if i.key == pygame.K_SPACE:
                player.hero.jump()
            if i.key == pygame.K_e:
                if player.hero.state != "heroattack":
                    player.hero.attacktimer = 12
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_a:
                player.hero.ml = False
            if i.key == pygame.K_d:
                player.hero.mr = False
            
    pygame.display.update()
    screen.fill([0,0,0])