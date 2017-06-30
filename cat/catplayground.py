import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 10.0
frameTime = 1000/FPS
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400,300),pygame.DOUBLEBUF,32)
pygame.display.set_caption('Animation')

WHITE = (255,255,255)
catImg1 = pygame.image.load('cat''.png')
catImg2 = pygame.image.load('cat2''.png')
stairs = pygame.image.load('staircase2.png')
catx = 0
caty = 0
catHeight = catImg1.get_height()
catWidth = catImg1.get_width()
rotation = 0
showFirstCat = True
direction = 'right'

while True:
    DISPLAYSURF.fill(WHITE)
    if direction == 'right':
        catImg1 = pygame.image.load('cat5''.png')
        catImg2 = pygame.image.load('cat6''.png')
        catx += 5
        caty += 2.5
        if catx >= 280:
            direction = 'left'
            rotation += 0
            catx = 350 - catHeight
            caty = 350 - catWidth
    elif direction == 'left':
        catImg1 = pygame.image.load('cat''.png')
        catImg2 = pygame.image.load('cat2''.png')
        catx -= 5
        if catx <= 0:
            direction = 'up'
            rotation -= 90
            caty = 300 - catWidth
    elif direction == 'up':
        catImg1 = pygame.image.load('cat''.png')
        catImg2 = pygame.image.load('cat2''.png')
        caty -= 5
        if caty <= 0:
            direction = 'right'
            rotation += 90
    catImg = catImg1 if showFirstCat else catImg2
    catImg = pygame.transform.rotate(catImg, rotation)
    showFirstCat = not showFirstCat
    DISPLAYSURF.blit(stairs,(5,10))
    DISPLAYSURF.blit(catImg,(catx,caty))
    pygame.time.delay(int(frameTime))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


