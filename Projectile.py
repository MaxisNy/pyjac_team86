import Settings
from Timer import Timer
from load_img import load_image
import pygame
import random
import math
import os


class Projectile(pygame.sprite.Sprite):

    INITIAL_COORDINATES = (780, 600)
    ACCELERATION = 50

    WIDTH = 20
    HEIGHT = 20

    ANGLE = 60

    def __init__(self, side):
        super().__init__()
        # TODO: adjust the range of velocities
        self.velocity = random.randint(150, 200)
        self._timer = Timer()
        self.launched = False
        self.side = side
        self.image = load_image(
            Settings.PROJECTILE_IMG, Settings.SCREEN_WIDTH // 35,
            Settings.SCREEN_WIDTH // 35)
        self.rect = self.image.get_rect()
        self.rect.x = self.get_init_coords(side)
        self.rect.y = 600

    def get_init_coords(self, side):
        if side:
            return 1200
        return 80

    def get_x(self, side):
        return self.rect.x + ((-1)**side) * self.velocity * \
               math.cos(self.ANGLE * math.pi / 180) * \
               self._timer.get_time_elapsed()

    def get_y(self):
        return self.rect.y - \
               self.velocity * math.sin(self.ANGLE * math.pi / 180) * \
               self._timer.get_time_elapsed() + \
               (self.ACCELERATION * (self._timer.get_time_elapsed() ** 2) / 2)

    def draw(self, screen):
        """
        Draws the Player avatar on the screen.
        """
        screen.blit(self.image, (self.get_x(self.side), self.get_y()))

    def launch(self):
        if not self.launched:
            self.launched = True
            self._timer.start()
