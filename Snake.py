import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up display
width = 600
height = 400
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game with Fruits")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
yellow = (255, 255, 102)
purple = (160, 32, 240)
orange = (255, 165, 0)

# Snake block size and speed
snake_block = 10
snake_speed = 15

# Fonts
font = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 25)

# Clock
clock = pygame.time.Clock()

# Fruit list (name, color, points)
fruits = [
    ("Apple", red, 1),
    ("Banana", yellow, 2),
    ("Grapes", purple, 3),
    ("Orange", orange, 2)
]

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, black, [x[0], x[1], snake_block, snake_block])

def draw_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    game_window.blit(value, [10, 10])

def message(msg, color, pos):
    mesg = font.render(msg, True, color)
    game_window.blit(mesg, pos)

def gameLoop():
    game_over = False
    game_close = False

    # Starting position
    x1 = width / 2
    y1 = height / 2

    # Movement
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Score
    score = 0

    # Pick a fruit
    fruit = random.choice(fruits)
    fruitx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    fruity = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_window.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red, [width/6, height/3])
            draw_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Check boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_window.fill(blue)

        # Draw fruit
        pygame.draw.rect(game_window, fruit[1], [fruitx, fruity, snake_block, snake_block])

        # Snake logic
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        draw_score(score)

        pygame.display.update()

        # Eating fruit
        if x1 == fruitx and y1 == fruity:
            score += fruit[2]  # add fruit points
            length_of_snake += 1
            fruit = random.choice(fruits)  # pick a new fruit
            fruitx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            fruity = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
