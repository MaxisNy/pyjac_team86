import Settings
from Timer import Timer
from load_img import load_image
import pygame
import random
import math


class Projectile(pygame.sprite.Sprite):

    INITIAL_COORDINATES = (780, 600)

    WIDTH = 20
    HEIGHT = 20

    def __init__(self, side):
        super().__init__()
        # TODO: adjust the range of velocities
        self.velocity = random.randint(150, 200)
        self._timer = Timer()
        self.launched = False
        self.side = side
        self.image = load_image(
            Settings.PROJECTILE_IMG, Settings.SCREEN_WIDTH // 50,
            Settings.SCREEN_WIDTH // 50)
        self.rect = self.image.get_rect()
        self.rect.x = self.get_init_coords(side)
        self.rect.y = 600

    def get_init_coords(self, side):
        if side:
            return 1200
        return 80

    def get_x(self, side):
        return self.rect.x + ((-1)**side) * self.velocity * \
               math.cos(Settings.PROJECTILE_ANGLE * math.pi / 180) * \
               self._timer.get_time_elapsed()

    def get_y(self):
        return self.rect.y - \
               self.velocity * math.sin(Settings.PROJECTILE_ANGLE * math.pi / 180) * \
               self._timer.get_time_elapsed() + \
               (Settings.PROJECTILE_ACCELERATION * (self._timer.get_time_elapsed() ** 2) / 2)

    def draw(self, screen):
        """
        Draws the Player avatar on the screen.
        """
        screen.blit(self.image, (self.get_x(self.side), self.get_y()))

    def launch(self):
        if not self.launched:
            self.launched = True
            self._timer.start()
