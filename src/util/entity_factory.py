from src.entities.food import Food
from src.entities.monster import Monster
from src.core.constants import WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE

class EntityFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_entity(entity_type, **kwargs):
        if entity_type == "Food":
            return Food("assets/food.png", WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
        elif entity_type == "Monster":
            return Monster(**kwargs)
        else:
            raise ValueError(f"Unknown entity type: {entity_type}")
