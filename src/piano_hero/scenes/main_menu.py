from objects import button
from utils.utils import Utils


class MainMenu:
    def __init__(self, settings, screen) -> None:
        self.name = "MAIN MENU"
        self.settings = settings
        self.screen = screen
        self.background = self.settings.assets["background"]
        self.utils = Utils(self.settings)
        self.main_menu()

    def main_menu(self) -> None:
        x, y = self.screen.get_size()
        title_font_size = int((x + y) / 20)
        option_font_size = int(title_font_size * 0.8)

        """Main menu of the pygame."""
        self.buttons = [
            button.Button(
                settings=self.settings,
                index=0,
                pos=(x / 2, y / 9),
                text_input=self.name,
                font=self.utils.get_font(title_font_size),
            )
        ]
        self.buttons.append(button.Button(settings=self.settings, index=1,
                                          pos=(x / 2, 3 * y / 9),
                                          text_input="PLAY",
                                          font=self.utils.get_font(option_font_size)))
        self.buttons.append(button.Button(settings=self.settings, index=2,
                                          pos=(x / 2, 5 * y / 9),
                                          text_input="OPTIONS",
                                          font=self.utils.get_font(option_font_size)))
        self.buttons.append(button.Button(settings=self.settings, index=3,
                                          pos=(x / 2, 7 * y / 9),
                                          text_input="QUIT",
                                          font=self.utils.get_font(option_font_size)))
