import pygame
import math
from pygame.locals import *

import random

class Puck(pygame.sprite.Sprite):

    def __init__(self, img, top, left, bottom, right):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        pygame.transform.scale(pygame.image.load(img).convert_alpha(), (30,30), self.image)
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (((left+right)/2)-15, ((top+bottom)/2)-15)
        self.xmin = left
        self.ymin = top
        self.xmax = right
        self.ymax = bottom
        self.vx = 0
        self.vy = 0

    def update(self):
        if (self.vx>0):
            self.vx -= 1
        elif (self.vx<0):
            self.vx += 1
        if (self.vy>0):
            self.vy -= 1
        elif (self.vy<0):
            self.vy += 1
        self.rect.move_ip(self.vx, self.vy)

        # Forms the barrier in which the paddle can move
        # If paddle hits the left barrier
        if self.rect.left<self.xmin:
            # Forms left barrier for each paddle
            self.rect.left = self.xmin
            # When paddle hits the left barrier it stops moving
            self.vx *= -1
        # If paddle hits the right barrier
        elif self.rect.right>self.xmax:
            # Forms right barrier for each paddle
            self.rect.right = self.xmax
            # When paddle hits the right barrier it stops moving
            self.vx *= -1

        # If paddle hits the top barrier
        if self.rect.top<self.ymin:
            # Forms the top barrier for each paddle
            self.rect.top = self.ymin
            # When paddle hits the top barrier its stops moving
            self.vy *= -1
        # If paddle hits the bottom barrier
        elif self.rect.bottom>self.ymax:
            # Forms the bottom barrier for each paddle
            self.rect.bottom = self.ymax
            # When paddle hits the bottom barrier it stops moving
            self.vy *= -1  
        
    def bounce(self, paddle):
        paddlex = (self.rect.left+self.rect.right)/2
        paddley = (self.rect.top+self.rect.bottom)/2
        puckx = (puck.rect.left+puck.rect.right)/2
        pucky = (puck.rect.top+puck.rect.bottom)/2
        slope = (paddley-pucky)/(paddlex-puckx)
        yint = paddley-slope*paddlex
        poix = 0
        poiy = 0
        ans = 1000
        if (paddlex<puckx):
            for x in range(paddlex, puckx, 0.1):
                y = slope*x+yint
                dist = ((paddlex-x)**2+(paddley-y)**2)**0.5
                if ((dist-paddle.rect.width/2)<ans):
                    ans = dist-paddle.rect.width/2
                    poix = x
                    poiy = y
        else:
            for x in range(paddlex, puckx, -0.1):
                y = slope*x+yint
                dist = ((paddlex-x)**2+(paddley-y)**2)**0.5
                if ((dist-paddle.rect.width/2)<ans):
                    ans = dist-paddle.rect.width/2
                    poix = x
                    poiy = y
        tangent = -1/slope
        angle = 180-abs(math.degrees(math.arctan(slope))-math.degrees(math.arctan(self.vy/self.vx))) 
        vlen = (self.vx**2+self.vy**2)**0.5
        length = (2*(vlen)**2-4*vlen*math.cos(math.radians(180-angle*2)))**0.5





