import pygame, json, os

def get_input(action):
    # Get pressed keys
    keys = pygame.key.get_pressed()
    mouse_keys = pygame.mouse.get_pressed()

    # Load keybinds
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keybinds.json")

    with open(path, "r") as file:
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