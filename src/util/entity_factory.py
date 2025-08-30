from src.entities.food import Food
from src.core.constants import WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE

class EntityFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_entity(entity_type):
        if entity_type == "Food":
            return Food("assets/food.png", WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
        else:
            raise ValueError(f"Unknown entity type: {entity_type}")
