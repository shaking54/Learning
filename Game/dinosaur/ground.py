import pygame

class Ground(object):
    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 180
        self.img = pygame.image.load('Images/ground.png')

    def blitme(self):
        self.screen.blit(self.img,(self.x,self.y))