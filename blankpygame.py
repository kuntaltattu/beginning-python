import pygame,sys
from pygame.locals import*

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,350))
pygame.display.set_caption ("Hi fuckers!")
pygame.Color(200,100,188)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
