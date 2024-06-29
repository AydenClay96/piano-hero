from scenes import game, main_menu, config  # type: ignore
from config import Parameters


class Scenes():
    def __init__(self, settings: Parameters) -> None:
        self.initialize()
        self.settings = settings

    def initialize(self) -> None:
        main_background = self.settings.assets["background"]
        self.scenes = [main_menu.MainMenu(name="PIANOHERO",
                                          background=main_background,
                                          settings=self.settings)]
        self.scenes.append(game.Game(name="PIANOHERO",
                                     background=None,
                                     settings=self.settings))
        self.scenes.append(config.Settings(name="OPTIONS",
                                           background=None,
                                           settings=self.settings))
