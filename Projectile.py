import pygame
import math

class Projectile:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel, angle):
        self.x += vel * math.cos(angle)
        self.y = self.y + vel * math.sin(angle) - (9.81 / 2)