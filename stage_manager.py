from constants import *

class GameStateManager:
    """Class quản lý trạng thái game"""
    
    def __init__(self):
        self.state = MENU
    
    def set_state(self, new_state):
        self.state = new_state
    
    def is_menu(self):
        return self.state == MENU
    
    def is_playing(self):
        return self.state == PLAYING
    
    def is_game_over(self):
        return self.state == GAME_OVER
    
    def is_paused(self):
        return self.state == PAUSED