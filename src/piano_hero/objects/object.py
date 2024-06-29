import pygame
from config import Parameters


class Object():
    """General Object superclass with useful generic information."""

    def __init__(self, name: str,
                 settings: Parameters,
                 position: tuple[float, float]) -> None:
        self.name = name
        self.settings = settings
        self.position = position

    def update(self, screen: pygame.Surface) -> None:
        return NotImplementedError("Subclass must define this.")
