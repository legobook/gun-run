import pygame

class Camera:
    def __init__(self, player):
        # Camera setup
        self.offset = pygame.Vector2(0, 0)
        self.target = pygame.Vector2(0, 0)
        self.player = player
    
    def update(self, screen):
        # Screen center
        center = pygame.Vector2(screen.get_size()) / 2

        # Calculate offsets
        offset = (pygame.Vector2(pygame.mouse.get_pos()) - center) * 0.2
        self.target = self.player.position - center + offset

        # Smoothly move camera
        self.offset += (self.target - self.offset) * 0.1
    
    def position_offset(self, position):
        # Apply the offset to position
        return position - self.offset
    
    def rect_offset(self, rect):
        # Apply the offset to rect object
        return rect.move(-self.offset.x, -self.offset.y)