from constants import *

class Ground:
    """Class quản lý mặt đất"""
    
    def __init__(self, assets):
        self.y = HEIGHT - 100
        self.height = 100
        self.scroll = 0
        self.assets = assets
    
    def update(self):
        self.scroll -= 5
        if self.scroll <= -WIDTH:
            self.scroll = 0
    
    def draw(self, screen):
        screen.blit(self.assets.ground_img, (self.scroll, self.y))
        screen.blit(self.assets.ground_img, (self.scroll + WIDTH, self.y))