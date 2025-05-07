import pygame
import random
from . import config # Assuming config.py is in the snake directory

class Food:
    def __init__(self, screen_width, screen_height, cell_size, color=config.RED, snake_body=None):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.color = color
        # Initial spawn, ensuring it's not on the snake's body if provided
        self.position = self._generate_random_pos(snake_body if snake_body else []) 

    def _generate_random_pos(self, snake_body):
        while True:
            # Generate position in terms of grid cells
            col = random.randint(0, (self.screen_width // self.cell_size) - 1)
            row = random.randint(0, (self.screen_height // self.cell_size) - 1)
            pos = (col, row)
            if pos not in snake_body: # Ensure food doesn't spawn on the snake
                return pos

    def spawn(self, snake_body):
        # Re-spawn the food, ensuring it's not on the snake's body
        self.position = self._generate_random_pos(snake_body)

    def draw(self, surface):
        col, row = self.position
        rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(surface, self.color, rect)
        # Optional: draw a border for food
        # pygame.draw.rect(surface, config.WHITE, rect, 1)