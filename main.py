import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480

# Define block size
BLOCK_SIZE = 20

# Define snake speed
SNAKE_SPEED = 15


class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # Initial snake body
        self.direction = (20, 0)  # Initial direction (right)

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)

    def check_collision(self):
        head = self.body[0]
        if (
            head[0] < 0
            or head[0] >= SCREEN_WIDTH
            or head[1] < 0
            or head[1] >= SCREEN_HEIGHT
        ):
            return True
        for block in self.body[1:]:
            if head == block:
                return True
        return False


class Food:
    def __init__(self):
        self.position = (
            random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE),
            random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE),
        )

    def generate_new_food(self):
        self.position = (
            random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE),
            random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE),
        )


def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    snake = Snake()
    food = Food()
    food.generate_new_food()

    clock = pygame.time.Clock()
    game_over = False
    score = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.direction = (-BLOCK_SIZE, 0)
                if event.key == pygame.K_RIGHT:
                    snake.direction = (BLOCK_SIZE, 0)
                if event.key == pygame.K_UP:
                    snake.direction = (0, -BLOCK_SIZE)
                if event.key == pygame.K_DOWN:
                    snake.direction = (0, BLOCK_SIZE)

        if snake.check_collision():
            game_over = True

        snake.move()

        if snake.body[0] == food.position:
            snake.grow()
            food.generate_new_food()
            score += 1

        # Draw everything
        screen.fill(BLACK)
        for block in snake.body:
            pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])
        pygame.draw.rect(screen, RED, [food.position[0], food.position[1], BLOCK_SIZE, BLOCK_SIZE])

        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(SNAKE_SPEED)

    # Game Over Screen
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)

    pygame.display.flip()

    pygame.time.wait(2000)  # Wait for 2 seconds before quitting

    pygame.quit()


if __name__ == "__main__":
    game_loop()
