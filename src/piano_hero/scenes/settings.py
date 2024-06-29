class Settings:
    """Options screen of the pygame."""
    def __init__(self, settings, screen) -> None:
        self.settings = settings
        self.screen = screen
        self.background = None

    # while True:
    #     self.screen.fill("Black")

    #     menu_mouse_pos = pygame.mouse.get_pos()

    #     options_button = Button(pos=(640,100), text_input = "OPTIONS", font=self.get_font(75),
    #                             base_color="#b68f40", hovering_color="#b68f40")
    
    #     save_button = Button(pos=(200, 600), text_input = "SAVE", font=self.get_font(30),
    #                             base_color="#b68f40", hovering_color="White")
        
    #     for button in [options_button, save_button]:
    #         button.changeColor(menu_mouse_pos)
    #         button.update(self.screen)
    #         button.update(self.screen)
        
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             if save_button.checkForInput(menu_mouse_pos):
    #                 self.save()
        
    #     pygame.display.update()