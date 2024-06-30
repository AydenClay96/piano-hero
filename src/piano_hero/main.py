import contextlib
import logging

import pygame
from config import Parameters  # type: ignore
from objects import button
from scenes import game, main_menu  # type: ignore
from utils import event_handler  # type: ignore

from scenes import config

logger = logging.getLogger(__name__)


class Main():
    """Main class for the piano-hero game."""

    def __init__(self) -> None:
        logging.basicConfig(filename="game.log", level=logging.INFO)
        logger.info("Beginning initialization phase.")
        self.init_game()
        self.init_settings()
        self.init_screen()
        self.init_scenes()
        self.init_event_handler()
        logger.info("Initialization complete.")
        self.run()

    def init_game(self) -> None:
        logger.info("Initializing pygame.")
        pygame.init()

    def init_settings(self) -> None:
        logger.info("Initializing configuration.")
        self.settings = Parameters()

    def init_screen(self) -> None:
        logger.info("Initializing screen.")
        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            res = self.settings.resolution
            self.screen = pygame.display.set_mode(res, pygame.RESIZABLE)
        pygame.display.set_caption(self.settings.name)
        pygame.display.set_icon(self.settings.assets["icon"])

    def init_scenes(self) -> None:
        logger.info("Initializing scenes.")
        self.scenes = {}
        self.scenes["main_menu"] = main_menu.MainMenu(self.settings,
                                                      self.screen)
        self.scenes["settings"] = config.Settings(self.settings, self.screen)
        self.scenes["game"] = game.Game(self.settings, self.screen)

    def init_event_handler(self) -> None:
        logger.info("Initializing event handler.")
        self.event_handler = event_handler.EventHandler()

    def run(self) -> None:
        logger.info("Running...")
        self.scene = self.scenes["main_menu"]
        self.selected = 1

        while True:
            out = self.event_handler.event()
            if out in ["up", "down", "left", "right"]:
                # Keyboard input.
                if out == "down":
                    old_selection = self.selected
                    self.selected += 1
                    if self.selected == len(self.scene.objects):
                        self.selected = 1
                elif out == "up":
                    old_selection = self.selected
                    self.selected -= 1
                    if self.selected == 0:
                        self.selected = len(self.scene.objects) - 1
                self.scene.objects[self.selected].selected = True
                self.scene.objects[old_selection].selected = False
            if out == "enter":
                if self.scene.name == "MAIN MENU":
                    if self.selected == 3:
                        self.event_handler.quit()
                    for scene in self.scenes.keys():
                        if self.scenes[scene].index == self.selected:
                            self.scene = self.scenes[scene]
                            break
                elif self.scene.name == "OPTIONS":
                    print("Options Page")
                    self.scene = self.scenes["main_menu"]
                elif self.scene.name == "PianoHero":
                    print("Game Page")
                    self.scene = self.scenes["main_menu"]

            for object in self.scene.objects:
                if isinstance(object, button.Button):
                    if pygame.mouse.get_visible():  # type: ignore
                        mouse_pos = pygame.mouse.get_pos()
                        object.check_hover(mouse_pos)
                    object.change_color()

            # View
            self.render()

    def render(self) -> None:
        # Get current scene.
        scene = self.scene

        # Clear screen and render background.
        self.screen.fill("black")
        if scene.background is not None:
            screen_size = self.screen.get_size()
            background = pygame.transform.scale(scene.background, screen_size)
            self.screen.blit(background, (0, 0))

        # Render objects.
        with contextlib.suppress(AttributeError):
            for object in self.scene.objects:
                object.update(self.screen)

        # Update the display.
        pygame.display.update()


if __name__ == "__main__":
    main = Main()
