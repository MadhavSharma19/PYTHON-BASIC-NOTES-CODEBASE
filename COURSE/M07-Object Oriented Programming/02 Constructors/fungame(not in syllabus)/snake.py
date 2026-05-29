# =========================================
# 🐍 Modern Snake Game using Pygame
# =========================================

# Install pygame first:
# pip install pygame

import pygame
import random
import sys

# =========================================
# INITIAL SETUP
# =========================================

pygame.init()

# Screen Size
WIDTH = 800
HEIGHT = 600

# Creating Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("🐍 Snake Game")

# Clock
clock = pygame.time.Clock()

# =========================================
# COLORS
# =========================================

BLACK = (15, 15, 15)
GREEN = (0, 255, 120)
RED = (255, 80, 80)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 180, 90)

# =========================================
# FONTS
# =========================================

font = pygame.font.SysFont("arial", 30, bold=True)

big_font = pygame.font.SysFont("arial", 60, bold=True)

# =========================================
# SNAKE SETTINGS
# =========================================

snake_block = 20

snake_speed = 12

# Snake Position
x = WIDTH // 2
y = HEIGHT // 2

# Snake Movement
x_change = 0
y_change = 0

# Snake Body
snake_list = []

snake_length = 1

# =========================================
# FOOD SETTINGS
# =========================================

food_x = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20

food_y = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20

# =========================================
# SCORE
# =========================================

score = 0

# =========================================
# FUNCTIONS
# =========================================

def draw_snake(block, snake):

    for i, part in enumerate(snake):

        if i == len(snake) - 1:

            pygame.draw.rect(screen, GREEN, [part[0], part[1], block, block], border_radius=8)

        else:

            pygame.draw.rect(screen, DARK_GREEN, [part[0], part[1], block, block], border_radius=6)

def show_score():

    value = font.render(f"Score : {score}", True, WHITE)

    screen.blit(value, [20, 20])

def draw_food(x, y):

    pygame.draw.circle(screen, RED, (x + 10, y + 10), 10)

    pygame.draw.circle(screen, (0, 255, 0), (x + 14, y + 4), 4)

def game_over_screen():

    screen.fill(BLACK)

    text = big_font.render("GAME OVER", True, RED)

    screen.blit(text, (WIDTH // 2 - 180, HEIGHT // 2 - 100))

    score_text = font.render(f"Final Score : {score}", True, WHITE)

    screen.blit(score_text, (WIDTH // 2 - 90, HEIGHT // 2))

    retry_text = font.render("Press R to Restart or Q to Quit", True, GREEN)

    screen.blit(retry_text, (WIDTH // 2 - 200, HEIGHT // 2 + 80))

    pygame.display.update()

# =========================================
# GAME LOOP
# =========================================

running = True

game_over = False

while running:

    while game_over:

        game_over_screen()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:

                    pygame.quit()

                    sys.exit()

                if event.key == pygame.K_r:

                    python = sys.executable

                    import os

                    os.execl(python, python, *sys.argv)

    # =========================================
    # EVENTS
    # =========================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                x_change = -snake_block

                y_change = 0

            elif event.key == pygame.K_RIGHT:

                x_change = snake_block

                y_change = 0

            elif event.key == pygame.K_UP:

                y_change = -snake_block

                x_change = 0

            elif event.key == pygame.K_DOWN:

                y_change = snake_block

                x_change = 0

    # =========================================
    # MOVEMENT
    # =========================================

    x += x_change

    y += y_change

    # =========================================
    # WALL COLLISION
    # =========================================

    if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:

        game_over = True

    # =========================================
    # BACKGROUND
    # =========================================

    screen.fill(BLACK)

    # Grid Effect
    for i in range(0, WIDTH, 20):

        pygame.draw.line(screen, (25, 25, 25), (i, 0), (i, HEIGHT))

    for j in range(0, HEIGHT, 20):

        pygame.draw.line(screen, (25, 25, 25), (0, j), (WIDTH, j))

    # =========================================
    # DRAW FOOD
    # =========================================

    draw_food(food_x, food_y)

    # =========================================
    # SNAKE LOGIC
    # =========================================

    snake_head = []

    snake_head.append(x)

    snake_head.append(y)

    snake_list.append(snake_head)

    if len(snake_list) > snake_length:

        del snake_list[0]

    # Self Collision
    for part in snake_list[:-1]:

        if part == snake_head:

            game_over = True

    # Draw Snake
    draw_snake(snake_block, snake_list)

    # =========================================
    # SCORE
    # =========================================

    show_score()

    # =========================================
    # UPDATE SCREEN
    # =========================================

    pygame.display.update()

    # =========================================
    # FOOD COLLISION
    # =========================================

    if x == food_x and y == food_y:

        food_x = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20

        food_y = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20

        snake_length += 1

        score += 10

    # =========================================
    # FPS
    # =========================================

    clock.tick(snake_speed)

# =========================================
# QUIT
# =========================================

pygame.quit()