import pygame
from pygame.sprite import Sprite
class Cactus(Sprite):
    def __init__(self,screen):
        self.screen = screen
        self.x = 500
        self.y = 125
        self.img = pygame.image.load('Images/cactus.png')
        self.img = pygame.transform.scale(self.img,(65,70))
        self.rect = self.img.get_rect()
        self.speed = -5
        self.hithox = (self.x+10, self.y+5, 50,65)


    def move(self):
        self.x += self.speed

    def is_collisided(self, dino):
        return pygame.Rect.colliderect(pygame.Rect(self.x+10, self.y+5, 50,65),pygame.Rect(dino.x + 30, dino.y +5, 45,65))
    def blitme(self):
        self.screen.blit(self.img,(self.x,self.y))
        #pygame.draw.rect(self.screen, [0,0,0], [self.rect], width=0)