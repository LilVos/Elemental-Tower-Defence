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

waypoints = [(100,100),(400,200),(400,100),(200,300),(700,700)]

first_enemy = Enemy(waypoints, enemy_image)
enemy_group.add(first_enemy)

print(first_enemy)

# game loop
run = True
while run:
    
    clock.tick(FPS)
    
    screen.fill("grey100")
    
    #draw enemy path
    
    pygame.draw.lines(screen, "BLACK", False, waypoints)
    
    for first_enemy in enemy_group:
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