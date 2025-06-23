import pygame
from constants import *
from assetmanager import AssetManager
from bird import Bird
from pipe import Pipe
from cloud import Cloud
from ground import Ground
from score_manager import ScoreManager
from collision_detector import CollisionDetector
from assetmanager import AssetManager
from stage_manager import GameStateManager


pygame.init()
pygame.mixer.init()


class Game:
    """Main game class"""
    
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Flappy Bird - Reverse Mode")
        self.clock = pygame.time.Clock()
        
        # Initialize components
        self.assets = AssetManager()
        self.state_manager = GameStateManager()
        self.score_manager = ScoreManager()
        
        # Game objects
        self.bird = Bird(100, HEIGHT // 2, self.assets)
        self.pipe = Pipe(WIDTH, HEIGHT // 2, self.assets)
        self.ground = Ground(self.assets)
        self.clouds = [Cloud(self.assets) for _ in range(5)]
        
        self.running = True
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                
                elif event.key == pygame.K_SPACE:
                    if self.state_manager.is_menu():
                        self.state_manager.set_state(PLAYING)
                        self.reset_game()
                    elif self.state_manager.is_game_over():
                        self.state_manager.set_state(PLAYING)
                        self.reset_game()
                
                elif self.state_manager.is_playing():
                    if event.key == pygame.K_p:
                        self.state_manager.set_state(PAUSED)
                    elif event.key == pygame.K_UP:
                        self.pipe.set_move_direction(-1)
                        if self.assets.wing_sound:
                            self.assets.wing_sound.play()
                    elif event.key == pygame.K_DOWN:
                        self.pipe.set_move_direction(1)
                        if self.assets.wing_sound:
                            self.assets.wing_sound.play()
                
                elif self.state_manager.is_paused():
                    if event.key == pygame.K_p:
                        self.state_manager.set_state(PLAYING)
            
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    self.pipe.set_move_direction(0)
    
    def update(self):
        if self.state_manager.is_playing():
            self.bird.update()
            self.pipe.update()
            self.ground.update()
            
            for cloud in self.clouds:
                cloud.update()
            
            # Check if pipe passed
            if self.pipe.is_off_screen():
                self.pipe.reset_position()
                self.score_manager.add_point()
                if self.assets.point_sound:
                    self.assets.point_sound.play()
                
                # Increase difficulty
                if self.score_manager.score % 5 == 0:
                    self.bird.oscillation_speed += 0.005
                    self.pipe.speed += 0.2
            
            # Check collision
            if CollisionDetector.check_collision(self.bird, self.pipe, self.ground.y):
                if self.assets.hit_sound:
                    self.assets.hit_sound.play()
                
                self.score_manager.save_high_score()
                self.state_manager.set_state(GAME_OVER)
        
        elif self.state_manager.is_menu():
            self.bird.update_animation()
            for cloud in self.clouds:
                cloud.update()
            self.ground.update()
    
    def draw(self):
        self.screen.blit(self.assets.background_img, (0, 0))
        
        for cloud in self.clouds:
            cloud.draw(self.screen)
        
        if self.state_manager.is_menu():
            self.draw_menu()
        elif self.state_manager.is_playing():
            self.draw_game()
        elif self.state_manager.is_game_over():
            self.draw_game()
            self.draw_game_over()
        elif self.state_manager.is_paused():
            self.draw_game()
            self.draw_paused()
        
        self.ground.draw(self.screen)
        pygame.display.flip()
    
    def draw_menu(self):
        title = self.assets.large_font.render("Reverse Flappy Bird", True, BLACK)
        instructions = self.assets.font.render("Press SPACE to Start", True, BLACK)
        high_score_text = self.assets.font.render(f"High Score: {self.score_manager.high_score}", True, BLACK)
        
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
        self.screen.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, HEIGHT // 2))
        self.screen.blit(high_score_text, (WIDTH // 2 - high_score_text.get_width() // 2, HEIGHT // 2 + 80))
        
        self.screen.blit(self.assets.bird_frames[self.bird.current_frame], 
                        (WIDTH // 2 - self.bird.width//2, HEIGHT // 2 - 80 - self.bird.height//2))
    
    def draw_game(self):
        self.pipe.draw(self.screen)
        self.bird.draw(self.screen)
        self.score_manager.draw(self.screen, self.assets)
    
    def draw_game_over(self):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        self.screen.blit(overlay, (0, 0))
        
        if self.assets.game_over_img:
            self.screen.blit(self.assets.game_over_img, 
                           (WIDTH // 2 - self.assets.game_over_img.get_width() // 2, HEIGHT // 3))
        else:
            game_over_text = self.assets.large_font.render("Game Over!", True, RED)
            self.screen.blit(game_over_text, 
                           (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
        
        score_text = self.assets.font.render(f"Score: {self.score_manager.score}", True, WHITE)
        self.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        
        restart_text = self.assets.font.render("Press SPACE to Restart", True, WHITE)
        quit_text = self.assets.font.render("Press ESC to Quit", True, WHITE)
        self.screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))
        self.screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 100))
    
    def draw_paused(self):
        pause_text = self.assets.large_font.render("Game Paused", True, RED)
        resume_text = self.assets.font.render("Press P to Resume", True, BLACK)
        
        self.screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2 - 40))
        self.screen.blit(resume_text, (WIDTH // 2 - resume_text.get_width() // 2, HEIGHT // 2 + 20))
    
    def reset_game(self):
        self.bird = Bird(100, HEIGHT // 2, self.assets)
        self.pipe = Pipe(WIDTH, HEIGHT // 2, self.assets)
        self.score_manager.reset()
    
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()
        
        pygame.quit()

# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()