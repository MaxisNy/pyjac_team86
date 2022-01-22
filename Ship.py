from __future__ import annotations
from typing import Tuple
from load_img import load_image
import pygame
import Settings


class Ship(pygame.sprite.Sprite):
    """
    This class represents a ship in the game.
    """
    def __init__(self, flipped: bool = False) -> None:
        """
        Create an instance of a ship.
        """
        super().__init__()
        self.image = self.load_ship_sprite(flipped)
        self.rect = self.image.get_rect()

    def load_ship_sprite(self, flipped: bool = False):
        """
        Gets the image of the ship.
        """
        raise NotImplementedError

    @ staticmethod
    def initialize_game_ships() -> Tuple[EnemyShip, PlayerShip, EnemyShip]:
        """
        Initializes all the game ships.
        """
        left_ship = EnemyShip()
        main_ship = PlayerShip()
        right_ship = EnemyShip(True)
        distance_from_wall = Settings.SCREEN_WIDTH / 40
        enemy_ship_size_x = right_ship.rect.size[0]
        player_ship_size_x = main_ship.rect.size[0]
        player_ship_size_y = main_ship.rect.size[1]
        left_ship.rect.x = distance_from_wall
        left_ship.rect.y = (Settings.SCREEN_HEIGHT / 2)
        right_ship.rect.x = \
            (Settings.SCREEN_WIDTH - distance_from_wall - enemy_ship_size_x)
        right_ship.rect.y = (Settings.SCREEN_HEIGHT / 2)
        main_ship.rect.x = (Settings.SCREEN_WIDTH / 2) - player_ship_size_x / 2
        main_ship.rect.y = (Settings.SCREEN_HEIGHT // 1.4)
        return left_ship, main_ship, right_ship


class EnemyShip(Ship):
    """
    This class represents an enemy ship in the game.
    """
    def __init__(self, flipped: bool = False) -> None:
        """
        Create an instance of an enemy ship.
        """
        super().__init__(flipped)

    def load_ship_sprite(self, flipped: bool = False):
        """
        Gets the image of the ship.
        """
        img = load_image(Settings.ENEMY_SHIP_IMG, (int(Settings.SCREEN_WIDTH / 6.3)), int(Settings.SCREEN_WIDTH / 6.3))
        return pygame.transform.flip(img, flipped, False)


class PlayerShip(Ship):
    """
    This class represents the ship that the player must protect.
    """
    def __init__(self) -> None:
        """
        Create an instance of a player ship.
        """
        super().__init__()
        self.ship_health = 5

    def load_ship_sprite(self, flipped: bool = False):
        """
        Gets the image of the ship.
        """
        img = load_image(Settings.PLAYER_SHIP_IMG, int(5.4 * Settings.SCREEN_WIDTH // 11), int(Settings.SCREEN_WIDTH // 11))
        return pygame.transform.flip(img, flipped, False)

    @staticmethod
    def load_ship_background():
        """
        Loads the background image of the ship
        """
        return load_image(Settings.PLAYER_SHIP_BG_IMG,
                          int(2 * Settings.SCREEN_WIDTH // 4),
                          int(Settings.SCREEN_WIDTH // 4))

    def damage(self, sprite: pygame.Sprite.sprite) -> None:
        """
        Lowers ship_health if the ship is damaged.
        """
        if self.is_hit(sprite):
            self.ship_health -= 1

    def is_hit(self, sprite: pygame.Sprite.sprite) -> bool:
        """
        Returns whether the ship has been hit
        """
        if self.rect.colliderect(sprite.rect):
            return True
        return False

    def get_ship_health(self) -> int:
        """
        Returns the current ship_health
        """
        return self.ship_health
