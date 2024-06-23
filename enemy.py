import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        
    def enemy_move(self):
        self.rect.x = self.rect.x + 1