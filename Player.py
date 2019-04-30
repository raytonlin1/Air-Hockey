import pygame
from pygame.locals import *
pygame.init()

controls = [[K_UP, K_DOWN, K_LEFT, K_RIGHT], ["K_W", "K_S", "K_A", "K_D"]]

class Player(pygame.sprite.Sprite):

    def __init__(self, img, id,  top, left, bottom, right):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("small_ball.png")
        self.rect= self.image.get_rect()
        self.rect.topleft = ((left+right)/2, (top+bottom)/2)
        self.id = id
        self.xmin = left
        self.ymin = top 
        self.xmax = right
        self.ymax = bottom
        self.vx = 0
        self.vy = 0

    def update(self, keys):
        
        if keys[controls[self.id][0]]:
            self.vy -= 2
        if keys[controls[self.id][1]]:
            self.vy += 2
        if keys[controls[self.id][2]]:
            self.vx -= 2
        if keys[controls[self.id][3]]:
            self.vx += 2
        
        if self.vx>0:
            self.vx -= 1
        elif self.vx<0:
            self.vx += 1
        if self.vy>0:
            self.vy -= 1
        elif self.vy<0:
            self.vy += 1

        self.rect.move_ip(self.vx, self.vy)
        
        if self.rect.left<self.xmin:
            self.rect.left = self.xmin
            self.vx = 0
        elif self.rect.right>self.xmax:
            self.rect.right = self.xmax
            self.vx = 0

        if self.rect.top<self.ymin:
            self.rect.top = self.ymin
            self.vy = 0
        elif self.rect.bottom>self.ymax:
            self.rect.bottom = self.ymax
            self.vy = 0

        


        


