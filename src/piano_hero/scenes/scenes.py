import pygame
from config import Parameters
from scenes import config, game, main_menu  # type: ignore


class Scenes():
    def __init__(self, settings: Parameters) -> None:
        self.initialize()
        self.settings = settings
        self.scene = self.scenes[0]

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

    def render(self, screen: pygame.Surface) -> None:
        pass
