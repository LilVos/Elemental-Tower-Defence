import pygame
from constants import *

#initalize pygame
pygame.init()

# create clock FPS
clock = pygame.time.Clock()

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Elemental Tower Defence")

#load images

enemy_image = pygame.image.load("C:\Users\User\Desktop\PYTHON\Elemantal Tower Defense\Elemental-Tower-Defence\ASSESTS\images.jpeg").convert_alpha()

# game loop
run = True
while run:
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        #quit
        if event.type == pygame.QUIT:
            run = False

pygame.quit()