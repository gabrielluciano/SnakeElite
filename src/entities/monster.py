import pygame
import random
from src.core.constants import WINDOW_WIDTH, WINDOW_HEIGHT, MONSTER_SPEED

class Monster(pygame.sprite.Sprite):
    SIZE = (100, 100)
    
    def __init__(self, x=None, y=None, image_path="assets/monster_1.png"):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.SIZE)
        self.mask = pygame.mask.from_surface(self.image)
        
        # If no position is provided, start off screen to the right at a random height
        if x is None:
            x = WINDOW_WIDTH
        if y is None:
            y = random.randint(0, WINDOW_HEIGHT - self.SIZE[1])
            
        self.rect = self.image.get_rect(topleft=(x, y))
        
    def update(self, dt):
        # Move left based on speed and delta time
        self.rect.x -= MONSTER_SPEED * dt
        
    def is_off_screen(self):
        return self.rect.right < 0  # True if monster has completely left the screen
        
    @staticmethod
    def generate_random_y():
        return random.randint(0, WINDOW_HEIGHT - Monster.SIZE[1])