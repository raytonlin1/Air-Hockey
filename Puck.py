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
        self.angle = 0
        self.speed = 0

    def update(self):
        if (self.speed>0):
            self.speed -= 0.2
        elif (self.speed>0):
            self.speed += 0.2
        self.rect.move_ip(math.sin(self.angle)*self.speed, -math.cos(self.angle)*self.speed)

        # Forms the barrier in which the paddle can move
        # If paddle hits the left barrier
        if self.rect.left<self.xmin:
            # Forms left barrier for each paddle
            self.rect.left = self.xmin
            # When paddle hits the left barrier it stops moving
            self.angle = 2*math.pi-self.angle
        # If paddle hits the right barrier
        elif self.rect.right>self.xmax:
            # Forms right barrier for each paddle
            self.rect.right = self.xmax
            # When paddle hits the right barrier it stops moving
            self.angle = 3/2*math.pi-self.angle+math.pi/2

        # If paddle hits the top barrier
        if self.rect.top<self.ymin:
            # Forms the top barrier for each paddle
            self.rect.top = self.ymin
            # When paddle hits the top barrier its stops moving
            self.angle = 2*math.pi-self.angle+math.pi
        # If paddle hits the bottom barrier
        elif self.rect.bottom>self.ymax:
            # Forms the bottom barrier for each paddle
            self.rect.bottom = self.ymax
            # When paddle hits the bottom barrier it stops moving
            self.angle = math.pi-self.angle
        
    def bounce(self, paddle):
        paddlex = (paddle.rect.left+paddle.rect.right)/2
        paddley = (paddle.rect.top+paddle.rect.bottom)/2
        puckx = (self.rect.left+self.rect.right)/2
        pucky = (self.rect.top+self.rect.bottom)/2
        try:
            reflect_angle = math.atan(((paddley-pucky)/(paddlex-puckx)))
            opp_angle = math.pi+reflect_angle
            diff = min(abs(reflect_angle-self.angle), abs(opp_angle-self.angle))
            rotate = math.pi-diff*2
            self.angle += rotate
            '''
            print(reflect_angle)
            print(opp_angle)
            print(diff)
            print(self.angle)
            fad = input()
            '''
        except:
            if (paddlex==puckx):
                if (paddlex<puckx):
                    self.angle = 0
                else:
                    self.angle = math.pi/2
            else:
                if (paddley<pucky):
                    self.angle = 3/2*math.pi
                else:
                    self.angle = math.pi/2
        self.speed += (paddle.vx**2+paddle.vy**2)**0.5
        while (paddle.collide(self)):
                self.rect.move_ip(math.sin(self.angle)*self.speed, -math.cos(self.angle)*self.speed)



