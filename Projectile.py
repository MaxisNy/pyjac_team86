from Timer import Timer
import pygame
import random
import math


class Projectile:

    INITIAL_COORDINATES = (780, 600)
    ACCELERATION = 50

    WIDTH = 20
    HEIGHT = 20

    ANGLE = 60

    def __init__(self, side):
        self.x_0 = self.get_init_coords(side)
        self.y_0 = 600
        # TODO: adjust the range of velocities
        self.velocity = random.randint(150, 200)
        self._timer = Timer()
        self.launched = False
        self.side = side

    def get_init_coords(self, side):
        if side:
            return 1200
        return 80

    def get_x(self, side):
        return self.x_0 + ((-1)**side) * self.velocity * \
               math.cos(self.ANGLE * math.pi / 180) * \
               self._timer.get_time_elapsed()

    def get_y(self):
        return self.y_0 - \
               self.velocity * math.sin(self.ANGLE * math.pi / 180) * \
               self._timer.get_time_elapsed() + \
               (self.ACCELERATION * (self._timer.get_time_elapsed() ** 2) / 2)

    def draw(self, screen):
        """
        Draws the Player avatar on the screen.
        """
        # TODO: implement image drawing
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(
            self.get_x(self.side), self.get_y(), self.WIDTH, self.HEIGHT))

    def launch(self):
        if not self.launched:
            self.launched = True
            self._timer.start()
