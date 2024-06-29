class MainMenu:
    def __init__(self, settings, screen) -> None:
        self.settings = settings
        self.screen = screen
        self.background = self.settings.assets["background"]

    def main_menu(self) -> None:
        """Main menu of the pygame."""
        print("MAIN MENU")

    #     pygame.display.set_caption(self.name)
    #     pygame.display.set_icon(self.icon)

    #     menu_button = Button(pos=(640, 100), text_input = self.name, font=self.get_font(100),
    #                                                     base_color="#b68f40", hovering_color="#b68f40")
    #     play_button = Button(pos=(640, 250), text_input = "PLAY", font=self.get_font(75),
    #                                                     base_color=self.text_color, hovering_color="White")
    #     options_button = Button(pos=(640, 400), text_input = "OPTIONS", font=self.get_font(75),
    #                                                     base_color=self.text_color, hovering_color="White")
    #     quit_button = Button(pos=(640, 550), text_input = "QUIT", font=self.get_font(75),
    #                                                     base_color=self.text_color, hovering_color="White")

    #     while True:
    #         self.screen.fill("Black")
    #         self.screen.blit(self.background, (0, 0))

    #         menu_mouse_pos = pygame.mouse.get_pos()

    #         for button in [menu_button, play_button, options_button, quit_button]:
    #             button.changeColor(menu_mouse_pos)
    #             button.update(self.screen)

    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 sys.exit()
    #             if event.type == pygame.MOUSEBUTTONDOWN:
    #                 if play_button.checkForInput(menu_mouse_pos):
    #                     self.play()
    #                 if options_button.checkForInput(menu_mouse_pos):
    #                     self.options()
    #                 if quit_button.checkForInput(menu_mouse_pos):
    #                     pygame.quit()
    #                     sys.exit()

    #         pygame.display.update()