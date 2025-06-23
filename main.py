import pygame
from bird import Bird
from pipe import Pipe
from cloud import Cloud
from ground import Ground
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
        self.pipe = Pipe(x=WIDTH + 100, y=HEIGHT // 2, assets=self.assets)
        self.ground = Ground(assets=self.assets)
        
        # Tạo nhiều đám mây
        self.clouds = [Cloud(self.assets) for _ in range(5)]

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
        for cloud in self.clouds:
            cloud.update()

        self.bird.update()
        self.pipe.update()
        self.ground.update()

        # Delay 1s đầu để tránh va chạm tức thì
        if pygame.time.get_ticks() > 1000:
            bird_rect = self.bird.get_rect()
            if bird_rect.colliderect(self.pipe.get_top_rect()) or bird_rect.colliderect(self.pipe.get_bottom_rect()):
                self.game_over()

        if self.pipe.is_off_screen():
            self.pipe.reset_position()
            self.score += 1

        self.speed_timer += 1
        if self.speed_timer >= self.speed_interval:
            self.bird.oscillation_speed += 0.005
            self.pipe.speed += 0.3
            self.speed_timer = 0

    def draw(self):
        self.screen.fill(BLUE_SKY)  # nền trời xanh

        # Layer: clouds -> pipe -> bird -> ground
        for cloud in self.clouds:
            cloud.draw(self.screen)

        self.pipe.draw(self.screen)
        self.bird.draw(self.screen)
        self.ground.draw(self.screen)

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
