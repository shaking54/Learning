import pygame


class Dino(object):
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('Images/dino.jpg')
        #self.image = pygame.transform.scale(self.image, (100, 90))
        #self.jumping = False
        self.up = 8
        self.x = 40
        self.y = 130
        self.gravity = -0.25;
        self.t = 0
        self.hitbox = (self.x + 30, self.y +5, 45,65)


    def jump(self):
        self.y -= self.up
        #self.jumping = True


    def blitme(self):
        self.screen.blit(self.image, (self.x,self.y))