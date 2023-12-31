import pygame
import time
import random

pygame.init()

# Set up display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up snake
snake_block = 10
snake_speed = 15
snake = [(width / 2, height / 2)]  # Initial position of the snake
snake_direction = 'RIGHT'

# Set up food
food_size = 10
food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]

# Set up score
score = 0

# Main game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not snake_direction == 'DOWN':
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and not snake_direction == 'UP':
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and not snake_direction == 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and not snake_direction == 'LEFT':
                snake_direction = 'RIGHT'

    # Move the snake
    new_head = (snake[0][0], snake[0][1])
    if snake_direction == 'UP':
        new_head = (new_head[0], new_head[1] - snake_block)
    elif snake_direction == 'DOWN':
        new_head = (new_head[0], new_head[1] + snake_block)
    elif snake_direction == 'LEFT':
        new_head = (new_head[0] - snake_block, new_head[1])
    elif snake_direction == 'RIGHT':
        new_head = (new_head[0] + snake_block, new_head[1])

    snake.insert(0, new_head)

    # Check if snake ate the food
    if (
        snake[0][0] == food_pos[0] and snake[0][1] == food_pos[1]
    ):
        score += 1
        food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
    else:
        snake.pop()

    # Check if snake collided with walls
    if (
        snake[0][0] < 0
        or snake[0][0] >= width
        or snake[0][1] < 0
        or snake[0][1] >= height
        or any(segment == snake[0] for segment in snake[1:])
    ):
        game_over = True

    # Draw everything on the screen
    display.fill(black)
    for pos in snake:
        pygame.draw.rect(display, green, [pos[0], pos[1], snake_block, snake_block])
    pygame.draw.rect(display, red, [food_pos[0], food_pos[1], food_size, food_size])

    # Display the score
    font = pygame.font.SysFont(None, 25)
    score_text = font.render("Score: " + str(score), True, white)
    display.blit(score_text, [10, 10])

    pygame.display.update()

    # Set the frame rate
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
