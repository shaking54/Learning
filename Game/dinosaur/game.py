import pygame
from game_stat import Gamestats
from dino import Dino
from ground import Ground
from settings import Settings
from cactus import Cactus
import game_function as gf

FPS = 75

def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    settings = Settings()
    displaysurf = pygame.display.set_mode((settings.screen_width,settings.screen_height))

    dino = Dino(displaysurf)
    ground = Ground(displaysurf)
    gamestats = Gamestats()
    cactuses = []
    while True:
        gf.check_evect(dino, cactuses,displaysurf, gamestats)
        if gamestats.gameactive:
            clock.tick(FPS)
            gf.update_dino(dino)
            gf.update_cactus(dino, cactuses, gamestats)
            gf.update_screen(displaysurf, settings, dino,ground, cactuses)
        pygame.display.update()


run_game()