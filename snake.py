import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def get_random_food():
    return random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1)

def main():
    clock = pygame.time.Clock()
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    food = get_random_food()
    dx, dy = 0, 0
    new_segment = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -1, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = 1, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, 1

        # Move the snake
        head_x, head_y = snake[-1]
        new_head = (head_x + dx, head_y + dy)

        # Check for collisions
        if new_head in snake or new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
            print("Game Over")
            pygame.quit()
            sys.exit()

        # Check if the snake eats the food
        if new_head == food:
            new_segment = True
            food = get_random_food()

        # Update the snake
        snake.append(new_head)
        if not new_segment:
            snake.pop(0)
        new_segment = False

        # Draw the screen
        screen.fill(BLACK)
        draw_grid()
        draw_food(food)
        draw_snake(snake)
        pygame.display.flip()

        clock.tick(FPS)

if __name__ == "__main__":
    main()
