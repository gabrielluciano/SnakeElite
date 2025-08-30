import pygame
from src.core.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from src.entities.snake import Snake
from src.entities.snake_controller import SnakeController
from src.util.entity_factory import EntityFactory

class GameLoop:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Game Loop Example")
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.snake = Snake(self.all_sprites, 5)
        self.snake_controller = SnakeController(self.snake)
        bg_image = pygame.image.load("assets/level_1_bg.png").convert()
        self.bg_image = pygame.transform.scale(bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.food = EntityFactory.create_entity("Food")
        self.all_sprites.add(self.food)

    def start(self):
        self.running = True
        dt = 0
        while self.running:
            self.screen.blit(self.bg_image, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.snake_controller.handle_event(event)

            self.snake_controller.update(dt)
            self.all_sprites.draw(self.screen)

            own_collision_detected = self.snake_controller.check_collision()
            if own_collision_detected:
                self.running = False

            food_collision_detected = self.snake_controller.check_food_collision(self.food)
            if food_collision_detected:
                self.snake.grow(self.all_sprites)
                self.food.spawn_random()
            
            pygame.display.flip()
            dt = self.clock.tick(FPS) / 1000

        pygame.quit()
