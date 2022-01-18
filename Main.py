import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (40, 40, 40)
LIGHT_GRAY = (100, 100, 100)
ORANGE = (255, 165, 0)
GREEN = (0, 128, 0)
RED = (100, 0, 0)
BLUE = (30, 144, 255)
DARK_BLUE = (0, 0, 205)
PURPLE = (102, 0, 204)
YELLOW = (255, 255, 0)


class Screen:
    """
    The main screen for the game.
    """
    SCREEN_WIDTH: int
    SCREEN_HEIGHT: int
    screen: pygame.surface
    game_running: bool

    def __init__(self) -> None:
        """
        Initializes the screen
        """
        self.SCREEN_WIDTH = 750
        self.SCREEN_HEIGHT = 750
        self.game_running = True
        pygame.init()
        pygame.display.set_caption("HackathonGame")
        self.screen = \
            pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def run_game(self):
        """
        Responsible for running the main loop of the game.
        """
        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    pygame.quit()
            self.screen.fill(DARK_GRAY)
            pygame.display.update()


if __name__ == '__main__':
    screen = Screen()
    screen.run_game()
