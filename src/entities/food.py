import pygame
import random
import math


class Food(pygame.sprite.Sprite):
    def __init__(self, image_path, map_width, map_height, cell_size):
        super().__init__()

        # keep a sensible base cell size for the food graphic
        cell_size = int(cell_size * 1.5)
        self.map_width = map_width
        self.map_height = map_height
        # used for grid alignment
        self.cell_size = cell_size * 2

        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.base_size = cell_size
        self.image = pygame.transform.smoothscale(self.original_image, (self.base_size, self.base_size))

        self.rect = self.image.get_rect()

        # Pulse animation parameters
        # amplitude: max fractional change from base size (e.g. 0.15 => +/-15%)
        self.pulse_amplitude = 0.12
        # speed: radians per millisecond multiplier for the sine wave
        self.pulse_speed = 0.006

        # spawn at a random grid-aligned position
        self.spawn_random()

    def spawn_random(self):
        # Choose random position aligned to the grid
        grid_x = random.randint(0, max(0, (self.map_width // self.cell_size) - 1))
        grid_y = random.randint(0, max(0, (self.map_height // self.cell_size) - 1))
        self.rect.topleft = (grid_x * self.cell_size, grid_y * self.cell_size)

    def update(self, *args):
        # compute oscillation based on current time
        t = pygame.time.get_ticks()
        scale_factor = 1.0 + self.pulse_amplitude * math.sin(t * self.pulse_speed)

        # compute new size (ensure at least 1 px)
        new_size = max(1, int(self.base_size * scale_factor))

        # preserve center so the sprite doesn't jump around
        center = self.rect.center

        # smoothscale from the original image for best quality
        try:
            self.image = pygame.transform.smoothscale(self.original_image, (new_size, new_size))
        except Exception:
            # fallback to simple scale if smoothscale is not available for some surfaces
            self.image = pygame.transform.scale(self.original_image, (new_size, new_size))

        self.rect = self.image.get_rect()
        self.rect.center = center