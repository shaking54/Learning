import pygame
from pygame.sprite import  Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreborad
from button import Button
from ship import Ship
from background import Background
import game_functions as gf


def run_game():
    #initalize pygame,settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    #make the play button
    play_button = Button(ai_settings, screen, "Play")

    #create an instance to store game stactistics and create a scoreboard
    stats = GameStats(ai_settings,)
    sb = Scoreborad(ai_settings, screen, stats)

    #Make a background
    #background = Background(screen)

    #make a ship, group of bullets, group of aliens
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    #create a fleet of aliens
    gf.create_fleet(ai_settings, screen,ship, aliens)

    #start for main loop for the q
    while True:

        #watch for keyboard and mouse event
        gf.check_events(ai_settings, screen, stats, sb,play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()

