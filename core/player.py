import pygame
from core.utils import *

class Player:
    def __init__(self, position, projectiles):
        # Player setup
        self.position = position
        self.projectiles = projectiles
        self.speed = 250

        # Player sprite
        self.rect = pygame.Rect(self.position.x, self.position.y ,50, 50)
        self.rect.center = self.position
        self.color = (200, 20, 20)
    
    def update(self, screen, delta_time):
        # Movement handler
        direction = pygame.Vector2(0, 0)

        if get_input("left"):
            direction.x -= 1
        elif get_input("right"):
            direction.x += 1

        if get_input("up"):
            direction.y -= 1
        elif get_input("down"):
            direction.y += 1
        
        # Normalize the direction
        if direction.length() != 0:
            direction = direction.normalize()
        
        # Apply movement
        self.position += direction * self.speed * delta_time

        # Handle shooting
        if get_input("shoot"):
            # Get mouse direction from player
            mouse_direction = (pygame.Vector2(pygame.mouse.get_pos()) - self.position)

            if mouse_direction.length() != 0:
                mouse_direction = mouse_direction.normalize()
            
            # Spawn projectile in that direction
            self.projectiles.create(self.position, mouse_direction)

        # Draw player
        self.rect.center = self.position
        pygame.draw.rect(screen, self.color, self.rect)