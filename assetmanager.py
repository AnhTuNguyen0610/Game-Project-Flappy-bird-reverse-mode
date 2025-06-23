import pygame
import os
from constants import *


class AssetManager:
    """Quản lý tất cả assets của game"""
    
    def __init__(self):
        self.ensure_assets_folder()
        self.load_fonts()
        self.load_images()
        self.load_sounds()
    
    def ensure_assets_folder(self):
        if not os.path.exists("assets"):
            os.makedirs("assets")
    
    def load_fonts(self):
        self.font = pygame.font.SysFont("Arial", 40)
        self.large_font = pygame.font.SysFont("Arial", 60)
    
    def load_image(self, file_path, size=None, convert_alpha=True, fallback_color=None):
        try:
            if os.path.exists(file_path):
                if convert_alpha:
                    image = pygame.image.load(file_path).convert_alpha()
                else:
                    image = pygame.image.load(file_path).convert()
                
                if size:
                    image = pygame.transform.scale(image, size)
                return image
            else:
                if fallback_color:
                    if size:
                        surface = pygame.Surface(size, pygame.SRCALPHA if convert_alpha else 0)
                        surface.fill(fallback_color)
                        return surface
                    else:
                        surface = pygame.Surface((50, 50), pygame.SRCALPHA if convert_alpha else 0)
                        surface.fill(fallback_color)
                        return surface
        except Exception as e:
            print(f"Error loading image {file_path}: {e}")
            if size:
                return pygame.Surface(size, pygame.SRCALPHA)
            else:
                return pygame.Surface((50, 50), pygame.SRCALPHA)
    
    def load_images(self):
        # Background
        self.background_img = self.load_image("assets/backround.jpg", (WIDTH, HEIGHT), 
                                            convert_alpha=False, fallback_color=BLUE_SKY)
        # Ground
        self.ground_img = self.load_image("", (WIDTH, 100), fallback_color=(222, 184, 135))
        
        # Pipes
        self.pipe_up_img = self.load_image("assets/pipe.png", (80, 400), fallback_color=GREEN)
        self.pipe_down_img = self.load_image("assets/pipe.png", (80, 400), fallback_color=GREEN)
        
        # Bird
        self.bird_frames = [
            self.load_image("assets/bird.png", (80, 80), fallback_color=(255, 205, 0))
        ]
        
        # Clouds
        self.cloud_img = self.load_image("assets/cloud.png", (1000, 1000), fallback_color=WHITE)
        
        # UI
        self.game_over_img = self.load_image("assets/—Pngtree—game end game over_655542.png", 
                                           (300, 100), fallback_color=None)
        self.start_button_img = self.load_image("assets/pngkit_start-button-png_8948805.png", 
                                              (200, 80), fallback_color=None)
    
    def load_sounds(self):
        try:
            self.point_sound = pygame.mixer.Sound("sound/collect-points-190037.mp3")
            self.hit_sound = pygame.mixer.Sound("sound/game-over-2-sound-effect-230463.mp3")
            self.wing_sound = pygame.mixer.Sound("sound/wood-effect-254997.mp3")
        except:
            print("Sound files not found. Playing without sound.")
            self.point_sound = None
            self.hit_sound = None
            self.wing_sound = None