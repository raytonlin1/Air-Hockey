import pygame
import time
from Paddle import *
from Puck import *
from Goal import *
from pygame.locals import *
from Wall import *
# Initiates pygame.mixer to allow user to adjust the sound volume
pygame.mixer.init(frequency = 22050, size = -16, channels = 2, buffer = 1024)
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

font1 = pygame.font.SysFont("arial", 48)
font1.set_bold(True)
font2 = pygame.font.SysFont("arial", 24)
font2.set_bold(True)

#screen = pygame.display.set_mode((1000, 640))
screen = pygame.display.set_mode((1040, 700))
mainMenu = pygame.Surface((1040, 700))
mainMenu.fill((255, 255, 255))
pygame.draw.rect(mainMenu, (255, 0, 0), pygame.Rect(200, 200, 200, 200))
pygame.draw.rect(mainMenu, (0, 255, 0), pygame.Rect(600, 200, 200, 200))
rules = pygame.Surface((1040, 700))
rules.fill((255, 255, 255))
mainTitle = font1.render("MAIN MENU", True, (0,0,0))
rulesTitle = font1.render("RULES", True, (0,0,0))  
pygame.draw.rect(rules, (255, 0, 0), pygame.Rect(200, 200, 200, 200))
inMenu = True
inGame = False
inRules = False
p1 = Paddle("redpaddle.png", 1, 145, 55, 645, 520, 60)
p2 = Paddle("bluepaddle.png", 0, 145, 520, 645, 985, 60)
puck = Puck("puck.png", 100, 10, 690, 1030, 45)
# Initialize left goal width
width1 = 200
# Initialize right goal width
width2 = 200
# Create left goal
goal1 = Goal(-100, 55, 295, 495)
# Create right goal
goal2 = Goal(985, 1140, 295, 495)
# Initialize left goalSideBlock width
sideBlockWidth1 = 195
# Initialize rigth goalSideBlock width
sideBlockWidth2 = 195
leftWall = Wall(90, 700, 0, 55, (128, 128, 128))
rightWall = Wall(90, 700, 985, 1040, (128, 128, 128))
upWall = Wall(90, 145, 0, 1040, (128, 128, 128))
downWall = Wall(645, 700, 0, 1040, (128, 128, 128))
background = pygame.Surface(screen.get_size()).convert()
pygame.display.set_caption('Air Hockey')
background.fill((255, 255, 255))
clock = pygame.time.Clock()

keep_going = True

# Vertical border size
# recSize1 = (55,610)
# Horizontal border size
recSize2 = (1040,10)

# Initialize score for player 1
score1 = 0
# Initialize score for player 2
score2 = 0

# Number of increases of goal size
numIncrease1 = 0
numIncrease2 = 0

# Make 4 borders of air hockey table
# recSideLeft = pygame.Surface(recSize1).convert()
# recSideRight = pygame.Surface(recSize1).convert()
recSideTop = pygame.Surface(recSize2).convert()
recSideBottom = pygame.Surface(recSize2).convert()

while keep_going:
    clock.tick(60)
    if (inRules):
        for ev in pygame.event.get():
            if ev.type == QUIT:
                keep_going = False
            elif ev.type == MOUSEBUTTONDOWN:
                if (ev.pos[0]>=200 and ev.pos[0]<=400 and ev.pos[1]>=200 and ev.pos[1]<=400):
                    inRules = False
        screen.blit(rules, (0, 0))
        screen.blit(rulesTitle, (350, 100))
    elif (inMenu):
        for ev in pygame.event.get():
            if ev.type == QUIT:
                keep_going = False
            elif ev.type == MOUSEBUTTONDOWN:
                if (ev.pos[0]>=200 and ev.pos[0]<=400 and ev.pos[1]>=200 and ev.pos[1]<=400):
                    inMenu = False
                    inGame = True
                elif (ev.pos[0]>=600 and ev.pos[0]<=800 and ev.pos[1]>=200 and ev.pos[1]<=400):
                    inRules = True
        screen.blit(mainMenu, (0, 0))
        screen.blit(mainTitle, (350, 100))
    else:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                keep_going = False
        scoreLabel = font1.render((str(score2) + " : " + str(score1)), True, (0,0,255))
        keys = pygame.key.get_pressed()
        p1.update(keys, upWall, downWall)
        p2.update(keys, upWall, downWall)
        if (p1.collide(puck)):
            puck.bounce(p1)
        if (p2.collide(puck)):
            puck.bounce(p2)
        if (puck.rect.colliderect(goal1.rect)):
            goalMusic = pygame.mixer.Sound("goal.wav")
            goalMusic.play()
            puck = Puck("puck.png", 100, 10, 690, 1030, 45)
            p1 = Paddle("redpaddle.png", 1, 100, 55, 690, 520, 60)
            p2 = Paddle("bluepaddle.png", 0, 100, 520, 690, 985, 60)
            time.sleep(2)
        elif (puck.rect.colliderect(goal2.rect)):
            goalMusic = pygame.mixer.Sound("goal.wav")
            goalMusic.play()
            puck = Puck("puck.png", 100, 10, 690, 1030, 45)
            p1 = Paddle("redpaddle.png", 1, 100, 55, 690, 520, 60)
            p2 = Paddle("bluepaddle.png", 0, 100, 520, 690, 985, 60)
            time.sleep(2)

        puck.update(goal1, goal2, leftWall, rightWall, upWall, downWall)

        screen.blit(background, (0, 0))
        # Draw centre line of air hockey surface
        pygame.draw.line(screen, (255,0,0), (519,100), (519,690),5)
    
        # Draw circle at centre of air hockey surface
        pygame.draw.circle(screen, (255,0,0), (520, 395), 130)
        pygame.draw.circle(screen, (255,255,255), (520, 395), 125)

        # Draw semicircle at left goal
        pygame.draw.circle(screen, (255,0,0), (15, 395), 105+(numIncrease1*20))
        pygame.draw.circle(screen, (255,255,255), (15, 395), 100+(numIncrease1*20))

        # Draw semicircle at right goal
        pygame.draw.circle(screen, (255,0,0), (1025, 395), 105+(numIncrease2*20))
        pygame.draw.circle(screen, (255,255,255), (1025, 395), 100+(numIncrease2*20))
    
        screen.blit(p1.image, p1.rect)
        screen.blit(p2.image, p2.rect)

        screen.blit(leftWall.image, leftWall.rect)
        screen.blit(rightWall.image, rightWall.rect)
        screen.blit(upWall.image, upWall.rect)
        screen.blit(downWall.image, downWall.rect)

        screen.blit(goal1.image, goal1.rect)
        screen.blit(goal2.image, goal2.rect)

        screen.blit(puck.image, puck.rect)

        # Centre the output of the score on the screen
        if score2 < 10:
            screen.blit(scoreLabel, (472,40))
        elif score2 >= 10:
            screen.blit(scoreLabel, (446,40))

        # Output of text if the goal size reaches maximum size
        if width1 > 400:
            screen.blit(maxIncreaseLabel2, (30,60))
        if width2 > 400:
            screen.blit(maxIncreaseLabel1, (800,60))
    
    pygame.display.flip()
