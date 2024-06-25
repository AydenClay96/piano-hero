import pygame


class Obj:
    """Base class for all entities."""
    def __init__(self):
        pass


class App:
    """Main application of piano_hero
    """
    def __init__(self) -> None:
        pygame.init()
        self.prepare()

    def prepare(self) -> None:
        """Configures and shows the screen."""
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.screen.fill("white")
        self.running = True
        self.main()

    def logic(self) -> None:
        """Organizes the game logic."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render(self) -> None:
        """Controls the rendering."""
        player_pos = pygame.Vector2(self.screen.get_width()/2,
                                    self.screen.get_height()/2)
        pygame.draw.circle(self.screen, "red", player_pos, 40)
        pygame.display.flip()

    def main(self) -> None:
        """Main game loop"""
        while self.running:
            self.logic()
            self.render()
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    app = App()
