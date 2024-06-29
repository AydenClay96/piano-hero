import pygame
from config import Parameters
from scenes import game, main_menu, settings
from utils import event_handler
import logging
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
        self.scenes["main_menu"] = main_menu.MainMenu(self.settings, self.screen)
        self.scenes["settings"] = settings.Settings(self.settings, self.screen)
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
                if out == "up":
                    old_selection = self.selected
                    self.selected -= 1
                    if self.selected == 0:
                        self.selected = len(self.scene.buttons) - 1
                if out == "down":
                    old_selection = self.selected
                    self.selected += 1
                    if self.selected == len(self.scene.buttons):
                        self.selected = 1
                self.scene.buttons[self.selected].selected = True
                self.scene.buttons[old_selection].selected = False
                print(self.selected)
            else:
                # Mouse click.
                pass

            for button in self.scene.buttons:
                if pygame.mouse.get_visible:
                    mouse_pos = pygame.mouse.get_pos()
                    button.check_hover(mouse_pos)
                    button.change_color()

            # View
            self.render()
    
    def render(self) -> None:
        # Get current scene.
        scene = self.scene

        # Clear screen and render background.
        self.screen.fill("black")
        if scene.background is not None:
            self.screen.blit(scene.background, (0, 0))

        # Render objects.
        for button in self.scene.buttons:
            button.update(self.screen)

        # Update the display.
        pygame.display.update()

if __name__ == "__main__":
    main = Main()
