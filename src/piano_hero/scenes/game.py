import pygame
from config import Parameters  # type: ignore
from objects import button  # type: ignore
from utils.utils import Utils


class Game:
    """Game class that initializes and runs the core game processes."""

    def __init__(self, settings: Parameters, screen: pygame.Surface) -> None:
        self.index = 1
        self.name = "PianoHero"
        self.settings = settings
        self.utils = Utils(settings)
        self.screen = screen
        self.background = None
        self.play()

    def play(self) -> None:
        x, y = self.screen.get_size()
        t_f_s = int((x + y) / 20)

        self.objects = [
            button.Button(
                settings=self.settings,
                index=0,
                pos=(x / 2, y / 9),
                text_input=self.name,
                font=self.utils.get_font(t_f_s),
            )
        ]
