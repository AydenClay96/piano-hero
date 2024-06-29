import pygame
from config import Parameters
from utils.utils import Utils


class Scene():
    """Superclass scene object for scene subclasses."""

    def __init__(self,
                 name: str,
                 background: pygame.Surface,
                 settings: Parameters) -> None:
        self.name = name
        self.settings = settings
        self.utils = Utils(settings)
        self.background = background
        self.objects = []
        self.selected = None

    def initialize(self, screen: pygame.Surface) -> None:
        """Initializes the class."""
        self.screen = screen
        return NotImplementedError("Subclass must define this.")

    def event(self, events: list[str]) -> None:
        return NotImplementedError("Subclass must define this.")

    def update(self, screen: pygame.Surface) -> None:
        """Update the  class"""
        self.screen = screen
        return NotImplementedError("Subclass must define this.")
