import pygame
import random
from .constants import *

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.food = self.place_food()
        self.score = 0
        self.game_over = False

    def place_food(self):
        while True:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food not in self.snake:
                return food

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != (0, 1):
                    self.direction = (0, -1)
                elif event.key == pygame.K_DOWN and self.direction != (0, -1):
                    self.direction = (0, 1)
                elif event.key == pygame.K_LEFT and self.direction != (1, 0):
                    self.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                    self.direction = (1, 0)
        return True

    def update(self):
        if not self.game_over:
            head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
            if (head in self.snake or 
                head[0] < 0 or head[0] >= GRID_WIDTH or 
                head[1] < 0 or head[1] >= GRID_HEIGHT):
                self.game_over = True
                return

            self.snake.insert(0, head)
            if head == self.food:
                self.score += 1
                self.food = self.place_food()
            else:
                self.snake.pop()

    def draw(self):
        self.screen.fill(BLACK)
        for segment in self.snake:
            pygame.draw.rect(self.screen, GREEN, 
                           (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(self.screen, RED, 
                        (self.food[0] * GRID_SIZE, self.food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.display.update()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()