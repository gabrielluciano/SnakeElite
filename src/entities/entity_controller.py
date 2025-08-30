from abc import ABC, abstractmethod

class EntityController(ABC):
    @abstractmethod
    def handle_event(self, event):
        pass

    @abstractmethod
    def update(self, dt):
        pass