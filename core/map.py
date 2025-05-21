import pygame, pytmx

class Map:
    def __init__(self):
        # Map setup (for testing purposes)
        self.data = pytmx.load_pygame("assets/rooms/dev.tmx", pixelalpha=True)

    def update(self, screen, camera):
        # Loop through map layers/tiles
        for i in self.data.layers:
            for x, y, gid in i:
                # Create the tile
                tile = self.data.get_tile_image_by_gid(gid)

                if tile:
                    # Scale tile
                    tile = pygame.transform.scale(tile, (tile.get_width() * 3, tile.get_height() * 3))

                    # Draw the tile
                    screen.blit(tile, camera.position_offset(pygame.Vector2(x * self.data.tilewidth * 3, y * self.data.tileheight * 3)))