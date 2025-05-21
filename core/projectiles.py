import pygame

class Projectile:
    def __init__(self, position, direction):
        # Projectile setup
        self.position = position
        self.direction = direction
        self.speed = 300
    
    def update(self, screen, delta_time):
        # Move the projectile
        self.position += self.direction * self.speed * delta_time

        # Draw the projectile
        pygame.draw.circle(screen, (255, 255, 20), (self.position.x, self.position.y), 5)
    
class Projectiles:
    def __init__(self):
        # Projectiles setup
        self.projectiles = []
    
    def create(self, position, direction):
        # Create new projectile
        projectile = Projectile(position.copy(), direction)
        
        # Add to projectiles
        self.projectiles.append(projectile)
    
    def update(self, screen, delta_time):
        # Update projectiles
        for i in self.projectiles:
            i.update(screen, delta_time)

            # Check if the projectile is off the screen
            if i.position.y < 0 or i.position.x < 0 or i.position.x > screen.get_width() or i.position.y > screen.get_height():
                self.projectiles.remove(i)