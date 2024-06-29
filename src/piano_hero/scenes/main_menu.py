from objects import button  # type: ignore
from config import Parameters  # type: ignore
from utils.utils import Utils  # type: ignore
import pygame


class MainMenu:
    def __init__(self, settings: Parameters, screen: pygame.Surface) -> None:
        self.index = 0
        self.name = "MAIN MENU"
        self.settings = settings
        self.screen = screen
        self.background = self.settings.assets["background"]
        self.utils = Utils(self.settings)
        self.main_menu()

    def main_menu(self) -> None:
        """Main menu of the pygame."""
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
                                          pos=(x / 2, 3 * y / 9),
                                          text_input="PLAY",
                                          font=self.utils.get_font(o_f_s),
                                          selectable=False))
        self.objects.append(button.Button(settings=self.settings, index=2,
                                          pos=(x / 2, 5 * y / 9),
                                          text_input="OPTIONS",
                                          font=self.utils.get_font(o_f_s)))
        self.objects.append(button.Button(settings=self.settings, index=3,
                                          pos=(x / 2, 7 * y / 9),
                                          text_input="QUIT",
                                          font=self.utils.get_font(o_f_s)))
