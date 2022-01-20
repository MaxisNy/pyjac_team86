from typing import List

import pygame
import Settings
from Ship import Ship, EnemyShip, PlayerShip
from load_img import load_image

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
    actors: pygame.sprite.Group
    background: pygame.image

    def __init__(self) -> None:
        """
        Initializes the screen
        """
        self.SCREEN_WIDTH = Settings.SCREEN_WIDTH
        self.SCREEN_HEIGHT = Settings.SCREEN_HEIGHT
        self.game_running = True
        pygame.init()
        pygame.display.set_caption("HackathonGame")
        self.screen = \
            pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.actors = pygame.sprite.Group()
        self._initialize_actors()
        self.background = load_image(Settings.BACKGROUND_IMG)

    def _initialize_actors(self) -> None:
        """
        Initializes all the game actors
        """
        left_ship = EnemyShip()
        main_ship = PlayerShip()
        right_ship = EnemyShip(True)
        distance_from_wall = self.SCREEN_WIDTH / 40
        enemy_ship_size_x = right_ship.rect.size[0]
        enemy_ship_size_y = right_ship.rect.size[1]
        player_ship_size_x = main_ship.rect.size[0]
        player_ship_size_y = main_ship.rect.size[1]
        left_ship.rect.x = distance_from_wall
        left_ship.rect.y = (self.SCREEN_HEIGHT / 2)
        right_ship.rect.x = (self.SCREEN_WIDTH - distance_from_wall - enemy_ship_size_x)
        right_ship.rect.y = (self.SCREEN_HEIGHT / 2)
        main_ship.rect.x = (self.SCREEN_WIDTH / 2) - player_ship_size_x / 2
        main_ship.rect.y = (self.SCREEN_HEIGHT / 2) - (player_ship_size_y / 6)
        self.actors.add(left_ship, main_ship, right_ship)

    def run_game(self):
        """
        Responsible for running the main loop of the game.
        """
        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    pygame.quit()
            self.screen.blit(self.background, (0, 0))
            self.actors.draw(self.screen)
            pygame.display.update()


if __name__ == '__main__':
    screen = Screen()
    screen.run_game()
