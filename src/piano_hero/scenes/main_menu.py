import pygame
from scenes.scene import Scene  # type: ignore
from objects import button  # type: ignore


class MainMenu(Scene):
    def __init__(self, screen: pygame.Surface) -> None:
        self.index = 0
        self.name = "MAIN MENU"
        self.screen = screen
        self.initialize()

    def initialize(self) -> None:
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

        self.objects.append(button.Button(settings=self.settings,
                                          pos=(x / 2, 3 * y / 9),
                                          text_input="PLAY",
                                          font=self.utils.get_font(o_f_s)))
        self.objects.append(button.Button(settings=self.settings,
                                          pos=(x / 2, 5 * y / 9),
                                          text_input="OPTIONS",
                                          font=self.utils.get_font(o_f_s)))
        self.objects.append(button.Button(settings=self.settings,
                                          pos=(x / 2, 7 * y / 9),
                                          text_input="QUIT",
                                          font=self.utils.get_font(o_f_s)))

    def event(self, events: list[str]) -> None:
        print("Event triggered!")
        return 0

    def update(self, screen: pygame.Surface) -> None:
        print("Updating main menu.")
        return 0
