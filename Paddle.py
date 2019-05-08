# Imports the pygame module
import pygame, math
# Imports all local functions from pygame.local 
from pygame.locals import *
# Initiates pygame
pygame.init()

# Controls that the players are going use to control the movement of the paddle
controls = [[K_UP, K_DOWN, K_LEFT, K_RIGHT], [K_w, K_s, K_a, K_d]]

class Paddle(pygame.sprite.Sprite):

    def __init__(self, img, id,  top, left, bottom, right, size):
        # Constructs the parent component
        pygame.sprite.Sprite.__init__(self)
        # Size of the image
        self.image = pygame.Surface((50, 50))
        # Makes the paddle a specific size and loads image of the paddle to the surface
        pygame.transform.scale(pygame.image.load(img).convert_alpha(), (50, 50), self.image)
        # Makes the background of the paddle transparent
        self.image.set_colorkey(self.image.get_at((0,0)))
        # Determines the attributes of the paddle
        self.rect = self.image.get_rect()
        # Determines the midpoint of the area that the paddle can move (starting point)
        self.rect.topleft = (((left+right)/2)-size/2), (((top+bottom)/2)-size/2)
        # Decides which set of controls is used
        self.id = id

        # Determines attributes of the paddle (barrier and velocity in x and y direction)
        self.xmin = left
        self.ymin = top
        self.xmax = right
        self.ymax = bottom
        self.vx = 0
        self.vy = 0

    def update(self, keys):

        # Accelerates the paddle if key is pressed
        # If up key or key 'w' is pressed depending on the index
        if keys[controls[self.id][0]]:
            # Paddle goes up
            self.vy -= 1.5
        # If down key or key 's' is pressed depending on the index
        if keys[controls[self.id][1]]:
            # Paddle goes down
            self.vy += 1.5
        # If left key or key 'a' is pressed depending on the index
        if keys[controls[self.id][2]]:
            # Paddle goes left
            self.vx -= 1.5
        # If right key or key 'd' is pressed depending on the index
        if keys[controls[self.id][3]]:
            # Paddle goes right
            self.vx += 1.5

        # Decelerates the paddle
        # If moving forward (horizontally)
        if self.vx>0:
            self.vx -= 0.5
        # If moving backward (horizontally)
        elif self.vx<0:
            self.vx += 0.5
        # If moving down (vertically)
        if self.vy>0:
            self.vy -= 0.5
        # If moving up (vertically)
        elif self.vy<0:
            self.vy += 0.5

        self.vx = min(self.vx, 20)
        self.vy = min(self.vy, 20)

        self.rect.move_ip(self.vx, self.vy)

        # Forms the barrier in which the paddle can move
        # If paddle hits the left barrier
        if self.rect.left<self.xmin:
            # Forms left barrier for each paddle
            self.rect.left = self.xmin
            # When paddle hits the left barrier it stops moving
            self.vx = 0
        # If paddle hits the right barrier
        elif self.rect.right>self.xmax:
            # Forms right barrier for each paddle
            self.rect.right = self.xmax
            # When paddle hits the right barrier it stops moving
            self.vx = 0

        # If paddle hits the top barrier
        if self.rect.top<self.ymin:
            # Forms the top barrier for each paddle
            self.rect.top = self.ymin
            # When paddle hits the top barrier its stops moving
            self.vy = 0
        # If paddle hits the bottom barrier
        elif self.rect.bottom>self.ymax:
            # Forms the bottom barrier for each paddle
            self.rect.bottom = self.ymax
            # When paddle hits the bottom barrier it stops moving
            self.vy = 0

    def getAngle(self):
        return math.atan2(-self.vy, self.vx)

    def collide(self, puck):
        paddlex = self.rect.centerx
        paddley = self.rect.centery
        puckx = puck.rect.centerx
        pucky = puck.rect.centery
        dist = ((paddlex-puckx)**2+(paddley-pucky)**2)**0.5
        paddleradius = (self.rect.width)/2
        puckradius = (puck.rect.width)/2
        if (dist<paddleradius+puckradius):
            return True
        else:
            return False
