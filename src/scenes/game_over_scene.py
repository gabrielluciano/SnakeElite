import pygame
from src.core.scene import Scene
from src.core.constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, GAME_OVER_FONT_SIZE, GAME_OVER_COLOR,
    SCORE_FONT_SIZE, SCORE_COLOR, PRIMARY_FONT_PATH
)
from src.util.ui_utils import draw_creator_legend
from src.core.db_proxy import DBProxy

class GameOverScene(Scene):
    def __init__(self, score):
        self.score = score
        self.game_over_font = pygame.font.Font(PRIMARY_FONT_PATH, GAME_OVER_FONT_SIZE)
        self.score_font = pygame.font.Font(PRIMARY_FONT_PATH, SCORE_FONT_SIZE)
        self.input_font = pygame.font.Font(PRIMARY_FONT_PATH, 36)
        self.next_scene = None
        self.player_name = ""
        self.input_active = True
        
        bg_image = pygame.image.load("assets/game_over.png").convert()
        self.bg_image = pygame.transform.scale(bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def handle_event(self, event):
        if self.input_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.save_score()
                    self.input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.player_name = self.player_name[:-1]
                else:
                    self.player_name += event.unicode
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            from src.scenes.menu_scene import MenuScene
            self.next_scene = MenuScene()

    def update(self, dt):
        return True

    def draw(self, screen):
        screen.blit(self.bg_image, (0, 0))
        
        game_over_text = self.game_over_font.render("Game Over", True, GAME_OVER_COLOR)
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH / 2, 150))
        screen.blit(game_over_text, game_over_rect)
        
        score_text = self.score_font.render(f"Your Score: {self.score}", True, SCORE_COLOR)
        score_rect = score_text.get_rect(center=(WINDOW_WIDTH / 2, 250))
        screen.blit(score_text, score_rect)

        if self.input_active:
            prompt_text = self.input_font.render("Enter your name:", True, SCORE_COLOR)
            prompt_rect = prompt_text.get_rect(center=(WINDOW_WIDTH / 2, 350))
            screen.blit(prompt_text, prompt_rect)

            input_box = pygame.Rect(WINDOW_WIDTH / 2 - 150, 400, 300, 50)
            pygame.draw.rect(screen, SCORE_COLOR, input_box, 2)
            
            input_surface = self.input_font.render(self.player_name, True, SCORE_COLOR)
            screen.blit(input_surface, (input_box.x + 5, input_box.y + 5))
        else:
            instruction_font = pygame.font.Font(PRIMARY_FONT_PATH, 36)
            instruction_text = instruction_font.render("Press ESC to go back", True, (255, 255, 255))
            screen.blit(instruction_text, (10, 10))

        draw_creator_legend(screen)

    def save_score(self):
        if self.player_name:
            db = DBProxy()
            db.add_score(self.player_name, self.score)
