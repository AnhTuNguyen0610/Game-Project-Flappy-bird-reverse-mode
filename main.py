import pygame
from bird import Bird
from pipe import Pipe
from constants import *
from assetmanager import AssetManager

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Flappy Bird - Reverse Mode")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 40)

        self.assets = AssetManager()
        self.reset()

    def reset(self):
        self.bird = Bird(x=100, y=HEIGHT // 2, assets=self.assets)
        self.pipe = Pipe(x=WIDTH, y=HEIGHT // 2, assets=self.assets)
        self.score = 0
        self.speed_timer = 0
        self.speed_interval = 500
        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.pipe.set_move_direction(-1)
                elif event.key == pygame.K_DOWN:
                    self.pipe.set_move_direction(1)
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    self.pipe.set_move_direction(0)

    def update(self):
        self.bird.update()
        self.pipe.update()

        # Kiểm tra va chạm
        bird_rect = self.bird.get_rect()
        if bird_rect.colliderect(self.pipe.get_top_rect()) or bird_rect.colliderect(self.pipe.get_bottom_rect()):
            self.game_over()

        # Kiểm tra ống ra khỏi màn hình
        if self.pipe.is_off_screen():
            self.pipe.reset_position()
            self.score += 1

        # Tăng độ khó dần theo thời gian
        self.speed_timer += 1
        if self.speed_timer >= self.speed_interval:
            self.bird.oscillation_speed += 0.005
            self.pipe.speed += 0.3
            self.speed_timer = 0

    def draw(self):
        self.screen.fill(WHITE)
        self.bird.draw(self.screen)
        self.pipe.draw(self.screen)

        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (10, 10))

        pygame.display.flip()

    def game_over(self):
        text = self.font.render("Game Over!", True, RED)
        self.screen.blit(text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
        pygame.display.flip()
        pygame.time.delay(2000)
        self.running = False


if __name__ == "__main__":
    game = Game()
    game.run()