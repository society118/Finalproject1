import pygame
import random

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Racing Game")

clock = pygame.time.Clock()
FPS = 60


WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)


player_width = 50
player_height = 90
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 30
player_speed = 7


obs_width = 50
obs_height = 90
obs_speed = 5
obstacles = []
spawn_timer = 0
spawn_delay = 90

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    spawn_timer += 1
    if spawn_timer >= spawn_delay:
        spawn_timer = 0
        obs_x = random.randrange(0, WIDTH - obs_width)
        obs_rect = pygame.Rect(obs_x, -obs_height, obs_width, obs_height)
        obstacles.append(obs_rect)

    for obs in obstacles:
        obs.y += obs_speed

    obstacles = [obs for obs in obstacles if obs.y < HEIGHT]

    for obs in obstacles:

        pass

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for obs in obstacles:
        if player_rect.colliderect(obs):

            running = False

    road_margin = 100
    pygame.draw.rect(screen, BLACK, (road_margin, 0, WIDTH - 2 * road_margin, HEIGHT))

    pygame.draw.rect(screen, GREEN, (0, 0, road_margin, HEIGHT))
    pygame.draw.rect(screen, GREEN, (WIDTH - road_margin, 0, road_margin, HEIGHT))

    pygame.draw.rect(screen, WHITE, player_rect)

    for obs in obstacles:
        pygame.draw.rect(screen, RED, obs)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    score += 1

pygame.quit()
