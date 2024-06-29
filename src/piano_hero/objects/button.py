import pygame
from typing import Optional

class Button():
	def __init__(self, pos, text_input, font, base_color, hovering_color, padding: Optional[int] = 10, alpha: Optional[int] = 10):
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		self.padding = padding
		self.alpha = alpha

	def update(self, screen):
		s = pygame.Surface(size=(self.rect.right - self.rect.left + self.padding, self.rect.bottom - self.rect.top + self.padding))
		s.set_alpha(self.alpha)
		s.fill((0, 0, 0))
		screen.blit(s, (self.rect[0] - self.padding / 2, self.rect[1] - self.padding / 2))
		screen.blit(self.text, self.rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)