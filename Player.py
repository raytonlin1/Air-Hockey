import pygame
from pygame.locals import *
pygame.init()

controls = [["K_UP", "K_DOWN", "K_LEFT", "K_RIGHT"], ["K_W", "K_S", "K_A", "K_D"]]

class Player(pygame.sprite.Sprite):

    def __init__(self, img, id,  top, left, bottom, right, col):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("small_ball.png")
        self.rect= self.image.get_rect()
        self.rect.topleft = ((left+right)/2, (top+bottom)/2)
        self.id = id
        self.xmin = left
        self.ymin = top 
        self.xmax = right
        self.ymax = bottom
        self.colour = col
        self.vx = 0
        self.vy = 0

    def update(ev):
        if ev[self.id][0]:
            self.vy -= 1
        if ev[self.id][1]:
            self.vy += 1
        if ev[self.id][2]:
            self.vx -= 1
        if ev[self.id][3]:
            self.vx += 1
        
        self.posx += self.vx
        self.posy += self.vy
        
        if self.left<self.xmin:
            self.left = self.xmin
            self.vx = 0
        elif self.right>self.xmax:
            self.right = self.xmax
            self.vx = 0

        if self.top<self.ymin:
            self.top = self.ymin
            self.vy = 0
        elif self.bottom>self.ymax:
            self.bottom = self.ymax
            self.vy = 0

        


        


