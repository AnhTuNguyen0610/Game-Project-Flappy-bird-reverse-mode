import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird - Reverse Mode")

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

font = pygame.font.SysFont(None, 40)

bird_radius = 20
bird_x = 100
bird_timer = 0
oscillation_speed = 0.04
oscillation_amplitude = 80
phase_shift = random.uniform(0, math.pi * 2)

pipe_width = 80
pipe_gap = 180
pipe_x = WIDTH
pipe_y = HEIGHT // 2
pipe_speed = 4
pipe_move_direction = 0

speed_increase_timer = 0
speed_interval = 500  

score = 0

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pipe_move_direction = -1
            elif event.key == pygame.K_DOWN:
                pipe_move_direction = 1
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                pipe_move_direction = 0

    pipe_y += pipe_move_direction * pipe_speed
    pipe_y = max(pipe_gap // 2, min(HEIGHT - pipe_gap // 2, pipe_y))
    pipe_x -= 5
    if pipe_x + pipe_width < 0:
        pipe_x = WIDTH
        pipe_y = random.randint(150, HEIGHT - 150)
        score += 1

    bird_timer += 1
    bird_y = HEIGHT // 2 + math.sin(bird_timer * oscillation_speed + phase_shift) * oscillation_amplitude
    bird_y += math.sin(bird_timer * 0.1) * 10  

    pygame.draw.circle(screen, RED, (int(bird_x), int(bird_y)), bird_radius)

    top_rect = pygame.Rect(pipe_x, 0, pipe_width, pipe_y - pipe_gap // 2)
    bottom_rect = pygame.Rect(pipe_x, pipe_y + pipe_gap // 2, pipe_width, HEIGHT - pipe_y)
    pygame.draw.rect(screen, GREEN, top_rect)
    pygame.draw.rect(screen, GREEN, bottom_rect)

    bird_rect = pygame.Rect(bird_x - bird_radius, bird_y - bird_radius, bird_radius * 2, bird_radius * 2)
    if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
        text = font.render("Game Over!", True, RED)
        screen.blit(text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    speed_increase_timer += 1
    if speed_increase_timer >= speed_interval:
        oscillation_speed += 0.005
        pipe_speed += 0.3
        speed_increase_timer = 0

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()