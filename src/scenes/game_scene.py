import pygame
from src.core.scene import Scene
from src.core.constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS, SCORE_FONT_SIZE, SCORE_COLOR, 
    SCORE_POSITION, SCORE_INCREMENT, INITIAL_SNAKE_LENGTH,
    LEVEL_THRESHOLDS, MAX_LEVEL, PRIMARY_FONT_PATH
)
from src.entities.snake import Snake
from src.entities.snake_controller import SnakeController
from src.entities.monster_controller import MonsterController
from src.util.entity_factory import EntityFactory
from src.scenes.game_over_scene import GameOverScene
from src.util.ui_utils import draw_creator_legend

class GameScene(Scene):
    def __init__(self, level=1, score=0, snake=None):
        self.level = level
        self.score = score
        self.font = pygame.font.Font(PRIMARY_FONT_PATH, SCORE_FONT_SIZE)
        
        self.all_sprites = pygame.sprite.Group()
        
        if snake:
            self.snake = snake
            self.snake.sprite_group = self.all_sprites
            for segment in self.snake.body:
                self.all_sprites.add(segment)
        else:
            self.snake = EntityFactory.create_entity("Snake", sprite_group=self.all_sprites, initial_length=INITIAL_SNAKE_LENGTH)
            
        self.snake_controller = SnakeController(self.snake)
        self.monster_controller = MonsterController(self.all_sprites)
        self.monster_controller.set_level(self.level)
        
        bg_image_path = f"assets/level_{self.level}_bg.png"
        try:
            bg_image = pygame.image.load(bg_image_path).convert()
        except pygame.error:
            # Fallback to level 1 bg if a level's bg is missing
            bg_image = pygame.image.load("assets/level_1_bg.png").convert()
            
        self.bg_image = pygame.transform.scale(bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.food = EntityFactory.create_entity("Food")
        self.all_sprites.add(self.food)
        
        self.next_scene = None

    def handle_event(self, event):
        self.snake_controller.handle_event(event)

    def update(self, dt):
        self.snake_controller.update(dt)
        self.monster_controller.update(dt)

        if self.snake_controller.check_collision() or self.monster_controller.check_snake_collision(self.snake):
            self.next_scene = GameOverScene(self.score)
            return True

        if self.snake_controller.check_food_collision(self.food):
            self.snake.grow(self.all_sprites)
            self.food.spawn_random()
            self.score += SCORE_INCREMENT
            self.check_level_up()
            
        return True

    def draw(self, screen):
        screen.blit(self.bg_image, (0, 0))
        self.all_sprites.draw(screen)
        score_text = self.font.render(f"Score: {self.score}  Level: {self.level}", True, SCORE_COLOR)
        screen.blit(score_text, SCORE_POSITION)
        draw_creator_legend(screen)

    def check_level_up(self):
        if self.level < MAX_LEVEL and self.score >= LEVEL_THRESHOLDS[self.level]:
            next_level = self.level + 1
            self.next_scene = GameScene(level=next_level, score=self.score, snake=self.snake)
