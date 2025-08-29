import pygame
from src.core.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, SNAKE_COLOR, Direction
from src.entities.snake import Snake
from src.entities.snake_controller import SnakeController

class GameLoop:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Game Loop Example")
        self.clock = pygame.time.Clock()
        self.entities = self.create_entities()

    def start(self):
        self.running = True
        dt = 0
        while self.running:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                for entity in self.entities:
                    entity.handle_event(event)
            
            for entity in self.entities:
                entity.update_entity_position(dt, self.screen)
            
            pygame.display.flip()
            dt = self.clock.tick(FPS) / 1000

        pygame.quit()

    def create_entities(self):
        entities = []
        entities.append(SnakeController(Snake()))
        return entities