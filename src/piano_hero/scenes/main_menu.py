import pygame
from scenes import scene  # type: ignore
from objects import button, text  # type: ignore


class MainMenu(scene.Scene):

    def initialize(self, screen: pygame.Surface) -> None:
        """Main menu of the pygame."""
        x, y = screen.get_size()
        t_f_s = int((x + y) / 20)
        o_f_s = int(t_f_s * 0.8)

        self.objects.append(text.Text(name="title",
                                      settings=self.settings,
                                      position=(x / 2, y / 9)))
        self.objects[-1].initialize(text_input="PIANOHERO",
                                    font=self.utils.get_font(t_f_s))

        self.objects.append(button.Button(name="play",
                                          settings=self.settings,
                                          position=(x / 2, 3 * y / 9)))
        self.objects[-1].initialize(text_input="PLAY",
                                    font=self.utils.get_font(o_f_s))

        self.objects.append(button.Button(name="options",
                                          settings=self.settings,
                                          position=(x / 2, 5 * y / 9)))
        self.objects[-1].initialize(text_input="OPTIONS",
                                    font=self.utils.get_font(o_f_s))

        self.objects.append(button.Button(name="quit",
                                          settings=self.settings,
                                          position=(x / 2, 7 * y / 9)))
        self.objects[-1].initialize(text_input="QUIT",
                                    font=self.utils.get_font(o_f_s))
        self.selected = 1

    def event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed["K_w"] or pressed["K_up"]:
                self.selected -= 1
                if self.selected == 0:
                    self.selected = 3
            elif pressed["K_s"] or pressed["K_down"]:
                self.selected += 1
                if self.selected == 4:
                    self.selected = 1
        if pygame.mouse.get_visible():
            for object in self.objects:
                if isinstance(object, button.Button):
                    object.change_color(
                        object.check_hover(pygame.mouse.get_pos()))
        else:
            self.objects[self.selected].change_color(True)

    def update(self, screen: pygame.Surface) -> None:
        for object in self.objects:
            object.update(screen)
