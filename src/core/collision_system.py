import pygame

class CollisionSystem:
    def check(self, head, groups):
        for group in groups:
            if pygame.sprite.spritecollide(head, group, False):
                return True
        return False
