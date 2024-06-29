import pygame
import sys


class EventHandler:
    def __init__(self) -> None:
        pass

    def quit(self) -> None:
        pygame.quit()
        sys.exit()

    def on_mouse_move(self) -> None:
        pygame.mouse.set_visible(True)

    def on_click(self) -> None:
        return pygame.mouse.get_pos()

    def on_key_press(self) -> None:
        pygame.mouse.set_visible(False)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            self.quit()
        if pressed[pygame.K_w] or pressed[pygame.K_UP]:
            return "up"
        if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
            return "down"
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            return "left"
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            return "right"
        if pressed[pygame.K_RETURN]:
            return "enter"

    def on_midi_press(self) -> None:
        pygame.mouse.set_visible(False)
        print("NOTE PRESSED.")

    def event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return self.on_click()
            if event.type == pygame.KEYDOWN:
                return self.on_key_press()
            if event.type == pygame.MIDIIN:
                return self.on_midi_press()
            if event.type == pygame.MOUSEMOTION:
                self.on_mouse_move()
