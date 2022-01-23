import pygame
import Settings
from load_img import load_image
from Timer import Timer
from typing import Dict


class Player(pygame.sprite.Sprite):
    """
    The Player character class.
    """

    block: bool  # True if the shield is up, False otherwise
    jumping: bool  # True if the Player is currently in the air, False otherwise
    speed_hor: int  # Player's horizontal movement speed
    speed_ver: int  # Player's vertical movement speed
    _timer: Timer
    images: dict
    direction: str

    def __init__(self) -> None:
        """
        The Player constructor.
        """
        super().__init__()
        self.block = False
        self.jumping = False
        self.speed_hor = Settings.PLAYER_BLOCK_DOWN_SPEED
        self.speed_ver = Settings.PLAYER_JUMP_SPEED
        self._timer = Timer()
        self.images = self.generate_player_images()
        self.direction = "LEFT"
        self.rect = self.images["LEFT"].get_rect()
        self.rect.x = Settings.PLAYER_INITIAL_COORDINATES[0]
        self.rect.y = Settings.PLAYER_INITIAL_COORDINATES[1]

    @staticmethod
    def generate_player_images() -> Dict:
        """
        Returns a dictionary of images that relate to
        possible movement directions.
        """
        return {"LEFT": load_image(Settings.PLAYER_IMG,
                                   Settings.SCREEN_WIDTH // 37,
                                   (38 / 24) * Settings.SCREEN_WIDTH // 37),
                "RIGHT": pygame.transform.flip(
                    load_image(Settings.PLAYER_IMG,
                               Settings.SCREEN_WIDTH // 37,
                               (38 / 24) *
                               Settings.SCREEN_WIDTH // 37), True, False),
                "LEFT_JUMP": load_image(Settings.PLAYER_JUMP_IMG,
                                        Settings.SCREEN_WIDTH // 34,
                                        (41 / 35) *
                                        Settings.SCREEN_WIDTH // 34),
                "RIGHT_JUMP": pygame.transform.flip(
                    load_image(Settings.PLAYER_JUMP_IMG,
                               Settings.SCREEN_WIDTH // 34,
                               (41 / 35) *
                               Settings.SCREEN_WIDTH // 34), True, False),
                "LEFT_BLOCK": load_image(Settings.PLAYER_BLOCK_IMG,
                                         Settings.SCREEN_WIDTH // 27,
                                         (31 / 24) *
                                         Settings.SCREEN_WIDTH // 27),
                "RIGHT_BLOCK": pygame.transform.flip(
                    load_image(Settings.PLAYER_BLOCK_IMG,
                               Settings.SCREEN_WIDTH // 27,
                               (31 / 24) *
                               Settings.SCREEN_WIDTH // 27), True, False)}

    def get_x(self):
        """
        Returns Player's x coordinate.
        """
        return self.rect.x

    def get_y(self) -> float:
        """
        Returns Player's y coordinate.
        """
        if self.jumping:
            self.rect.y = Settings.PLAYER_INITIAL_COORDINATES[1] - \
                          (self.speed_ver * self._timer.get_time_elapsed()) + \
                          (Settings.PLAYER_ACCELERATION *
                           (self._timer.get_time_elapsed() ** 2) / 2)

            # end the jump
            if self.rect.y > Settings.PLAYER_INITIAL_COORDINATES[1]:
                self.rect.y = Settings.PLAYER_INITIAL_COORDINATES[1]
                self.jumping = False
                if self.direction == "LEFT_JUMP":
                    self.direction = "LEFT"
                else:
                    self.direction = "RIGHT"

        return self.rect.y

    def get_speed(self):
        """
        Returns Player's horizontal movement speed.
        """
        if self.block:
            return Settings.PLAYER_BLOCK_UP_SPEED
        return Settings.PLAYER_BLOCK_DOWN_SPEED

    def draw(self, screen):
        """
        Draws the Player avatar on the screen.
        """
        screen.blit(self.images[self.direction], (self.get_x(), self.get_y()))

    def move_right(self):
        """
        Moves Player horizontally to the right.
        """
        self.rect.x += self.get_speed()
        if self.jumping:
            self.direction = "RIGHT_JUMP"
        else:
            self.direction = "RIGHT"

    def move_left(self):
        """
        Moves Player horizontally to the left.
        """
        self.rect.x -= self.get_speed()
        if self.jumping:
            self.direction = "LEFT_JUMP"
        else:
            self.direction = "LEFT"

    def jump(self):
        """
        Initializes the jumping movement and changes the Player's direction.
        """
        if not self.jumping:
            self.jumping = True
            self._timer.start()
            if self.direction == "LEFT":
                self.direction = "LEFT_JUMP"
            else:
                self.direction = "RIGHT_JUMP"

    def block_up(self):
        """
        Enables defense. Only possible when the Player is on the ground.
        """
        if not self.jumping:
            self.block = True
            if self.direction == "LEFT":
                self.direction = "LEFT_BLOCK"
            else:
                self.direction = "RIGHT_BLOCK"

    def block_down(self):
        """
        Disables defense.
        """
        self.block = False
