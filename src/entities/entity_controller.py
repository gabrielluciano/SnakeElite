from abc import ABC, abstractmethod

class EntityController(ABC):
    @abstractmethod
    def handle_event(self, event):
        pass

    @abstractmethod
    def update_entity_position(self, dt, screen):
        pass