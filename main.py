import pygame
from constants import *
from enemy import *

# Initialize pygame
pygame.init()

# Create clock FPS
clock = pygame.time.Clock()

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Elemental Tower Defence")

# Load images
enemy_image = pygame.image.load(r"C:\\Users\\User\\Desktop\\PYTHON\\Elemantal Tower Defense\\Elemental-Tower-Defence\\ASSESTS\\images.png").convert_alpha()

# Create group
enemy_group = pygame.sprite.Group()

waypoints = [(100, 100), (400, 200), (400, 100), (200, 300), (300, 50)]

first_enemy = Enemy(waypoints, enemy_image)
enemy_group.add(first_enemy)

print(first_enemy)

# Game loop
run = True
while run:

    clock.tick(FPS)

    screen.fill("grey100")

    # Draw enemy path
    pygame.draw.lines(screen, "BLACK", False, waypoints)

    # Update and draw group
    enemy_group.update()  # This line was added
    enemy_group.draw(screen)

    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            run = False

    # Update Display
    pygame.display.flip()

pygame.quit()
