import pygame
from . import config # Assuming config.py is in the snake directory

class Snake:
    def __init__(self, start_x, start_y, cell_size, color=config.DARK_GREEN, head_color=config.GREEN):
        self.cell_size = cell_size
        self.color = color
        self.head_color = head_color
        # Store body segments as pygame.Rect objects for easier drawing and collision
        # Or store as (column, row) grid coordinates if preferred, then convert for drawing
        # For now, let's use grid coordinates (col, row)
        self.body = [(start_x // cell_size, start_y // cell_size)] # List of (col, row) tuples
        self.direction = config.RIGHT # Initial direction
        self.grow_pending = False

    def move(self):
        curr_head_col, curr_head_row = self.body[0]
        
        if self.direction == config.UP:
            new_head = (curr_head_col, curr_head_row - 1)
        elif self.direction == config.DOWN:
            new_head = (curr_head_col, curr_head_row + 1)
        elif self.direction == config.LEFT:
            new_head = (curr_head_col - 1, curr_head_row)
        elif self.direction == config.RIGHT:
            new_head = (curr_head_col + 1, curr_head_row)
        else: # Should not happen
            return

        self.body.insert(0, new_head)

        if self.grow_pending:
            self.grow_pending = False
        else:
            self.body.pop()

    def grow(self):
        self.grow_pending = True

    def draw(self, surface):
        for i, segment_pos in enumerate(self.body):
            col, row = segment_pos
            rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
            segment_color = self.head_color if i == 0 else self.color # Head is a different color
            pygame.draw.rect(surface, segment_color, rect)
            # Optional: draw a border for segments
            # pygame.draw.rect(surface, config.BLACK, rect, 1) 


    def change_direction(self, new_direction):
        # Prevent moving directly opposite to current direction
        if new_direction == config.UP and self.direction != config.DOWN:
            self.direction = new_direction
        elif new_direction == config.DOWN and self.direction != config.UP:
            self.direction = new_direction
        elif new_direction == config.LEFT and self.direction != config.RIGHT:
            self.direction = new_direction
        elif new_direction == config.RIGHT and self.direction != config.LEFT:
            self.direction = new_direction

    def check_collision_self(self):
        head = self.get_head_position()
        # Check if the head collides with any other segment of the body
        return head in self.body[1:]

    def check_collision_walls(self, screen_width, screen_height):
        head_col, head_row = self.get_head_position()
        
        # Convert grid coordinates to pixel coordinates for wall check
        head_pixel_x = head_col * self.cell_size
        head_pixel_y = head_row * self.cell_size

        if head_pixel_x < 0 or head_pixel_x + self.cell_size > screen_width:
            return True
        if head_pixel_y < 0 or head_pixel_y + self.cell_size > screen_height:
            return True
        return False

    def get_head_position(self):
        return self.body[0] # Returns (col, row) of the head