import logging

import pygame
from config import Parameters  # type: ignore
from scenes import scenes  # type: ignore
from utils import event_handler  # type: ignore

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
        self.clock = pygame.time.Clock()

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
        self.scenes = scenes.Scenes(self.settings, self.screen)
        for scene in self.scenes.scenes:
            scene.initialize(self.screen)

    def init_event_handler(self) -> None:
        logger.info("Initializing event handler.")
        self.event_handler = event_handler.EventHandler()

    def run(self) -> None:
        logger.info("Running...")
        self.scene = self.scenes.scenes[0]

        while True:
            for event in pygame.event.get():
                self.event_handler.event(event)
                self.scene.event(event)
            self.render()
            self.dt = self.clock.tick(60)

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
        scene.update(self.screen)

        # Update the display.
        pygame.display.update()


if __name__ == "__main__":
    main = Main()
