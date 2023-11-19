import pygame
import random
import time

pygame.init()

import pygame
import random
import time

pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooting Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
bullet_color = (0, 255, 0)

# Player settings
player_width = 50
player_height = 50
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height

# Bullet settings
bullet_width = 5
bullet_height = 10
bullet_speed = 5
bullet_state = "ready"  # Define the bullet state

# Enemy settings
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = 0
enemy_speed = 3

# Score
score = 0
font = pygame.font.Font(None, 36)

# Player movement function
def player_movement(direction):
    global player_x
    if direction == "left":
        player_x -= 5
    elif direction == "right":
        player_x += 5

# Fire bullet function
def fire_bullet():
    global bullet_state, bullet_x, bullet_y
    bullet_state = "fire"
    pygame.draw.rect(screen, bullet_color, (bullet_x, bullet_y, bullet_width, bullet_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_movement("left")
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_movement("right")
    if keys[pygame.K_SPACE]:
        if bullet_state == "ready":
            bullet_x = player_x + player_width // 2
            bullet_y = player_y
            fire_bullet()

    if bullet_state == "fire":
        bullet_y -= bullet_speed
        if bullet_y <= 0:
            bullet_state = "ready"

    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = 0

    screen.fill(black)
    pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_width, enemy_height))
    player = pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))
    if bullet_state == "fire":
        bullet = pygame.draw.rect(screen, bullet_color, (bullet_x, bullet_y, bullet_width, bullet_height))

    # Check collision with enemy
    if bullet_state == "fire" and bullet.colliderect(enemy_x, enemy_y, enemy_width, enemy_height):
        score += 1
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = 0
        bullet_state = "ready"

    # Display score
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    time.sleep(0.01)

pygame.quit()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_movement("left")
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_movement("right")
    if keys[pygame.K_SPACE]:
        if bullet_state == "ready":
            bullet_x = player_x + player_width // 2
            bullet_y = player_y
            fire_bullet()

    if bullet_state == "fire":
        bullet_y -= bullet_speed
        if bullet_y <= 0:
            bullet_state = "ready"

    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = 0

    screen.fill(black)
    pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_width, enemy_height))
    player = pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))
    if bullet_state == "fire":
        bullet = pygame.draw.rect(screen, bullet_color, (bullet_x, bullet_y, bullet_width, bullet_height))

    # Check collision with enemy
    if bullet.colliderect((enemy_x, enemy_y, enemy_width, enemy_height)):
        score += 1
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = 0
        bullet_state = "ready"

    # Display score
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    time.sleep(0.002)

pygame.quit()
