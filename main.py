import pygame, sys
from core.player import Player
from core.projectiles import Projectiles

class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Pygame setup
        self.screen = pygame.display.set_mode((1000, 600))
        self.uptime = pygame.time.Clock()
        pygame.display.set_caption("Gun Run")

        # Initialize projectiles
        self.projectiles = Projectiles()

        # Initialize player
        self.player = Player(pygame.Vector2(self.screen.get_width() // 2, self.screen.get_height() // 2), self.projectiles)
    
    def run(self):
        while True:
            # Close game when user ends window process
            for i in pygame.event.get():
                if i.type == pygame.QUIT or (i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
            
            # Reset background
            self.screen.fill((20, 20, 20))

            # Calculate delta time
            delta_time = self.uptime.tick(60) / 1000

            # Update classes
            self.projectiles.update(self.screen, delta_time)
            self.player.update(self.screen, delta_time)

            # Update screen
            pygame.display.flip()

# Run the game
if __name__ == "__main__":
    Game().run()