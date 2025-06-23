
class CollisionDetector:
    """Class kiểm tra va chạm"""
    
    @staticmethod
    def check_collision(bird, pipe, ground_y):
        bird_rect = bird.get_rect()
        
        # Check ground collision
        if bird.y + bird.height//2 >= ground_y:
            return True
        
        # Check pipe collision
        top_pipe_rect = pipe.get_top_rect()
        bottom_pipe_rect = pipe.get_bottom_rect()
        
        return bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect)