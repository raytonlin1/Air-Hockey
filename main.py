import pygame
import time
from Paddle import *
from Puck import *
from Goal import *
from GoalBaseBlock import *
from GoalSideBlock import *
from pygame.locals import *
# Initiates pygame.mixer to allow user to adjust the sound volume
pygame.mixer.init(frequency = 22050, size = -16, channels = 3, buffer = 1024)
#pygame.mixer.pre_init(44100, 16, 3, 4096)
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
puck = Puck("puck.png", 145, 10, 645, 1030, 45)
# Initialize left goal width, and left goalBaseBlock width
width1 = 200
# Initialize right goal width, and right goalBaseBlock width
width2 = 200
# Create left goal
goal1 = Goal(1, 0, 295, width1)
# Create right goal
goal2 = Goal(0, 985, 295, width2)
# Create left goalBaseBlock
goalBaseBlock1 = GoalBaseBlock(1, 0, 295, width1)
# Create right goalBaseBlock
goalBaseBlock2 = GoalBaseBlock(0, 1029, 295, width2)
# Initialize left goalSideBlock width
sideBlockWidth1 = 195
# Initialize rigth goalSideBlock width
sideBlockWidth2 = 195
# Create left upper goalSideBlock
goalSideBlockLU = GoalSideBlock(0, 0, 100, sideBlockWidth1)
# Create left lower goalSideBlock
goalSideBlockLL = GoalSideBlock(1, 0, 495, sideBlockWidth1)
# Create right upper goalSideBlock
goalSideBlockRU = GoalSideBlock(2, 985, 100, sideBlockWidth2)
# Create right lower goalSideBlock
goalSideBlockRL = GoalSideBlock(3, 985, 495, sideBlockWidth2)
background = pygame.Surface(screen.get_size()).convert()
pygame.display.set_caption('Air Hockey')
background.fill((255, 255, 255))
clock = pygame.time.Clock()

keep_going = True

# Vertical border size
# recSize1 = (55,610)
# Horizontal border size
recSize2 = (1040,55)

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

        scoreLabel = font1.render((str(score1) + " : " + str(score2)), True, (0,0,255))
        keys = pygame.key.get_pressed()
        p1.update(keys)
        p2.update(keys)
        if (p1.collide(puck)):
            puck.bounce(p1)
        if (p2.collide(puck)):
            puck.bounce(p2)
        
        # if (puck.rect.left < 11) and (puck.rect.top > 270-(numIncrease1*20) and puck.rect.top < 470+(numIncrease1*20)):
        if goalBaseBlock1.get_rect().colliderect(puck):
            pygame.mixer.Channel(0).play(pygame.mixer.Sound("goal.wav"))
            '''
            goalMusic = pygame.mixer.Sound("goal.wav")
            goalMusic.play()
            '''
            p1 = Paddle("redpaddle.png", 1, 145, 55, 645, 520, 60)
            p2 = Paddle("bluepaddle.png", 0, 145, 520, 645, 985, 60)
            puck = Puck("puck.png", 145, 10, 645, 1030, 45)
            if width1 < 401:
                width1 += 40
                sideBlockWidth1 -= 20
                numIncrease1 += 1
            maxIncreaseLabel2 = font2.render("Goal Size Maximum", True, (50,205,50))
            goal1 = Goal(1, 0, (100+((690-100)/2)-(width1/2)), width1)
            goalBaseBlock1 = GoalBaseBlock(1, 0,(100+((690-100)/2)-(width1/2)), width1)
            goalSideBlockLU = GoalSideBlock(0, 0, 100, sideBlockWidth1)
            goalSideBlockLL = GoalSideBlock(1, 0, (495 + numIncrease1*20), sideBlockWidth1)
            score2 += 1
            time.sleep(2)
            #print("Score Player 2:", score1)
        # elif (puck.rect.right > 1029) and (puck.rect.top > 270-(numIncrease2*20) and puck.rect.top < 470+(numIncrease2*20)):
        if goalBaseBlock2.get_rect().colliderect(puck):
            pygame.mixer.Channel(0).play(pygame.mixer.Sound("goal.wav"))
            '''
            goalSound = pygame.mixer.Sound("goal.wav")
            goalSound.play()
            '''
            p1 = Paddle("redpaddle.png", 1, 145, 55, 645, 520, 60)
            p2 = Paddle("bluepaddle.png", 0, 145, 520, 645, 985, 60)
            puck = Puck("puck.png", 145, 10, 645, 1030, 45)
            if width2 < 401:
                width2 += 40
                sideBlockWidth2 -= 20
                numIncrease2 += 1
            maxIncreaseLabel1 = font2.render("Goal Size Maximum", True, (50,205,50))
            goal2 = Goal(0, 985, (100+((690-100)/2)-(width2/2)), width2)
            goalBaseBlock2 = GoalBaseBlock(0, 1029,(100+((690-100)/2)-(width2/2)), width2)
            goalSideBlockRU = GoalSideBlock(2, 985, 100, sideBlockWidth2)
            goalSideBlockRL = GoalSideBlock(3, 985, (495 + numIncrease2*20), sideBlockWidth2)
            score1 += 1
            #print("Score Player 1:", score2)
            time.sleep(2)
        
        # Colour all 4 borders brown
        # recSideLeft.fill((138,54,15))
        # recSideRight.fill((138,54,15))
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
        pygame.draw.circle(screen, (255,0,0), (15, 395), 105+(numIncrease1*20))
        pygame.draw.circle(screen, (255,255,255), (15, 395), 100+(numIncrease1*20))

        # Draw semicircle at right goal
        pygame.draw.circle(screen, (255,0,0), (1025, 395), 105+(numIncrease2*20))
        pygame.draw.circle(screen, (255,255,255), (1025, 395), 100+(numIncrease2*20))
        
        screen.blit(p1.image, p1.rect)
        screen.blit(p2.image, p2.rect)
        screen.blit(puck.image, puck.rect)
        # screen.blit(recSideLeft, (0,100))
        # screen.blit(recSideRight, (985,100))
        screen.blit(recSideTop, (0,90))
        screen.blit(recSideBottom, (0,645))

        screen.blit(goal1.image, goal1.rect)
        screen.blit(goal2.image, goal2.rect)

        screen.blit(goalSideBlockLU.image, goalSideBlockLU.rect)
        screen.blit(goalSideBlockLL.image, goalSideBlockLL.rect)
        screen.blit(goalSideBlockRU.image, goalSideBlockRU.rect)
        screen.blit(goalSideBlockRL.image, goalSideBlockRL.rect)
        
        # Centre the output of the score on the screen
        if score1 < 10:
            screen.blit(scoreLabel, (472,40))
        elif score1 >= 10:
            screen.blit(scoreLabel, (446,40))

        # Output of text if the goal size reaches maximum size
        if width1 > 400:
            screen.blit(maxIncreaseLabel2, (30,60))
        if width2 > 400:
            screen.blit(maxIncreaseLabel1, (800,60))
    
    pygame.display.flip()
