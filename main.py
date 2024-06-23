import pygame

#initalize pygame
pygame.init()

# create clock FPS
clock = pygame.time.Clock()


#create game window
screen = pygame.display.set_mode((800,600))

# game loop
run = True
while run:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        #quit
        if event.type == pygame.QUIT:
            run = False

pygame.quit()