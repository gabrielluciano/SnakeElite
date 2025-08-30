import pygame
from src.core.constants import Direction
from src.entities.entity_controller import EntityController

class SnakeController(EntityController):
    def __init__(self, snake):
        self.snake = snake
        self.direction = snake.get_last_direction()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.direction = Direction.UP
            elif event.key == pygame.K_s:
                self.direction = Direction.DOWN
            elif event.key == pygame.K_a:
                self.direction = Direction.LEFT
            elif event.key == pygame.K_d:
                self.direction = Direction.RIGHT

    def update(self, dt):
        keys = pygame.key.get_pressed()

        fast = (keys[pygame.K_w] and self.direction == Direction.UP) or \
                (keys[pygame.K_s] and self.direction == Direction.DOWN) or \
                (keys[pygame.K_a] and self.direction == Direction.LEFT) or \
                (keys[pygame.K_d] and self.direction == Direction.RIGHT)

        self.snake.move(dt, fast, self.direction)

    def check_collision(self):
        return self.snake.check_self_collision()