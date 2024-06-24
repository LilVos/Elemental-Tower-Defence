import pygame
from pygame.math import Vector2


class Enemy(pygame.sprite.Sprite):
    def __init__(self, waypoints, image):
        pygame.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 1
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
    def enemy_move(self):
        
        #define a target waypoint
        self.target = Vector2(self.waypoints[self.target_waypoint])
        
        #move towards the target
        self.movement = self.target - self.pos
        
        #calculate distance to target
        distance_to_target = self.movement.length()
        
        #chek if distance is greater than step / speed
        if distance_to_target >= self.speed:
            self.pos += self.movement.normalize() * self.speed
            
        else:
            if distance_to_target != 0:
                self.pos += self.movement.normalize() * distance_to_target
            self.target_waypoint = self.target_waypoint + 1
            
        self.rect.center = self.pos