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
        img = pygame.image.load(Settings.ENEMY_SHIP_IMG).convert_alpha()
        img = pygame.transform.scale(img, (Settings.SCREEN_WIDTH // 7, Settings.SCREEN_WIDTH // 7))
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
        self.ship_health = 100

    def load_ship_sprite(self, flipped: bool = False):
        """
        Gets the image of the ship.
        """
        img = pygame.image.load(Settings.PLAYER_SHIP_IMG).convert_alpha()
        img = pygame.transform.scale(img, (int(2 * Settings.SCREEN_WIDTH // 3.6), int(Settings.SCREEN_WIDTH // 3.6)))
        return pygame.transform.flip(img, flipped, False)
