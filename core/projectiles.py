import pygame

class Projectile:
    def __init__(self, position, direction):
        # Projectile setup
        self.position = position
        self.direction = direction
        self.speed = 300
    
    def update(self, screen, delta_time, camera):
        # Move the projectile
        self.position += self.direction * self.speed * delta_time
        offset = camera.position_offset(self.position)

        # Draw the projectile
        pygame.draw.circle(screen, (255, 255, 20), (offset.x, offset.y), 5)
    
class Projectiles:
    def __init__(self):
        # Projectiles setup
        self.projectiles = []
    
    def create(self, position, direction):
        # Create new projectile
        projectile = Projectile(position.copy(), direction)
        
        # Add to projectiles
        self.projectiles.append(projectile)
    
    def update(self, screen, delta_time, camera):
        # Update projectiles
        for i in self.projectiles:
            i.update(screen, delta_time, camera)