import pygame
from config import Parameters
from utils.utils import Utils


class Scene():
    """Superclass scene object for scene subclasses."""

    def __init__(self,
                 name: str,
                 index: int,
                 settings: Parameters,
                 background: pygame.Surface = None) -> None:
        self.name = name
        self.index = index
        self.settings = settings
        self.utils = Utils(settings)
        self.background = background
        self.objects = []

    def initialize(self) -> None:
        """Initializes the class."""
        return NotImplementedError("Subclass must define this.")

    def event(self) -> None:
        return NotImplementedError("Subclass must define this.")

    def update(self) -> None:
        """Update the  class"""
        return NotImplementedError("Subclass must define this.")
