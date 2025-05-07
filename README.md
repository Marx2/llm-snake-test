# Python Snake Game

## Description
A classic implementation of the Snake game where the player controls a growing snake, trying to eat food items without colliding with walls or its own tail. The game difficulty increases as the snake gets longer.

## Features
*   Snake movement in four directions (Up, Down, Left, Right).
*   Snake grows in length after consuming food.
*   Randomly appearing food items.
*   Score tracking based on food consumed.
*   Game over condition on collision with boundaries or the snake's own body.
*   Simple, clear user interface.
*   Adjustable game speed/difficulty.

## Technologies Used
*   **Python 3.x**
*   **Pygame:** A cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries. We've chosen Pygame for its simplicity and suitability for 2D games like Snake, providing straightforward ways to handle graphics, event input, and the game loop.

## Setup and Installation

1.  **Clone the repository (Example):**
    ```bash
    git clone https://github.com/your-username/python-snake-game.git
    cd python-snake-game
    ```
    *(Replace the URL with your actual repository URL after creating it.)*

2.  **Create and Activate Virtual Environment:**
    It's highly recommended to use a virtual environment to manage project dependencies.
    *   Create the virtual environment:
        ```bash
        python -m venv venv
        ```
    *   Activate the virtual environment:
        *   **Windows:**
            ```bash
            .\venv\Scripts\activate
            ```
        *   **macOS/Linux:**
            ```bash
            source venv/bin/activate
            ```

3.  **Install Dependencies:**
    A [`requirements.txt`](./requirements.txt:1) file will list all necessary Python packages.
    ```bash
    pip install -r requirements.txt
    ```
    *(Initially, this file will contain `pygame`.)*

## How to Play

1.  Ensure you have completed the "Setup and Installation" steps, including activating the virtual environment.
2.  Run the game from the project's root directory:
    ```bash
    python snake/main.py
    ```
    *(Assuming the main game script is [`main.py`](./snake/main.py:1) inside a `snake` directory.)*
3.  Use the **arrow keys** (Up, Down, Left, Right) to control the snake's direction.
4.  The objective is to eat the food (typically a colored block) to score points and make the snake grow.
5.  Avoid running into the edges of the game window or the snake's own body.
6.  The game ends if a collision occurs. Press a designated key (e.g., 'R') to restart or 'Q' to quit.

## Development Plan / Implementation Steps

The development will be broken down into the following manageable tasks. Code will primarily reside in a `snake/` subdirectory.

1.  **Project Structure & Initial Setup:**
    *   Create the main project directory (e.g., `python-snake-game`).
    *   Inside it, create:
        *   A `snake/` subdirectory for game modules.
        *   This [`README.md`](./README.md:1) file at the root.
        *   A `.gitignore` file (e.g., to ignore `venv/`, `__pycache__/`, `*.pyc`).
    *   Set up and activate a virtual environment (see "Setup and Installation").
    *   Install Pygame: `pip install pygame`.
    *   Create [`requirements.txt`](./requirements.txt:1): `pip freeze > requirements.txt`.
    *   Create the main game script: [`snake/main.py`](./snake/main.py:1).
    *   Create module files: [`snake/snake_logic.py`](./snake/snake_logic.py:1) (for Snake class), [`snake/food.py`](./snake/food.py:1) (for Food class), and [`snake/config.py`](./snake/config.py:1) (for game settings).

2.  **Game Configuration ([`snake/config.py`](./snake/config.py:1)):**
    *   Define constants:
        *   Screen width and height (e.g., `SCREEN_WIDTH = 600`, `SCREEN_HEIGHT = 400`).
        *   Cell/Grid size (e.g., `CELL_SIZE = 20`).
        *   Colors (RGB tuples: `WHITE`, `BLACK`, `RED`, `GREEN`, `BLUE`).
        *   Game FPS (e.g., `FPS = 10`).
        *   Font settings for score/messages.

3.  **Pygame Initialization and Game Window ([`snake/main.py`](./snake/main.py:1)):**
    *   Import `pygame` and modules from `snake/config.py`.
    *   Initialize Pygame: `pygame.init()`.
    *   Set up the game display: `screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))`.
    *   Set window caption: `pygame.display.set_caption('Python Snake Game')`.
    *   Create a game clock: `clock = pygame.time.Clock()`.

