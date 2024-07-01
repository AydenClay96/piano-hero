import pygame
from objects.object import Object  # type: ignore
from objects.text import Text


class Button(Object):

    def initialize(self, text_input: str, font: pygame.font.Font) -> None:
        self.text_obj = Text(name=self.name,
                             settings=self.settings,
                             position=self.position)
        self.text_obj.initialize(text_input=text_input,
                                 font=font)

    def update(self, screen: pygame.Surface) -> None:
        self.text_obj.update(screen)

    def check_hover(self, position: tuple[float, float]) -> None:
        return position[0] in range(
            self.text_obj.rect.left, self.text_obj.rect.right
        ) and position[1] in range(
            self.text_obj.rect.top, self.text_obj.rect.bottom)

    def change_color(self, selected: bool) -> None:
        if selected:
            self.color = self.settings.font_hover_colour
        else:
            self.color = self.settings.font_base_colour
        self.text = self.text_obj.font.render(
            self.text_obj.text_input, True, self.color)
