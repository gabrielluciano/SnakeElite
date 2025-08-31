import pygame
from src.core.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from src.scenes.menu_scene import MenuScene

class GameLoop:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Elite")
        self.clock = pygame.time.Clock()
        self.current_scene = MenuScene()

    def start(self):
        running = True
        dt = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.current_scene.handle_event(event)

            if not self.current_scene.update(dt):
                running = False
            
            if self.current_scene.next_scene:
                self.current_scene = self.current_scene.next_scene

            self.current_scene.draw(self.screen)
            pygame.display.flip()
            
            dt = self.clock.tick(FPS) / 1000

        pygame.quit()