4.  **Snake Class ([`snake/snake_logic.py`](./snake/snake_logic.py:1)):**
    *   `class Snake:`
        *   `__init__(self, start_x, start_y, cell_size, color)`:
            *   `self.cell_size = cell_size`
            *   `self.color = color`
            *   `self.body = [(start_x, start_y)]` (list of (col, row) tuples for grid cells)
            *   `self.direction = "RIGHT"` (or initial direction)
            *   `self.grow_pending = False`
        *   `move(self)`:
            *   Calculate new head position based on `self.direction`.
            *   Insert new head at the beginning of `self.body`.
            *   If `self.grow_pending` is `False`, remove the tail segment. Else, set `self.grow_pending = False`.
        *   `grow(self)`:
            *   Set `self.grow_pending = True`.
        *   `draw(self, surface)`:
            *   Iterate `self.body`, draw a `pygame.Rect` for each segment on `surface`.
        *   `change_direction(self, new_direction)`:
            *   Update `self.direction`, preventing opposite direction changes (e.g., can't go LEFT if current is RIGHT).
        *   `check_collision_self(self)`:
            *   Return `True` if the head collides with any other segment in `self.body[1:]`.
        *   `check_collision_walls(self, screen_width, screen_height)`:
            *   Return `True` if head is outside screen boundaries (considering `cell_size`).
        *   `get_head_position(self)`:
            *   Return `self.body[0]`.

5.  **Food Class ([`snake/food.py`](./snake/food.py:1)):**
    *   `class Food:`
        *   `__init__(self, screen_width, screen_height, cell_size, color, snake_body)`:
            *   `self.screen_width, self.screen_height, self.cell_size, self.color = ...`
            *   `self.position = self._generate_random_pos(snake_body)` (grid cell (col, row))
        *   `_generate_random_pos(self, snake_body)`:
            *   Generate random (col, row) within grid limits.
            *   Ensure it's not on any part of `snake_body`.
            *   Return the valid position.
        *   `spawn(self, snake_body)`:
            *   `self.position = self._generate_random_pos(snake_body)`.
        *   `draw(self, surface)`:
            *   Draw a `pygame.Rect` at `self.position` on `surface`.

6.  **Game Logic and Main Loop ([`snake/main.py`](./snake/main.py:1)):**
    *   **Helper Functions:**
        *   `display_text(surface, text, position, font, color)`: For score and messages.
        *   `game_over_screen(screen, score, config)`: Display game over message and final score. Wait for input to restart or quit.
    *   **Main Game Function (`run_game()`):**
        *   Initialize `Snake` and `Food` objects.
        *   `score = 0`
        *   `game_running = True`, `game_over = False`
        *   **Game Loop (`while game_running`):**
            *   **Event Handling (`for event in pygame.event.get()`):**
                *   `pygame.QUIT`: `game_running = False`.
                *   `pygame.KEYDOWN`:
                    *   Arrow keys: `snake.change_direction(...)`.
                    *   If `game_over`: 'R' to restart (call `run_game()` again or reset state), 'Q' to `game_running = False`.
            *   **If not `game_over`:**
                *   `snake.move()`
                *   **Collision Detection:**
                    *   Snake eats food: If `snake.get_head_position() == food.position`:
                        *   `snake.grow()`
                        *   `food.spawn(snake.body)`
                        *   `score += 1`
                    *   Snake hits wall: If `snake.check_collision_walls(...)`: `game_over = True`.
                    *   Snake hits self: If `snake.check_collision_self()`: `game_over = True`.
            *   **Drawing:**
                *   `screen.fill(config.BLACK)` (or background color).
                *   `snake.draw(screen)`.
                *   `food.draw(screen)`.
                *   `display_text(...)` for score.
                *   If `game_over`: `game_over_screen(...)`.
            *   `pygame.display.flip()` (or `update()`).
            *   `clock.tick(config.FPS)`.
    *   Call `run_game()` at the end of `main.py` (e.g., `if __name__ == "__main__": run_game()`).
    *   `pygame.quit()`.

7.  **Scoring and UI Elements:**
    *   Implement `display_text` function using `pygame.font.Font` and `render`.
    *   Display current score during gameplay.
    *   Display "Game Over" and final score when the game ends.

8.  **Restart and Quit Functionality:**
    *   In the game over state, provide options to restart (resetting game state: snake, food, score) or quit the application.

9.  **Refinements and Enhancements (Optional Future Steps):**
    *   Sound effects (eating, game over).
    *   Increasing difficulty (e.g., snake speed increases with score).
    *   Start menu with difficulty selection.
    *   High score persistence (saving to a file).
    *   Different food types with different points/effects.

This plan provides a structured approach to developing the Snake game. Each step builds upon the previous one, leading to a fully functional game.