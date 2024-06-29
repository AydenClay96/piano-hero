import pygame
from config import Parameters  # type: ignore


class Utils:
    """Utilities """

    def __init__(self, settings: Parameters) -> None:
        self.settings = settings

    def get_font(self, size: int) -> pygame.font.Font:
        """Ensures the font is rendered in the required size.

        Parameters
        ----------
        size : int
            integer indicator of size in pixels.

        Returns
        -------
        pygame.font.Font
            pygame.font Font class.
            Use with <out>.render(text [str],
            anti-aliasing [bool], color [hex])
        """
        return pygame.font.Font(self.settings.assets["font_path"], size)
