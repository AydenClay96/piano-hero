import pygame
from objects import text  # type: ignore
from scenes import scene


class Game(scene.Scene):

    def initialize(self, screen: pygame.Surface) -> None:
        x, y = screen.get_size()
        t_f_s = int((x + y) / 20)

        self.objects.append(text.Text(name="title",
                                      settings=self.settings,
                                      position=(x / 2, y / 9)))
        self.objects[-1].initialize(text_input="PIANOHERO",
                                    font=self.utils.get_font(t_f_s))
