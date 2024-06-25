import pygame


class App:
    """Main application of piano_hero
    """
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.screen.fill("purple")
        self.running = True
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)

    def main(self) -> None:
        """Main game loop"""
        while self.running:
            pygame.draw.circle(self.screen, "red", self.player_pos, 40)
            pygame.display.flip()
            self.clock.tick(10)
        pygame.quit()


if __name__ == "__main__":
    app = App()
