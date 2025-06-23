import pygame
import random
from constants import *

class Pipe:
    """Class quản lý ống"""
    
    def __init__(self, x, y, assets):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 400
        self.gap = 180
        self.speed = 4
        self.move_direction = 0
        self.assets = assets
        self.ground_y = HEIGHT - 100
    
    def update(self):
        self.y += self.move_direction * self.speed
        self.y = max(self.gap // 2 + 50, min(self.ground_y - self.gap // 2 - 50, self.y))
        self.x -= 5
    
    def draw(self, screen):
        top_pipe_height = self.y - self.gap // 2
        bottom_pipe_start = self.y + self.gap // 2
        
        screen.blit(pygame.transform.flip(self.assets.pipe_up_img, False, True), 
                   (self.x, top_pipe_height - self.height))
        screen.blit(self.assets.pipe_down_img, (self.x, bottom_pipe_start))
    
    def reset_position(self):
        self.x = WIDTH
        self.y = random.randint(self.gap // 2 + 50, self.ground_y - self.gap // 2 - 50)
    
    def is_off_screen(self):
        return self.x + self.width < 0
    
    def get_top_rect(self):
        return pygame.Rect(self.x, 0, self.width, self.y - self.gap // 2)
    
    def get_bottom_rect(self):
        return pygame.Rect(self.x, self.y + self.gap // 2, self.width, HEIGHT - self.y)
    
    def set_move_direction(self, direction):
        self.move_direction = direction