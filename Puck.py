import pygame
import math
from pygame.locals import *

import random

def getAngle(x1, y1, x2, y2):
    yv = y2-y1
    xv = x1-x2
    if (xv==0):
        if (yv<0):
            return math.pi/2
        else:
            return 3/2*math.pi
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
    while (angle>=math.pi*2):
        angle -= math.pi*2
    return angle

def minDist(angle1, angle2):
    return min(calibrate(angle1-angle2), calibrate(angle2-angle1))

class Puck(pygame.sprite.Sprite):

    def __init__(self, img, top, left, bottom, right, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size,size))
        pygame.transform.scale(pygame.image.load(img).convert_alpha(), (size,size), self.image)
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
        angle = calibrate(getAngle(puckx, pucky, paddlex, paddley))
        reflect_angle = calibrate(angle-math.pi/2)
        opp_angle = calibrate(angle+math.pi/2)
        self.angle = calibrate(self.angle)
        paddle_angle = paddle.getAngle()
        if (paddlex==puckx):
            if (paddley<pucky):
                self.angle = 3/2*math.pi
            else:
                self.angle = math.pi/2
        elif (paddley==pucky):
            if (paddlex<puckx):
                self.angle = 0
            else:
                self.angle = math.pi
        elif (self.speed==0):
            self.angle = angle
        elif (minDist(self.angle, calibrate(paddle_angle))<math.pi/2):
            num = math.sin(self.angle)*self.speed-paddle.vy
            den = math.cos(self.angle)*self.speed+paddle.vx
            self.angle = abs(math.atan(num/den))
            if (num<0 and den<0):
                self.angle += math.pi
            elif (num<0):
                self.angle = 2*math.pi-self.angle
            elif (den<0):
                self.angle = math.pi-self.angle
        else:
            d1 = minDist(self.angle, reflect_angle)
            d2 = minDist(self.angle, opp_angle)
            if (d1<d2):
                if (self.angle==calibrate(reflect_angle+d1)):
                    self.angle = reflect_angle-d1;
                else:
                    self.angle = reflect_angle+d1
            else:
                if (self.angle==calibrate(opp_angle+d2)):
                    self.angle = opp_angle-d2
                else:
                    self.angle = opp_angle+d2
        self.speed += (paddle.vx**2+paddle.vy**2)**0.5
        self.speed = min(self.speed, 25)
        paddle.vx *= 0.9
        paddle.vy *= 0.9
        while (paddle.collide(self)):
                self.rect.move_ip(math.cos(self.angle)*self.speed, -math.sin(self.angle)*self.speed)
