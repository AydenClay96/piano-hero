import pygame
from typing import Optional
from config import Parameters  # type: ignore


class Button():
    def __init__(self,
                 settings: Parameters,
                 index: int,
                 pos: tuple[float, float],
                 text_input: str,
                 font: pygame.font.Font,
                 padding: Optional[int] = 10,
                 alpha: Optional[int] = 10,
                 selectable: Optional[bool] = True):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.index = index
        self.selected = False
        self.font = font
        self.settings = settings
        self.color = self.settings.font_base_colour
        self.text_input = text_input
        self.text = self.font.render(
            self.text_input, True, self.color)  # type: ignore
        self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.padding = padding
        self.alpha = alpha
        self.selectable = selectable

    def update(self, screen: pygame.Surface) -> None:
        horizontal = self.rect.right - self.rect.left
        + self.padding  # type: ignore
        vertical = self.rect.bottom - self.rect.top
        + self.padding  # type: ignore
        s = pygame.Surface(size=(horizontal, vertical))
        s.set_alpha(self.alpha)
        s.fill((0, 0, 0))
        screen.blit(s, (self.rect[0] - self.padding /  # type: ignore
                    2, self.rect[1] - self.padding / 2))  # type: ignore
        screen.blit(self.text, self.rect)

    def check_hover(self, position: tuple[float, float]) -> None:
        self.selected = position[0] in range(
            self.rect.left, self.rect.right
        ) and position[1] in range(self.rect.top, self.rect.bottom)

    def change_color(self) -> None:
        if self.selected:
            self.color = self.settings.font_hover_colour
        else:
            self.color = self.settings.font_base_colour
        self.text = self.font.render(self.text_input, True, self.color)
