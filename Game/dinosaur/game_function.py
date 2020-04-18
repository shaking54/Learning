import sys
import pygame
from time import sleep
from pygame.sprite import Sprite
from cactus import Cactus

def check_evect(dino, cactuses, screen, gamestats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dino.jump()
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_s:
                gamestats.gameactive = True
    if len(cactuses) < 1:
        cactus = Cactus(screen)
        cactuses.append(cactus)



def update_dino(dino):
    if dino.y < 130:
        dino.up = dino.up + dino.gravity * dino.t
        dino.y -= dino.up
        dino.t += 0.15

    if dino.y > 130:
        dino.y = 130
        dino.t = 0
        dino.up = 8
        #self.jump = False

def update_cactus(dino, cactuses, gamestats):
    for cactus in cactuses:
        cactus.move()
        if cactus.is_collisided(dino):
            print('hit')
            gamestats.gameactive = False
            sleep(0.5)
        if cactus.x < -20:
            cactuses.remove(cactus)


def update_screen(screen, settings, dino, ground, cactuses):
    screen.fill(settings.bg_color)
    dino.blitme()
    ground.blitme()
    for cactus in cactuses:
        cactus.blitme()
        pygame.draw.rect(screen, [3, 3, 3], [cactus.x+10, cactus.y+5, 50,65], 1)
    pygame.draw.rect(screen, [3, 3, 3], [dino.x + 30, dino.y +5, 45,65], 1)
    pygame.display.flip()
