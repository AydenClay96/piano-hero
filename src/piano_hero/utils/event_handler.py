import sys

import pygame


class EventHandler:
    def __init__(self) -> None:
        pass

    def quit(self) -> None:
        pygame.quit()
        sys.exit()

    def on_mouse_move(self) -> None:
        pygame.mouse.set_visible(True)

    def on_key_press(self) -> None:
        pygame.mouse.set_visible(False)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            self.quit()

    def on_midi_press(self) -> None:
        pygame.mouse.set_visible(False)
        print("NOTE PRESSED.")

    def event(self, event) -> None:
        if event.type == pygame.QUIT:
            self.quit()
        if event.type == pygame.MIDIIN:
            return self.on_midi_press()
        if event.type == pygame.KEYDOWN:
            self.on_key_press()
        if event.type == pygame.MOUSEMOTION:
            self.on_mouse_move()
