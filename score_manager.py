import os
from constants import *


class ScoreManager:
    """Class quản lý điểm số"""
    
    def __init__(self):
        self.score = 0
        self.high_score = self.load_high_score()
    
    def load_high_score(self):
        if os.path.exists("highscore.txt"):
            try:
                with open("highscore.txt", "r") as file:
                    return int(file.read())
            except:
                return 0
        return 0
    
    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as file:
                file.write(str(self.high_score))
    
    def add_point(self):
        self.score += 1
    
    def reset(self):
        self.score = 0
    
    def draw(self, screen, assets):
        # Score text with outline
        score_text = assets.font.render(f"Score: {self.score}", True, WHITE)
        score_outline = assets.font.render(f"Score: {self.score}", True, BLACK)
        
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            screen.blit(score_outline, (10 + dx, 10 + dy))
        screen.blit(score_text, (10, 10))
        
        # High score text with outline
        high_score_text = assets.font.render(f"Best: {self.high_score}", True, WHITE)
        high_score_outline = assets.font.render(f"Best: {self.high_score}", True, BLACK)
        
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            screen.blit(high_score_outline, (10 + dx, 50 + dy))
        screen.blit(high_score_text, (10, 50))
