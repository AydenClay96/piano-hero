import pygame
from config import Parameters
from scenes import config, game, main_menu  # type: ignore


class Scenes():
    def __init__(self, settings: Parameters, screen: pygame.Surface) -> None:
        self.settings = settings
        self.screen = screen
        self.initialize()
        self.scene = self.scenes[0]

    def initialize(self) -> None:
        main_background = self.settings.assets["background"]
        self.scenes = [main_menu.MainMenu(name="main_menu",
                                          index=0,
                                          settings=self.settings,
                                          background=main_background)]
        self.scenes.append(game.Game(name="game",
                                     index=1,
                                     settings=self.settings,
                                     background=None))
        self.scenes.append(config.Settings(name="options",
                                           index=2,
                                           background=None,
                                           settings=self.settings))
