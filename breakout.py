import pygame
import random

# initialize pygame
pygame.init()

# screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout   -   by Max Fischetti")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 100,10
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 8

# ball settings
BALL_RADIUS = 10
ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_RADIUS*2, BALL_RADIUS*2)
ball_speed_x = 1
ball_speed_y = 2

# brick settings
BRICK_ROWS = 8
BRICK_COLS = 10
BRICK_WIDTH = WIDTH//BRICK_COLS
BRICK_HEIGHT = HEIGHT//BRICK_ROWS
bricks = []

# Create bricks
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT + 50, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
        bricks.append(brick)

# game loop
running = True
clock = pygame.time.Clock()

while running == True:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False