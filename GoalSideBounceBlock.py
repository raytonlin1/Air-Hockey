import pygame
from pygame.locals import *

class GoalSideBounceBlock(pygame.sprite.Sprite):

    def __init__(self, id, lt, tp, width):
        # Constructs the parent component
        pygame.sprite.Sprite.__init__(self)
        # Creates a goalSideBounceBlock
        self.image = pygame.Surface((55,width)).convert()
        # Colour of goalSideBounceBlock is brown
        self.image.fill((138, 54, 15))
        # Determines the attributes of the goal as a rectangle
        self.rect = self.image.get_rect()

        # Sets the position of the goal
        self.lt = lt
        self.tp = tp
        self.width = width


    def get_rect(self):
        return pygame.Rect(self.lt, self.tp, 55, self.width)
