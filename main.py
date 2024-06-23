import pygame

#initalize pygame
pygame.init()

# create clock FPS
clock = pygame.time.Clock()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
FPS = 60

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# game loop
run = True
while run:
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        #quit
        if event.type == pygame.QUIT:
            run = False

pygame.quit()