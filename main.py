import pygame
from bird import Bird
from pipe import Pipe
from cloud import Cloud
from ground import Ground
from constants import *
from assetmanager import AssetManager
from collision_detector import CollisionDetector
from score_manager import ScoreManager
from stage_manager import GameStateManager


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Flappy Bird - Reverse Mode")
        self.clock = pygame.time.Clock()

        self.assets = AssetManager()
        self.reset_all()

    def reset_all(self):
        self.bird = Bird(x=100, y=HEIGHT // 2, assets=self.assets)
        self.pipe = Pipe(x=WIDTH + 100, y=HEIGHT // 2, assets=self.assets)
        self.ground = Ground(assets=self.assets)
        self.clouds = [Cloud(self.assets) for _ in range(5)]

        self.score_manager = ScoreManager()
        self.state_manager = GameStateManager()

        self.pipe_move_timer = 0
        self.pipe_speed_increase_interval = 500

    def run(self):
        while True:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            elif event.type == pygame.KEYDOWN:
                if self.state_manager.is_menu():
                    self.state_manager.set_state(PLAYING)

                elif self.state_manager.is_game_over():
                    self.reset_all()
                    self.state_manager.set_state(PLAYING)

                elif self.state_manager.is_playing():
                    if event.key == pygame.K_UP:
                        self.pipe.set_move_direction(-1)
                    elif event.key == pygame.K_DOWN:
                        self.pipe.set_move_direction(1)

            elif event.type == pygame.KEYUP and self.state_manager.is_playing():
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    self.pipe.set_move_direction(0)

    def update(self):
        if self.state_manager.is_playing():
            for cloud in self.clouds:
                cloud.update()

            self.bird.update()
            self.pipe.update()
            self.ground.update()

            if self.pipe.is_off_screen():
                self.pipe.reset_position()
                self.score_manager.add_point()

            if pygame.time.get_ticks() > 1000:  # delay kiểm tra va chạm
                if CollisionDetector.check_collision(self.bird, self.pipe, self.ground.y):
                    self.score_manager.save_high_score()
                    self.state_manager.set_state(GAME_OVER)

            # Tăng độ khó
            self.pipe_move_timer += 1
            if self.pipe_move_timer >= self.pipe_speed_increase_interval:
                self.bird.oscillation_speed += 0.005
                self.pipe.speed += 0.3
                self.pipe_move_timer = 0

    def draw(self):
        self.screen.fill(BLUE_SKY)

        for cloud in self.clouds:
            cloud.draw(self.screen)

        if self.state_manager.is_menu():
            self.draw_menu()
        elif self.state_manager.is_playing():
            self.pipe.draw(self.screen)
            self.bird.draw(self.screen)
            self.ground.draw(self.screen)
            self.score_manager.draw(self.screen, self.assets)
        elif self.state_manager.is_game_over():
            self.pipe.draw(self.screen)
            self.bird.draw(self.screen)
            self.ground.draw(self.screen)
            self.score_manager.draw(self.screen, self.assets)
            self.draw_game_over()

        pygame.display.flip()

    def draw_menu(self):
        title = self.assets.font.render("Flappy Bird Reverse", True, WHITE)
        start = self.assets.font.render("Nhấn bất kỳ để bắt đầu", True, WHITE)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 60))
        self.screen.blit(start, (WIDTH // 2 - start.get_width() // 2, HEIGHT // 2 + 10))

    def draw_game_over(self):
        text = self.assets.font.render("Game Over!", True, RED)
        restart = self.assets.font.render("Nhấn phím bất kỳ để chơi lại", True, WHITE)
        self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 50))
        self.screen.blit(restart, (WIDTH // 2 - restart.get_width() // 2, HEIGHT // 2 + 10))

    def quit(self):
        self.score_manager.save_high_score()
        pygame.quit()
        exit()


if __name__ == "__main__":
    Game().run()
