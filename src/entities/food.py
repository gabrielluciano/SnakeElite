import pygame
import random

class Food(pygame.sprite.Sprite):
    def __init__(self, image_path, map_width, map_height, cell_size):
        super().__init__()
        cell_size = int(cell_size * 1.5)
        self.map_width = map_width
        self.map_height = map_height
        self.cell_size = cell_size * 2

        # Load and scale image
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))

        self.rect = self.image.get_rect()
        self.spawn_random()

    def spawn_random(self):
        # Choose random position aligned to the grid
        grid_x = random.randint(0, (self.map_width // self.cell_size) - 1)
        grid_y = random.randint(0, (self.map_height // self.cell_size) - 1)
        self.rect.topleft = (grid_x * self.cell_size, grid_y * self.cell_size)