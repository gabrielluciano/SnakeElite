import pygame
from src.core.scene import Scene
from src.core.constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, MENU_FONT_SIZE, MENU_FONT_COLOR,
    PRIMARY_FONT_PATH, SCORE_COLOR
)
from src.util.ui_utils import draw_creator_legend
from src.core.db_proxy import DBProxy

class ScoreboardScene(Scene):
    def __init__(self):
        self.title_font = pygame.font.Font(PRIMARY_FONT_PATH, MENU_FONT_SIZE)
        self.score_font = pygame.font.Font(PRIMARY_FONT_PATH, 36)
        self.next_scene = None
        self.scroll_offset = 0
        
        bg_image = pygame.image.load("assets/menu.png").convert()
        self.bg_image = pygame.transform.scale(bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.db = DBProxy()
        self.scores = self.db.get_scores()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                from src.scenes.menu_scene import MenuScene
                self.next_scene = MenuScene()
            elif event.key == pygame.K_UP:
                self.scroll_offset = max(0, self.scroll_offset - 1)
            elif event.key == pygame.K_DOWN:
                self.scroll_offset = min(len(self.scores) - 10, self.scroll_offset + 1)

    def update(self, dt):
        return True

    def draw(self, screen):
        screen.blit(self.bg_image, (0, 0))
        
        instruction_font = pygame.font.Font(PRIMARY_FONT_PATH, 36)
        instruction_text = instruction_font.render("Press ESC to go back", True, (255, 255, 255))
        screen.blit(instruction_text, (10, 10))

        title_text = self.title_font.render("Scoreboard", True, MENU_FONT_COLOR)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH / 2, 100))
        screen.blit(title_text, title_rect)
        
        for i, (name, score, timestamp) in enumerate(self.scores[self.scroll_offset:self.scroll_offset + 10]):
            score_entry = f"{i+1+self.scroll_offset}. {name}: {score}"
            score_text = self.score_font.render(score_entry, True, SCORE_COLOR)
            score_rect = score_text.get_rect(midleft=(100, 200 + i * 40))
            screen.blit(score_text, score_rect)

        draw_creator_legend(screen)
