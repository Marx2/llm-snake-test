import pygame
import sys
from . import config
from .snake_logic import Snake # Import Snake class
from .food import Food       # Import Food class

# Helper function to display text
def display_text(surface, text, position, font_name, size, color):
    font = pygame.font.Font(pygame.font.match_font(font_name), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position) # Center the text
    surface.blit(text_surface, text_rect)

def game_over_screen(screen, score):
    screen.fill(config.BLACK)
    display_text(screen, "GAME OVER", 
                 (config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 - 50), 
                 config.FONT_NAME, config.GAME_OVER_FONT_SIZE, config.RED)
    display_text(screen, f"Final Score: {score}", 
                 (config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 10), 
                 config.FONT_NAME, config.MESSAGE_FONT_SIZE, config.WHITE)
    display_text(screen, "Press 'R' to Restart or 'Q' to Quit", 
                 (config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 70), 
                 config.FONT_NAME, config.SCORE_FONT_SIZE, config.WHITE)
    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    waiting_for_input = False # Will lead to main_game_loop() call
                    return True # Signal to restart
        pygame.time.Clock().tick(15) # Keep CPU usage low while waiting
    return False # Should not be reached if R or Q is pressed

def main_game_loop():
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption('Python Snake Game')
    clock = pygame.time.Clock()

    # Initial game state
    # Center of the screen, adjusted for grid
    start_col = (config.SCREEN_WIDTH // 2) // config.CELL_SIZE
    start_row = (config.SCREEN_HEIGHT // 2) // config.CELL_SIZE
    
    snake = Snake(start_col * config.CELL_SIZE, start_row * config.CELL_SIZE, config.CELL_SIZE)
    food = Food(config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.CELL_SIZE, snake_body=snake.body)
    
    score = 0
    game_over = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key == pygame.K_UP:
                        snake.change_direction(config.UP)
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction(config.DOWN)
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction(config.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction(config.RIGHT)
                # Handled by game_over_screen if game_over is True

        if not game_over:
            snake.move()

            # Collision Detection
            # Snake eats food
            if snake.get_head_position() == food.position:
                snake.grow()
                food.spawn(snake.body)
                score += 10 # Increase score

            # Snake hits wall
            if snake.check_collision_walls(config.SCREEN_WIDTH, config.SCREEN_HEIGHT):
                game_over = True

            # Snake hits self
            if snake.check_collision_self():
                game_over = True
        
        # Drawing
        screen.fill(config.BLACK)
        snake.draw(screen)
        food.draw(screen)
        
        # Display score
        display_text(screen, f"Score: {score}", 
                     (config.SCREEN_WIDTH - 70, 20), # Top-right corner
                     config.FONT_NAME, config.SCORE_FONT_SIZE, config.WHITE)

        if game_over:
            if game_over_screen(screen, score): # Returns True if 'R' is pressed
                # Reset game for restart
                game_over = False
                score = 0
                snake = Snake(start_col * config.CELL_SIZE, start_row * config.CELL_SIZE, config.CELL_SIZE)
                food = Food(config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.CELL_SIZE, snake_body=snake.body)
            else: # 'Q' was pressed or window closed in game_over_screen
                running = False


        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main_game_loop()