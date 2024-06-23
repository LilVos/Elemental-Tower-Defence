import pygame

#initalize pygame
pygame.init()


#create game window
screen = pygame.display.set_mode((800,600))

# game loop
run = True
while run:
    
    for event in pygame.event.get():
        #quit
        if event.type == pygame.QUIT:
            run = False

pygame.quit()