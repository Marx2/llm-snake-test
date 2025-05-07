# Screen dimensions
SCREEN_WIDTH = 800  # Or 600, feel free to adjust
SCREEN_HEIGHT = 600 # Or 400, feel free to adjust

# Grid and Cell size
CELL_SIZE = 20 # Size of each snake segment and food item

# Colors (RGB tuples)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0) # For snake body
BLUE = (50, 153, 213)
LIGHT_GRAY = (200, 200, 200) # For grid lines
DARK_GRAY = (40, 40, 40)   # For background or alternative elements

# Game speed
FPS = 10  # Frames Per Second - controls snake speed initially

# Font settings
FONT_NAME = 'arial' # or None for default pygame font
SCORE_FONT_SIZE = 25
MESSAGE_FONT_SIZE = 30
GAME_OVER_FONT_SIZE = 50

# Directions (optional, but can make code more readable)
# Using tuples for changes in (dx, dy) or just string identifiers
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"