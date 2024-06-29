class Game:
    """Game class that initializes and runs the core game processes."""
    def __init__(self, settings, screen) -> None:
        self.settings = settings
        self.screen = screen
        self.background = None