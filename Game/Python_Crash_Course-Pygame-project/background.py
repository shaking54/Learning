import pygame
from pygame.sprite import Sprite

class Background(Sprite):
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)