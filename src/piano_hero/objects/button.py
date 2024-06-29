import pygame
from typing import Optional

class Button():
	def __init__(self, settings, index, pos, text_input, font, padding: Optional[int] = 10, alpha: Optional[int] = 10):
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.index = index
		self.selected = False
		self.font = font
		self.settings = settings
		self.color = self.settings.font_base_colour
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.color)
		self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		self.padding = padding
		self.alpha = alpha

	def update(self, screen):
		s = pygame.Surface(size=(self.rect.right - self.rect.left + self.padding, self.rect.bottom - self.rect.top + self.padding))
		s.set_alpha(self.alpha)
		s.fill((0, 0, 0))
		screen.blit(s, (self.rect[0] - self.padding / 2, self.rect[1] - self.padding / 2))
		screen.blit(self.text, self.rect)

	def check_hover(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.selected = True
		else:
			self.selected = False

	def change_color(self):
		if self.selected:
			self.color = self.settings.font_hover_colour
		else:
			self.color = self.settings.font_base_colour
		self.text = self.font.render(self.text_input, True, self.color)