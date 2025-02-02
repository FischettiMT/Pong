import pygame
import sys

# Initialize PyGame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 900

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
CYAN = ( 0, 255, 255)
YELLOW = (255, 255, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 200
PADDLE_SPEED = 5

# Ball settings
BALL_WIDTH, BALL_HEIGHT = 45, 45
BALL_SPEED_X, BALL_SPEED_Y = 4, 4
score = 0
score_x_position = (SCREEN_WIDTH/2)-50
score_y_position = 10

# Define font for score
my_font = pygame.font.Font(None,36)
score_text = None

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game by Max Fischetti")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Initialize paddles and ball
player1_y = player2_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y
current_direction = ball_dx

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys for paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        player1_y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        player2_y += PADDLE_SPEED

    # Update ball position
    ball_x += ball_dx     # ball_x = ball_x + ball_dx
    ball_y += ball_dy

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - BALL_HEIGHT:
        ball_dy = -ball_dy

    # Ball collision with paddles
    if ((ball_x <= PADDLE_WIDTH) and
         (player1_y <= ball_y <= player1_y + PADDLE_HEIGHT)) or \
       ((ball_x >= SCREEN_WIDTH - PADDLE_WIDTH - BALL_WIDTH) and
         (player2_y <= ball_y <= player2_y + PADDLE_HEIGHT)):
        ball_dx = -ball_dx

    # # Ball collision with paddles
    # current_direction = ball_dx
    # if ((ball_x <= PADDLE_WIDTH) and
    #      (player1_y <= ball_y <= player1_y + PADDLE_HEIGHT)):
    #     ball_dx = -ball_dx

    # if ((ball_x >= SCREEN_WIDTH - PADDLE_WIDTH - BALL_WIDTH) and
    #      (player2_y <= ball_y <= player2_y + PADDLE_HEIGHT)):
    #     ball_dx = -ball_dx
    #     score += 1
    #     score_text = my_font.render(f"Score: {score}",True,WHITE)
    #     screen.blit(score_text,(score_x_position,score_y_position))

    # Ball out of bounds
    if ((ball_x < 0) or (ball_x > SCREEN_WIDTH)):
        ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, 
                    (0, ball_y - (PADDLE_HEIGHT/2 - (BALL_HEIGHT/2)), 
                    PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, 
                     (SCREEN_WIDTH - PADDLE_WIDTH, player2_y,
                       PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, RED, 
                        (ball_x, ball_y, 
                        BALL_WIDTH, BALL_HEIGHT))

    # Update score on screen
    score = score+1
    score_text = my_font.render(f"Score: {score}",True,WHITE)
    screen.blit(score_text,(score_x_position,score_y_position))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit PyGame
pygame.quit()
sys.exit()
