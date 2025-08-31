import pygame

def draw_creator_legend(screen):
    from src.core.constants import (
        WINDOW_WIDTH, CREATOR_TEXT, CREATOR_FONT_SIZE, CREATOR_FONT_COLOR
    )
    font = pygame.font.Font(None, CREATOR_FONT_SIZE)
    text = font.render(CREATOR_TEXT, True, CREATOR_FONT_COLOR)
    text_rect = text.get_rect(bottomright=(WINDOW_WIDTH - 10, 710))
    screen.blit(text, text_rect)
