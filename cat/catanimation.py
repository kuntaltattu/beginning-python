import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 10.0
frameTime = 1000/FPS
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400,300),pygame.DOUBLEBUF,32)
pygame.display.set_caption('Animation')

WHITE = (255,255,255)
catImg1 = pygame.image.load('cat.png')
catImg2 = pygame.image.load('cat2.png')
catx = 0
caty = 0
catHeight = catImg1.get_height()
catWidth = catImg1.get_width()
rotation = 180
showFirstCat = True
direction = 'right'

while True:
    DISPLAYSURF.fill(WHITE)
    if direction == 'right':
        catx += 5
        if catx >= 280:
            direction = 'down'
            rotation -= 90
            catx = 400 - catHeight
    elif direction == 'down':
        caty += 5
        if caty >= 300 - catWidth:
            direction = 'left'
            rotation -= 90
            caty = 300 - catHeight
            catx = 400 - catWidth
    elif direction == 'left':
        catx -= 5
        if catx <= 0:
            direction = 'up'
            rotation -= 90
            caty = 300 - catWidth
    elif direction == 'up':
        caty -= 5
        if caty <= 0:
            direction = 'right'
            rotation -= 90
    catImg = catImg1 if showFirstCat else catImg2
    catImg = pygame.transform.rotate(catImg, rotation)
    showFirstCat = not showFirstCat
    DISPLAYSURF.blit(catImg,(catx,caty))
    pygame.time.delay(int(frameTime))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


