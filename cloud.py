import pygame
import random
from constants import *

class Cloud:
    """Class quản lý đám mây"""
    
    def __init__(self, assets):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(HEIGHT//4, HEIGHT - 250)
        self.width = random.randint(80, 120)
        self.height = random.randint(50, 70)
        self.speed = random.uniform(0.5, 1.5)
        self.assets = assets
    
    def update(self):
        self.x -= self.speed
        if self.x < -self.width:
            self.reset_position()
    
    def reset_position(self):
        self.x = WIDTH + random.randint(50, 200)
        self.y = random.randint(HEIGHT//4, HEIGHT - 250)
        self.width = random.randint(80, 120)
        self.height = random.randint(50, 70)
        self.speed = random.uniform(0.5, 1.5)
    
    def draw(self, screen):
        cloud_surface = pygame.transform.scale(self.assets.cloud_img, (self.width, self.height))
        screen.blit(cloud_surface, (self.x, self.y))