import pygame
from src.core.scene import Scene
from src.scenes.game_scene import GameScene
from src.scenes.scoreboard_scene import ScoreboardScene
from src.core.constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, MENU_FONT_SIZE, MENU_FONT_COLOR, 
    MENU_SELECTED_COLOR, PRIMARY_FONT_PATH, GAME_TITLE_FONT_SIZE,
    GAME_TITLE_COLOR
)
from src.util.ui_utils import draw_creator_legend

class MenuScene(Scene):
    def __init__(self):
        self.title_font = pygame.font.Font(PRIMARY_FONT_PATH, GAME_TITLE_FONT_SIZE)
        self.font = pygame.font.Font(PRIMARY_FONT_PATH, MENU_FONT_SIZE)
        self.options = ["Start Game", "Scoreboard"]
        self.selected_option = 0
        self.next_scene = None
        
        # Load and scale background image
        bg_image = pygame.image.load("assets/menu.png").convert()
        self.bg_image = pygame.transform.scale(bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                if self.selected_option == 0:
                    self.next_scene = GameScene()
                elif self.selected_option == 1:
                    self.next_scene = ScoreboardScene()

    def update(self, dt):
        # No update logic needed for the menu
        return True

    def draw(self, screen):
        screen.blit(self.bg_image, (0, 0))
        
        # Draw title
        title_text = self.title_font.render("SnakeElite", True, GAME_TITLE_COLOR)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH / 2, 150))
        screen.blit(title_text, title_rect)
        
        for i, option in enumerate(self.options):
            color = MENU_SELECTED_COLOR if i == self.selected_option else MENU_FONT_COLOR
            text = self.font.render(option, True, color)
            text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, 350 + i * 100))
            screen.blit(text, text_rect)
            
        draw_creator_legend(screen)
