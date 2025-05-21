import pygame, math
from core.utils import *

class Player:
    def __init__(self, position, projectiles):
        # Player setup
        self.position = position
        self.projectiles = projectiles
        self.speed = 200

        # Animation setup
        self.animations = load_sprite_sheet("player", 26)
        self.animation = 2
        self.frame = 0
        self.time = 0
        self.animation_speed = 6
        self.flipped = False
        self.last_direction = pygame.Vector2(0, 0)
        self.last_animation = self.animation
    
    def animate(self, name):
        # Animation list
        animations = {
            "idle_back": 0,
            "idle_back_side": 1,
            "idle_front": 2,
            "idle_front_side": 3,
            "move_back": 4,
            "move_back_side": 5,
            "move_front": 6,
            "move_front_side": 7
        }

        # Set animation index
        self.animation = animations[name]
        
        # Set animation speed
        if name[:4] == "idle":
            self.animation_speed = 6
        else:
            self.animation_speed = 8

        # Reset frame count on new animation
        if self.last_animation != self.animation:
            self.frame = 0
            self.last_animation = self.animation
    
    def update(self, screen, delta_time, camera):
        # Movement
        direction = pygame.Vector2(0, 0)

        if get_input("left"):
            direction.x -= 1
            self.flipped = True
        elif get_input("right"):
            direction.x += 1
            self.flipped = False

        if get_input("up"):
            direction.y -= 1

            # Check which way to animate
            if direction.x == 0:
                self.animate("move_back")
            else:
                self.animate("move_back_side")
        elif get_input("down"):
            direction.y += 1

            # Check which way to animate
            if direction.x == 0:
                self.animate("move_front")
            else:
                self.animate("move_front_side")
        
        # Animate on the x axis only
        if direction.x != 0 and direction.y == 0:
            self.animate("move_front_side")

            if direction.x < 0:
                self.flipped = True
            elif direction.x > 0:
                self.flipped = False
        
        # Normalize the direction
        if direction.length() != 0:
            direction = direction.normalize()
            self.last_direction = direction
        else:
            # Set the correct idle animation
            if self.last_direction.x == 0:
                if self.last_direction.y < 0:
                    self.animate("idle_back")
                else:
                    self.animate("idle_front")
            else:
                if self.last_direction.y < 0:
                    self.animate("idle_back_side")
                else:
                    self.animate("idle_front_side")
        
        # Apply movement
        self.position += direction * self.speed * delta_time

        # Shooting
        if get_input("shoot"):
            # Get mouse direction from player
            mouse_direction = (pygame.Vector2(pygame.mouse.get_pos()) + camera.target)
            mouse_direction -= self.position

            if mouse_direction.length() != 0:
                mouse_direction = mouse_direction.normalize()
            
            # Spawn projectile in that direction
            self.projectiles.create(self.position, mouse_direction)
        
        # Animation loop
        self.time += delta_time

        if self.time >= 1 / self.animation_speed:
            self.time = 0
            self.frame = (self.frame + 1) % len(self.animations[self.animation])

        # Get position and frame
        position = camera.position_offset(self.position)
        frame = self.animations[self.animation][self.frame]

        # Flip image if needed
        if self.flipped:
            frame = pygame.transform.flip(frame, True, False)

        # Draw player
        screen.blit(frame, (position.x - (frame.get_width() / 2), position.y - (frame.get_height() / 2)))