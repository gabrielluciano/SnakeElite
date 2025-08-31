from src.entities.entity_controller import EntityController
from src.util.entity_factory import EntityFactory


class FoodController(EntityController):
    def __init__(self, sprite_group):
        self.sprite_group = sprite_group
        # create one food and add to the shared sprite group
        self.food = EntityFactory.create_entity("Food")
        self.sprite_group.add(self.food)

    def handle_event(self, event):
        # Food doesn't need event handling for now
        pass

    def update(self, dt):
        # Keep the same pattern as other controllers: forward update to the entity.
        # Food.update may ignore dt; tolerate both signatures.
        try:
            self.food.update(dt)
        except TypeError:
            self.food.update()

    def spawn_food(self):
        self.food.spawn_random()
