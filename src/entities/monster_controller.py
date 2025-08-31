from src.entities.entity_controller import EntityController
from src.util.entity_factory import EntityFactory
from src.core.constants import MONSTER_ASSETS
import random
import pygame

class MonsterController(EntityController):
    def __init__(self, sprite_group, num_monsters=3):
        self.sprite_group = sprite_group
        self.num_monsters = num_monsters
        self.monsters = []
        self.spawn_delay = 2  # seconds between monster spawns
        self.time_since_last_spawn = 0
        self.current_level = 1
        
        # Spawn first monster
        self.spawn_monster()
        
    def spawn_monster(self):
        if len(self.monsters) < self.num_monsters:
            monster_asset = random.choice(MONSTER_ASSETS[:self.current_level])
            monster = EntityFactory.create_entity("Monster", image_path=monster_asset)
            self.monsters.append(monster)
            self.sprite_group.add(monster)
            
    def handle_event(self, event):
        # No event handling needed for monsters
        pass
        
    def update(self, dt):
        # Update spawn timer
        self.time_since_last_spawn += dt
        
        # Check if it's time to spawn a new monster
        if self.time_since_last_spawn >= self.spawn_delay:
            self.spawn_monster()
            self.time_since_last_spawn = 0
            
        # Update monsters and remove those that are off screen
        for monster in self.monsters[:]:  # Create a copy to safely remove while iterating
            monster.update(dt)
            if monster.is_off_screen():
                monster.kill()  # Remove from sprite group
                self.monsters.remove(monster)
                
    def check_snake_collision(self, snake):
        # Optional: Check for collisions with snake segments
        for monster in self.monsters:
            for segment in snake.body:
                if pygame.sprite.collide_mask(monster, segment):
                    return True
        return False

    def set_level(self, level):
        self.current_level = level
