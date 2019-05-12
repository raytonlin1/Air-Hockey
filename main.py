import pygame
import time
from Paddle import *
from Puck import *
from Goal import *
from pygame.locals import *
# Initiates pygame.mixer to allow user to adjust the sound volume
pygame.mixer.init(frequency = 22050, size = -16, channels = 2, buffer = 1024)
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

#screen = pygame.display.set_mode((1000, 640))
screen = pygame.display.set_mode((1040, 700))
p1 = Paddle("redpaddle.png", 1, 100, 10, 690, 520, 60)
p2 = Paddle("bluepaddle.png", 0, 100, 520, 690, 1030, 60)
puck = Puck("puck.png", 100, 10, 690, 1030, 45)
# Initialize left goal width
width1 = 200
# Initialize right goal width
width2 = 200
goal1 = Goal(1, 0, 300, width1)
goal2 = Goal(0, 1010, 300, width2)
background = pygame.Surface(screen.get_size()).convert()
pygame.display.set_caption('Air Hockey')
background.fill((255, 255, 255))
clock = pygame.time.Clock()

keep_going = True

# Horizontal border size
recSize1 = (10,610)
# Vertical border size
recSize2 = (1040,10)

# Initialize score for player 1
score1 = 0
# Initialize score for player 2
score2 = 0

# Number of increases of goal size
numIncrease1 = 0
numIncrease2 = 0

# Make 4 borders of air hockey table
recSideLeft = pygame.Surface(recSize1).convert()
recSideRight = pygame.Surface(recSize1).convert()
recSideTop = pygame.Surface(recSize2).convert()
recSideBottom = pygame.Surface(recSize2).convert()

while keep_going:
    clock.tick(60)
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
    keys = pygame.key.get_pressed()
    p1.update(keys)
    p2.update(keys)
    if (p1.collide(puck)):
        puck.bounce(p1)
    if (p2.collide(puck)):
        puck.bounce(p2)

    if (puck.rect.left < 11) and (puck.rect.top > 270-(numIncrease1*20) and puck.rect.top < 470+(numIncrease1*20)):
        goalMusic = pygame.mixer.Sound("goal.wav")
        goalMusic.play()
        puck = Puck("puck.png", 100, 10, 690, 1030, 45)
        p1 = Paddle("redpaddle.png", 1, 100, 10, 690, 520, 60)
        p2 = Paddle("bluepaddle.png", 0, 100, 520, 690, 1030, 60)
        if width1 < 401:
            width1 += 40
            numIncrease1 += 1
        goal1 = Goal(1, 0, (100+((700-100)/2)-(width1/2)), width1)
        score1 += 1
        time.sleep(2)
        print("Score Player 2:", score1)
    elif (puck.rect.right > 1029) and (puck.rect.top > 270-(numIncrease2*20) and puck.rect.top < 470+(numIncrease2*20)):
        goalSound = pygame.mixer.Sound("goal.wav")
        goalSound.play()
        puck = Puck("puck.png", 100, 10, 690, 1030, 45)
        p1 = Paddle("redpaddle.png", 1, 100, 10, 690, 520, 60)
        p2 = Paddle("bluepaddle.png", 0, 100, 520, 690, 1030, 60)
        if width2 < 401:
            width2 += 40
            numIncrease2 += 1
        goal2 = Goal(0, 1010, (100+((700-100)/2)-(width2/2)), width2)
        score2 += 1
        print("Score Player 1:", score2)
        time.sleep(2)
    
    # Colour all 4 borders brown
    recSideLeft.fill((138,54,15))
    recSideRight.fill((138,54,15))
    recSideTop.fill((138,54,15))
    recSideBottom.fill((138,54,15))

    puck.update()

    screen.blit(background, (0, 0))
    # Draw centre line of air hockey surface
    pygame.draw.line(screen, (255,0,0), (519,100), (519,690),5)
    
    # Draw circle at centre of air hockey surface
    pygame.draw.circle(screen, (255,0,0), (520, 395), 130)
    pygame.draw.circle(screen, (255,255,255), (520, 395), 125)

    # Draw semicircle at left goal
    pygame.draw.circle(screen, (255,0,0), (15, 400), 105+(numIncrease1*20))
    pygame.draw.circle(screen, (255,255,255), (15, 400), 100+(numIncrease1*20))

    # Draw semicircle at right goal
    pygame.draw.circle(screen, (255,0,0), (1025, 400), 105+(numIncrease2*20))
    pygame.draw.circle(screen, (255,255,255), (1025, 400), 100+(numIncrease2*20))

    
    screen.blit(p1.image, p1.rect)
    screen.blit(p2.image, p2.rect)
    screen.blit(puck.image, puck.rect)
    screen.blit(recSideLeft, (0,100))
    screen.blit(recSideRight, (1030,100))
    screen.blit(recSideTop, (0,90))
    screen.blit(recSideBottom, (0,690))

    screen.blit(goal1.image, goal1.rect)
    screen.blit(goal2.image, goal2.rect)

    pygame.display.flip()
