import pygame
import random

pygame.init()
WIDTH, HEIGHT = 1280, 800
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50
PLAYER_SPEED = 5
OBSTACLE_SPEED = 5
KURO = (60, 60, 60)
MURASAKI = (127, 0, 255)
AKAI = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid Obstacles")
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - PLAYER_SIZE - 10, PLAYER_SIZE, PLAYER_SIZE)
obstacles = []
clock = pygame.time.Clock()     # controls frame rate
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player.x < WIDTH - PLAYER_SIZE:
        player.x += PLAYER_SPEED

    if random.randint(1, 10) == 1:
        obstacle = pygame.Rect(random.randint(0, WIDTH - OBSTACLE_SIZE), 0, OBSTACLE_SIZE, OBSTACLE_SIZE)
        obstacles.append(obstacle)
    for obstacle in obstacles:
        obstacle.y += OBSTACLE_SPEED
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)
            score += 1
        if player.colliderect(obstacle):
            running = False
    screen.fill(KURO)
    pygame.draw.rect(screen, MURASAKI, player)
    for obstacle in obstacles:
        pygame.draw.rect(screen, MURASAKI, obstacle)
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", False, AKAI)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()       # Update Display
    clock.tick(30)
pygame.quit()