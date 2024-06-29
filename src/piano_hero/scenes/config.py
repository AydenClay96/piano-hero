import pygame
from config import Parameters  # type: ignore
from objects import button  # type: ignore
from utils.utils import Utils  # type: ignore


class Settings:
    """Options screen of the pygame."""

    def __init__(self, settings: Parameters, screen: pygame.Surface) -> None:
        self.index = 2
        self.name = "OPTIONS"
        self.settings = settings
        self.screen = screen
        self.background = None
        self.utils = Utils(settings)
        self.configure()

    def configure(self) -> None:
        x, y = self.screen.get_size()
        t_f_s = int((x + y) / 20)
        o_f_s = int(t_f_s * 0.8)

        self.objects = [
            button.Button(
                settings=self.settings,
                index=0,
                pos=(x / 2, y / 9),
                text_input=self.name,
                font=self.utils.get_font(t_f_s),
            )
        ]
        self.objects.append(button.Button(settings=self.settings, index=1,
                                          pos=(x / 6, 8 * y / 9),
                                          text_input="SAVE",
                                          font=self.utils.get_font(o_f_s)))