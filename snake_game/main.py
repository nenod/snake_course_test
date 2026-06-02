import pygame
import random
import sys

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
SNAKE_SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
RED = (255, 82, 82)
GREEN = (76, 175, 80)
BLUE = (33, 150, 243)
GRAY = (200, 200, 200)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Modern Snake")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        self.reset_game()

    def reset_game(self):
        self.snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (GRID_SIZE, 0)
        self.new_direction = self.direction
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False
        self.speed = SNAKE_SPEED

    def spawn_food(self):
        while True:
            x = random.randrange(0, SCREEN_WIDTH, GRID_SIZE)
            y = random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)
            if (x, y) not in self.snake:
                return (x, y)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_r:
                        self.reset_game()
                else:
                    if event.key == pygame.K_UP and self.direction != (0, GRID_SIZE):
                        self.new_direction = (0, -GRID_SIZE)
                    elif event.key == pygame.K_DOWN and self.direction != (0, -GRID_SIZE):
                        self.new_direction = (0, GRID_SIZE)
                    elif event.key == pygame.K_LEFT and self.direction != (GRID_SIZE, 0):
                        self.new_direction = (-GRID_SIZE, 0)
                    elif event.key == pygame.K_RIGHT and self.direction != (-GRID_SIZE, 0):
                        self.new_direction = (GRID_SIZE, 0)

    def update(self):
        if self.game_over:
            return

        self.direction = self.new_direction
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # Wall collision
        if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
            new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT):
            self.game_over = True
            return

        # Self collision
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        # Food collision
        if new_head == self.food:
            self.score += 10
            self.food = self.spawn_food()
            # Increase speed slightly as the snake grows
            if self.score % 50 == 0:
                self.speed += 1
        else:
            self.snake.pop()

    def draw(self):
        self.screen.fill(BLACK)

        # Draw food
        pygame.draw.rect(self.screen, RED, (self.food[0], self.food[1], GRID_SIZE - 2, GRID_SIZE - 2))

        # Draw snake
        for i, segment in enumerate(self.snake):
            color = GREEN if i == 0 else BLUE
            pygame.draw.rect(self.screen, color, (segment[0], segment[1], GRID_SIZE - 2, GRID_SIZE - 2))

        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        if self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            self.screen.blit(overlay, (0, 0))
            
            over_text = self.font.render("GAME OVER", True, WHITE)
            restart_text = self.font.render("Press 'R' to Restart", True, GRAY)
            
            self.screen.blit(over_text, (SCREEN_WIDTH // 2 - 60, SCREEN_HEIGHT // 2 - 20))
            self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 20))

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(self.speed)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
