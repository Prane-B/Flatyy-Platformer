import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 800))

# Load images
link = pygame.image.load('Assets/link.png')
link = pygame.transform.scale(link, (125, 100))

bg = pygame.image.load('Assets/bg.png')

wall = pygame.image.load('Assets/wall.png')

coin = pygame.image.load('Assets/coin.png')
coin = pygame.transform.scale(coin, (75, 75))

# Link's initial position
px = 400
py = 400

# Movement flags
run = True
w = False
a = False
s = False
d = False

# Coin position
coin_x, coin_y = 407, 155
# Score or some action when the coin is collected
score = 0
level = 1



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                a = True
            if event.key == pygame.K_d:
                d = True
            if event.key == pygame.K_w:
                w = True
            if event.key == pygame.K_s:
                s = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                a = False
            if event.key == pygame.K_d:
                d = False
            if event.key == pygame.K_w:
                w = False
            if event.key == pygame.K_s:
                s = False

    # Move the object based on key presses
    if a:
        px -= 1
    if d:
        px += 1
    if w:
        py -= 1
    if s:
        py += 1

    # Link's collision with walls (boundaries)
    if px < 0:
        px = 0
    if px + 125 > 800:  # 125 is the width of link
        px = 800 - 125
    if py < 20:  # 20 is the height of the top wall
        py = 20
    if py + 100 > 800 - 20:  # 100 is the height of link, 20 is the bottom wall height
        py = 800 - 20 - 100

    # Create a rectangle for Link
    link_rect = pygame.Rect(px, py, 125, 100)  # Create a rectangle for Link
    coin_rect = pygame.Rect(coin_x,coin_y,5,60)
    # Check for collision with the coin
    if link_rect.colliderect(coin_rect):
        score += 1  # Increment score or trigger some action
        print("Score:", score, level) # Print score or handle it as needed
        level += 1
        px,py = 400,400
    # Draw everything
    screen.blit(bg, (0, 0))

    # Draw walls
    screen.blit(wall, (0, 0))       # Top wall
    screen.blit(wall, (0, 780))     # Bottom wall
    screen.blit(pygame.transform.rotate(wall, 90), (0, 0))  # Left wall
    screen.blit(pygame.transform.rotate(wall, 90), (780, 0))  # Right wall

    screen.blit(coin, (coin_x, coin_y))  # Draw coin at its position
    # Draw link
    screen.blit(coin,(coin_x,coin_y))
    screen.blit(link, (px, py))
    if level == 2:
        coin_x, coin_y = 700, 25
        wall_rect = pygame.Rect(650,175,20,650)
        screen.blit(pygame.transform.rotate(wall,90), (650,-175))
        if link_rect.colliderect(wall_rect):
            print("collided")

    # Update the display
    pygame.display.update()

pygame.quit()













