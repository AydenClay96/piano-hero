import pygame
from objects import button, text  # type: ignore
from scenes import scene  # type: ignore


class Settings(scene.Scene):
    """Options screen of the pygame."""

    def initialize(self, screen: pygame.Surface) -> None:
        x, y = screen.get_size()
        t_f_s = int((x + y) / 20)
        o_f_s = int(t_f_s * 0.8)

        self.objects.append(text.Text(name="title",
                                      settings=self.settings,
                                      position=(x / 2, y / 9)))
        self.objects[-1].initialize(text_input="OPTIONS",
                                    font=self.utils.get_font(t_f_s))

        self.objects.append(button.Button(name="save",
                                          settings=self.settings,
                                          position=(x / 6, 8 * y / 9)))
        self.objects[-1].initialize(text_input="SAVE",
                                    font=self.utils.get_font(o_f_s))
