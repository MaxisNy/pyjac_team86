from Timer import Timer
from Projectile import Projectile
from typing import List
import random


class ProjectileContainer:

    projectiles: List[Projectile]

    def __init__(self):
        self.projectiles = []
        self.cooldown = 2.00
        self.timer = Timer()

    def get_size(self):
        return len(self.projectiles)

    def generate(self, size: int):
        for i in range(size):
            projectile = Projectile(random.randint(0, 1))
            self.projectiles.append(projectile)

    def launch(self):
        print(self.cooldown - self.timer.get_time_elapsed())
        if self.timer.is_set:
            if self.timer.get_time_elapsed() >= self.cooldown:
                # shoot
                print("bam")
                for projectile in self.projectiles:
                    if not projectile.launched:
                        projectile.launch()
                # decrease cooldown to make the game more challenging
                self.cooldown -= 0.5
        else:
            self.timer.start()

    def remove(self, projectile: Projectile):
        self.projectiles.remove(projectile)

