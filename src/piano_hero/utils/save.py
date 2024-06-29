from dataclasses import dataclass


@dataclass
class Settings:
    """General config file with defaults for the game."""
    user: str = "default"
    scale: str = "C"
    issharp: bool = False
    isminor: bool = False
    tempo: int = 60
    midi: bool = False
    ledger_lines: int = 0


class Config():
    """Class for saving the provided data."""
    def __init__(self):
        self.settings = Settings()

    def save(self) -> None:

        question_button = Button(pos=(640, 300), text_input = "SAVE CHANGES?", font=self.get_font(75),
                                base_color="#b68f40", hovering_color="b68f40")
        yes_button = Button(pos=(500, 400), text_input = "YES", font=self.get_font(40),
                                base_color="#b68f40", hovering_color="White")
        no_button = Button(pos=(780, 400), text_input = "NO", font=self.get_font(40),
                                base_color="#b68f40", hovering_color="White")

        while True:
            self.screen.fill("Black")

            menu_mouse_pos = pygame.mouse.get_pos()
            
            for button in [question_button, yes_button, no_button]:
                    button.changeColor(menu_mouse_pos)
                    button.update(self.screen)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if yes_button.checkForInput(menu_mouse_pos):
                        print("SAVED!")   
                    if no_button.checkForInput(menu_mouse_pos):
                        print("NOT SAVED!")
                    self.main_menu()
            
            pygame.display.update()
