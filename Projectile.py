import Settings
from Timer import Timer
from typing import Dict
from load_img import load_image
import pygame
import random
import math


class Projectile(pygame.sprite.Sprite):
    """
    The Projectile class.
    """
    _style = str
    _timer: Timer
    velocity: int
    launched: bool
    side: int
    images: dict

    def __init__(self, side: int):
        """
        The Projectile constructor.
        """
        super().__init__()
        self.velocity = random.randint(200, 250)
        self._timer = Timer()
        self.launched = False
        self._style = "PROJECTILE"
        self.side = side
        self.images = self.generate_projectile_images()
        self.rect = self.images[self._style].get_rect()
        self.rect.x = self.get_init_coords(side)
        self.rect.y = Settings.INITIAL_PROJECTILE_HEIGHT

    @staticmethod
    def generate_projectile_images() -> Dict:
        """
        Returns a dictionary of projectile images that relate
        to different states.
        """
        return {
            "PROJECTILE": load_image(Settings.PROJECTILE_IMG,
                                     (29 / 28) * Settings.SCREEN_WIDTH // 60,
                                     Settings.SCREEN_WIDTH // 60),
            "EXPLOSION": load_image(Settings.EXPLOSION_IMG,
                                    Settings.SCREEN_WIDTH // 60,
                                    (29 / 28) * Settings.SCREEN_WIDTH // 60)}

    @staticmethod
    def get_init_coords(side):
        """
        Returns Projectile x coordinate based on the side it is launched from.
        """
        if side:
            return Settings.SCREEN_WIDTH - 230
        return 225

    def get_x(self, side):
        """
        Returns the x coordinate of this Projectile.
        """
        self.rect.x = self.get_init_coords(side) + ((-1) ** side) * self.velocity * \
                math.cos(Settings.PROJECTILE_ANGLE * math.pi / 180) * \
                self._timer.get_time_elapsed()
        return self.rect.x

    def get_y(self):
        """
        Returns the y coordinate of this Projectile.
        """
        self.rect.y = Settings.INITIAL_PROJECTILE_HEIGHT - \
               self.velocity * math.sin(Settings.PROJECTILE_ANGLE * math.pi / 180) * \
               self._timer.get_time_elapsed() + \
               (Settings.PROJECTILE_ACCELERATION * (self._timer.get_time_elapsed() ** 2) / 2)
        return self.rect.y

    def get_style(self):
        """
        Returns the style of this Projectile.
        """
        return self._style

    def draw(self, screen):
        """
        Draws the Player avatar on the screen.
        """
        screen.blit(self.images[self._style], (self.get_x(self.side), self.get_y()))

    def launch(self):
        """
        Begins the launching sequence.
        """
        if not self.launched:
            self.launched = True
            self._timer.start()
