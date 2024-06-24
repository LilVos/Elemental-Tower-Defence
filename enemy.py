import pygame
from pygame.math import Vector2
import math 


class Enemy(pygame.sprite.Sprite):
    def __init__(self, waypoints, image):
        pygame.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 5
        self.angle = 0
        self.original_image = image
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
    def update(self):
        self.enemy_move()
        self.rotate()
        self.rect.center = self.pos  # Update the rect's center to match the position
        
    def enemy_move(self):
        #define a target waypoint
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            #enemy rreached ened path
            self.kill()
            print("enemy killed")
        
        #calculate distance to target
        distance_to_target = self.movement.length()
        
        #chek if distance is greater than step / speed
        if distance_to_target >= self.speed:
            self.pos += self.movement.normalize() * self.speed
            
        else:
            if distance_to_target != 0:
                self.pos += self.movement.normalize() * distance_to_target
            self.target_waypoint = self.target_waypoint + 1
        
        
    def rotate(self):
        #calculate distance to next waypoint
        distance_to_target = self.target - self.pos
        #use Distance to calculate angle the enemy should look towards
        self.angle = math.degrees(math.atan2(-distance_to_target[1], distance_to_target[0]))
        #rotate image update rectangle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos