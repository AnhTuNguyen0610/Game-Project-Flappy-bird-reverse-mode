import pygame
import random
import math
from constants import *



class Bird:
    """Class quản lý chim"""
    
    def __init__(self, x, y, assets):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 80
        self.assets = assets
        self.timer = 0
        self.oscillation_speed = 0.04
        self.oscillation_amplitude = 80
        self.phase_shift = random.uniform(0, math.pi * 2)
        self.current_frame = 0
        self.animation_timer = 0
    
    def update(self):
        self.timer += 1
        self.y = HEIGHT // 2 + math.sin(self.timer * self.oscillation_speed + self.phase_shift) * self.oscillation_amplitude
        self.update_animation()
    
    def update_animation(self):
        self.animation_timer += 1
        if self.animation_timer >= 15:
            self.current_frame = (self.current_frame + 1) % len(self.assets.bird_frames)
            self.animation_timer = 0
    
    def draw(self, screen):
        bird_angle = math.sin(self.timer * self.oscillation_speed) * 20
        rotated_bird = pygame.transform.rotate(self.assets.bird_frames[self.current_frame], bird_angle)
        screen.blit(rotated_bird, 
                   (self.x - rotated_bird.get_width()//2, 
                    self.y - rotated_bird.get_height()//2))
    
    def get_rect(self):
        return pygame.Rect(self.x - self.width//3, self.y - self.height//3, 
                          self.width*2//3, self.height*2//3)


