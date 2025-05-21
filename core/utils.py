import pygame, json

def get_input(action):
    # Get pressed keys
    keys = pygame.key.get_pressed()
    mouse_keys = pygame.mouse.get_pressed()

    # Load keybinds
    with open("core/keybinds.json", "r") as file:
        data = json.load(file)
    
    # Check if action was pressed
    if data[action] in ("left", "right", "middle"):
        mouse_map = {
            "left": 0,
            "middle": 1,
            "right": 2
        }

        if mouse_keys[mouse_map[data[action]]]:
            return True
    elif keys[pygame.key.key_code(data[action])]:
        return True

def load_sprite_sheet(name, frame_size):
    # Get sprite sheet
    sheet = pygame.image.load(f"assets/sprites/{name}.png").convert_alpha()

    # Load frames
    animations = []

    for i in range(sheet.get_height() // frame_size):
        # Get animation frames
        frames = []

        for v in range(sheet.get_width() // frame_size):
            # Get frame
            frame = sheet.subsurface(pygame.Rect(v * frame_size, i * frame_size, frame_size, frame_size))
            frame = pygame.transform.scale(frame, (frame.get_width() * 3, frame.get_height() * 3))

            # Check to see if the frame isn't blank
            if pygame.mask.from_surface(frame).count() > 0:
                frames.append(frame)
        
        animations.append(frames)

    return animations