import pygame
from constants import *
from enemy import *

#initalize pygame
pygame.init()

# create clock FPS
clock = pygame.time.Clock()

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Elemental Tower Defence")

#load images

enemy_image = pygame.image.load(r"C:\Users\User\Desktop\PYTHON\Elemantal Tower Defense\Elemental-Tower-Defence\ASSESTS\images.png").convert_alpha()

#create group

enemy_group = pygame.sprite.Group()

first_enemy = Enemy((200,300), enemy_image)
enemy_group.add(first_enemy)

print(first_enemy)

# game loop
run = True
while run:
    
    clock.tick(FPS)
    
    first_enemy.enemy_move()
    
    #draw group 
    enemy_group.draw(screen)
    
    for event in pygame.event.get():
        #quit
        if event.type == pygame.QUIT:
            run = False
            
    #Update Display
    pygame.display.flip()


pygame.quit()