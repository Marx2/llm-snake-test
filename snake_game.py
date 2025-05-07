import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH//2, GRID_HEIGHT//2)]
        self.direction = (0, 1)
    
    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        # Check wall collision
        if new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
            return False
        # Check self collision
        if new_head in self.body[1:]:
            return False
        self.body.insert(0, new_head)
        self.body.pop()
        return True
    
    def change_direction(self, new_direction):
        # Prevent reversing direction
        if (self.direction[0] * -1, self.direction[1] * -1) != new_direction:
            self.direction = new_direction

class Food:
    def __init__(self):
        self.position = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
    
    def respawn(self):
        self.position = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))

class Board:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
    
    def update(self):
        if not self.snake.move():
            return False
        if self.snake.body[0] == self.food.position:
            self.snake.body.append(self.snake.body[-1])
            self.food.respawn()
            self.score += 1
        return True

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    
    board = Board()
    
    running = True
    paused = False
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    board.snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    board.snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    board.snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    board.snake.change_direction((1, 0))
                elif event.key == pygame.K_p:
                    paused = not paused
        
        if not paused:
            board.update()
        
        screen.fill(WHITE)
        # Draw snake
        for segment in board.snake.body:
            pygame.draw.rect(screen, GREEN, (segment[0]*GRID_SIZE, segment[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))
        # Draw food
        pygame.draw.rect(screen, RED, (board.food.position[0]*GRID_SIZE, board.food.position[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))
        # Draw score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {board.score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()