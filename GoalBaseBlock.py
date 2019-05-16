import pygame
from pygame.locals import *

class GoalBaseBlock(pygame.sprite.Sprite):

    def __init__(self, id, lt, tp, width):
        # Constructs the parent component
        pygame.sprite.Sprite.__init__(self)
        # Creates a goal
        self.image = pygame.Surface((11,width)).convert()
        # Colour of goal is black
        self.image.fill((0,0,0))
        # Determines the attributes of the goal as a rectangle
        self.rect = self.image.get_rect()

        # Sets the position of the goal
        self.lt = lt
        self.tp = tp
        self.width = width


    def get_rect(self):
        return pygame.Rect(self.lt, self.tp, 11, self.width)
