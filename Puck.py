import pygame
import math
from pygame.locals import *

import random

def getAngle(x1, y1, x2, y2):
    yv = y2-y1
    xv = x1-x2
    angle = 0
    if (xv>0):
        if (yv>0):
            angle = math.atan(yv/xv)
        else:
            angle = math.pi*2+math.atan(yv/xv)
    else:
        if (yv>0):
            angle = math.pi+math.atan(yv/xv)
        else:
            angle = math.pi+math.atan(yv/xv)
    return angle

def calibrate(angle):
    while (angle<0):
        angle += math.pi*2
    while (angle>math.pi*2):
        angle -= math.pi*2
    return angle

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
        if (self.speed>0.5):
            self.speed -= 0.5
        elif (self.speed>0.5):
            self.speed += 0.5
        else:
            self.speed = 0
        self.rect.move_ip(math.cos(self.angle)*self.speed, -math.sin(self.angle)*self.speed)
        self.angle = calibrate(self.angle)
        if self.rect.left<self.xmin:
            self.rect.left = self.xmin
            if (self.angle<math.pi):
                self.angle = math.pi-self.angle
            else:
                self.angle = math.pi*2-self.angle-math.pi
        elif self.rect.right>self.xmax:
            self.rect.right = self.xmax
            if (self.angle<math.pi/2):
                self.angle = math.pi-self.angle
            else:
                self.angle = math.pi*2-self.angle+math.pi
        if self.rect.top<self.ymin:
            self.rect.top = self.ymin
            if (self.angle<math.pi/2):
                self.angle = math.pi*2-self.angle
            else:
                self.angle = math.pi-self.angle+math.pi
        elif self.rect.bottom>self.ymax:
            self.rect.bottom = self.ymax
            if (self.angle<3/2*math.pi):
                self.angle = 2*math.pi-self.angle
            else:
                self.angle = math.pi*2-self.angle
        while (self.rect.left<self.xmin or self.rect.right>self.xmax or self.rect.top<self.ymin or self.rect.bottom>self.ymax):
            self.rect.move_ip(math.cos(self.angle)*self.speed, -math.sin(self.angle)*self.speed)
        
    def bounce(self, paddle):
        paddlex = (paddle.rect.left+paddle.rect.right)/2
        paddley = (paddle.rect.top+paddle.rect.bottom)/2
        puckx = (self.rect.left+self.rect.right)/2
        pucky = (self.rect.top+self.rect.bottom)/2
        try:
            paddle_angle = getAngle(paddlex, paddley, puckx, pucky)
            reflect_angle = calibrate(paddle_angle+math.pi/2)
            opp_angle = calibrate(paddle_angle-math.pi/2)
            if (self.speed==0):
                self.angle = paddle_angle+math.pi
            else:
                self.angle = calibrate(self.angle)
                reflect_angle = calibrate(reflect_angle)
                opp_angle = calibrate(opp_angle)
                diff = min(min(abs(reflect_angle-self.angle), abs(reflect_angle-self.angle+360)), min(abs(opp_angle-self.angle), abs(opp_angle-self.angle+360)))
                d1 = min(abs(self.angle-reflect_angle), abs(self.angle-reflect_angle+360))
                d2 = min(abs(self.angle-opp_angle), abs(self.angle-opp_angle+360))
                if (d1<d2):
                    if (calibrate(self.angle)==calibrate(opp_angle+diff)):
                        self.angle = opp_angle-diff;
                    else:
                        self.angle = opp_angle+diff
                else:
                    print(reflect_angle)
                    print(calibrate(self.angle+math.pi))
                    print(calibrate(reflect_angle+diff))
                    if (calibrate(self.angle)==calibrate(reflect_angle+diff)):
                        self.angle = reflect_angle-diff
                    else:
                        self.angle = reflect_angle+diff
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
                self.rect.move_ip(math.cos(self.angle)*self.speed, -math.sin(self.angle)*self.speed)



