from objects.object import Object
import pygame


class Text(Object):
    """Text class from the object superclass"""

    def initialize(self, text_input: str, font: pygame.font.Font) -> None:
        self.text_input = text_input
        self.font = font
        self.color = self.settings.font_base_colour
        self.text = self.font.render(self.text_input, True, self.color)
        self.rect = self.text.get_rect(center=self.position)
        self.padding = self.settings.padding
        self.alpha = self.settings.alpha

    def update(self, screen: pygame.Surface) -> None:
        horz = self.rect.right - self.rect.left + self.padding
        vert = self.rect.bottom - self.rect.top + self.padding
        s = pygame.Surface(size=(horz, vert))
        s.set_alpha(self.alpha)
        s.fill((0, 0, 0))
        s_pos = (self.rect[0] - self.padding / 2,
                 self.rect[1] - self.padding / 2)
        screen.blit(s, s_pos)
        screen.blit(self.text, self.rect)
