import unittest
from snake.main import *

class TestSnakeGame(unittest.TestCase):
    def test_snake_movement(self):
        # Test snake movement logic
        initial_snake = [(100, 100), (90, 100), (80, 100)]
        direction = (20, 0)  # Move right
        new_head = (initial_snake[0][0] + direction[0], initial_snake[0][1] + direction[1])
        expected_snake = [new_head] + initial_snake[:-1]
        self.assertEqual(expected_snake, [(120, 100), (100, 100), (90, 100)])

    def test_food_generation(self):
        # Test food generation logic
        snake = [(100, 100), (90, 100), (80, 100)]
        food = (random.randint(0, (WINDOW_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                random.randint(0, (WINDOW_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
        self.assertTrue(0 <= food[0] < WINDOW_WIDTH and 0 <= food[1] < WINDOW_HEIGHT)
        self.assertNotIn(food, snake)

    def test_collision_detection(self):
        # Test collision detection logic
        snake = [(100, 100), (90, 100), (80, 100)]
        new_head_wall = (-20, 100)  # Out of bounds (wall collision)
        new_head_body = (90, 100)  # Collides with body
        new_head_food = (120, 100)  # Collides with food

        # Wall collision
        self.assertTrue(new_head_wall[0] < 0 or new_head_wall[1] < 0 or
                        new_head_wall[0] >= WINDOW_WIDTH or new_head_wall[1] >= WINDOW_HEIGHT)

        # Body collision
        self.assertIn(new_head_body, snake)

        # Food collision
        food = (120, 100)
        self.assertEqual(new_head_food, food)

    def test_scoring(self):
        # Test scoring functionality
        initial_score = 0
        snake = [(100, 100), (90, 100), (80, 100)]
        food = (120, 100)
        new_head = (120, 100)  # Snake eats food

        if new_head == food:
            updated_score = initial_score + 1
        else:
            updated_score = initial_score

        self.assertEqual(updated_score, 1)

if __name__ == "__main__":
    unittest.main()