import pygame
import random
import sys

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.CELL_SIZE = 20
        self.FPS = 10

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 24)

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.snake_dir = (self.CELL_SIZE, 0)
        self.food = self.spawn_food()
        self.score = 0

    def spawn_food(self):
        return (random.randint(0, (self.WINDOW_WIDTH - self.CELL_SIZE) // self.CELL_SIZE) * self.CELL_SIZE,
                random.randint(0, (self.WINDOW_HEIGHT - self.CELL_SIZE) // self.CELL_SIZE) * self.CELL_SIZE)

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, self.GREEN, pygame.Rect(segment[0], segment[1], self.CELL_SIZE, self.CELL_SIZE))

    def draw_food(self):
        pygame.draw.rect(self.screen, self.RED, pygame.Rect(self.food[0], self.food[1], self.CELL_SIZE, self.CELL_SIZE))

    def display_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, self.WHITE)
        self.screen.blit(score_text, (10, 10))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake_dir != (0, self.CELL_SIZE):
                    self.snake_dir = (0, -self.CELL_SIZE)
                elif event.key == pygame.K_DOWN and self.snake_dir != (0, -self.CELL_SIZE):
                    self.snake_dir = (0, self.CELL_SIZE)
                elif event.key == pygame.K_LEFT and self.snake_dir != (self.CELL_SIZE, 0):
                    self.snake_dir = (-self.CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and self.snake_dir != (-self.CELL_SIZE, 0):
                    self.snake_dir = (self.CELL_SIZE, 0)

    def move_snake(self):
        new_head = (self.snake[0][0] + self.snake_dir[0], self.snake[0][1] + self.snake_dir[1])
        self.snake = [new_head] + self.snake[:-1]
        return new_head

    def check_collisions(self, new_head):
        if (new_head[0] < 0 or new_head[0] >= self.WINDOW_WIDTH or
            new_head[1] < 0 or new_head[1] >= self.WINDOW_HEIGHT or
            new_head in self.snake[1:]):
            pygame.quit()
            sys.exit()

    def check_food_collision(self, new_head):
        if new_head == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.spawn_food()
            self.score += 1

    def run(self):
        while True:
            self.handle_events()
            new_head = self.move_snake()
            self.check_collisions(new_head)
            self.check_food_collision(new_head)

            self.screen.fill(self.BLACK)
            self.draw_snake()
            self.draw_food()
            self.display_score()
            pygame.display.flip()
            self.clock.tick(self.FPS)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()