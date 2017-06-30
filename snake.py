import pygame,sys
from pygame.locals import *

pygame.init()

FPS = 10
frametime = 1000/FPS
fpsClock = pygame.time.Clock ()

DISPLAYSURF = pygame.display.set_mode((700,500),pygame.DOUBLEBUF, 32)
DISPLAYSURF = pygame.display.set_caption ('Snakes!')
snakeImg = pygame.image.load ('snake.png')
WHITE = (255,255,255)
snakeht = pygame.image.get_height (snakeImg)
snakewd = pygame.image.get_width (snakeImg)
froght = pygame.image.get_height (frogImg)
frogwd = pyagem.image.get_width (frogImg)
rotation = 0
direction = 'right'
snakex = 0
snakey = 500

while True:
	DISPLAYSURF.fill (WHITE)
	if direction == 'right':
		if snakex <= 700:
			snakex += 5
			direction = 'left'
	elif direction == 'left':
		if snakex >= 0:
			snakex -= 5
	DISPLAYSURF.blit (snakeImg, (snakex, snakey))
	for event in pygame.event.get():
                if event.type() == QUIT:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()




        
