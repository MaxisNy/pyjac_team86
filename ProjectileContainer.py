from Timer import Timer
from Projectile import Projectile
from typing import List
import random


class ProjectileContainer:

    _projectiles: List[Projectile]

    def __init__(self, difficulty: str):
        self.difficulty = difficulty
        self._projectiles = []
        self.cooldown = self.init_cooldown()
        self.size = self.init_size()
        self.timer = Timer()

    def init_cooldown(self):
        if self.difficulty == "EASY":
            return 3.00
        if self.difficulty == "NORMAL":
            return 2.50
        return 1.50

    def init_size(self):
        if self.difficulty == "EASY":
            return 15
        if self.difficulty == "NORMAL":
            return 25
        return 45

    def get_size(self):
        return len(self._projectiles)

    def get_launched(self):
        """
        Returns a list of Projectile objects that have been launched.
        """
        launched_projectiles = []
        for projectile in self._projectiles:
            if projectile.launched:
                launched_projectiles.append(projectile)
        return launched_projectiles

    def generate(self):
        """
        Populates this ProjectileContainer with Projectile objects.
        :param size: number of Projectiles created
        """
        for i in range(self.size):
            projectile = Projectile(random.randint(0, 1))
            self._projectiles.append(projectile)

    def launch(self):
        """
        If the timer has been set (happens after the first main loop iteration),
        loads one of the cannons, waits, and shoots (launches) one of the
        projectiles.
        """
        # print(self.cooldown - self.timer.get_time_elapsed())
        if self.timer.is_set:
            if self.timer.get_time_elapsed() >= self.cooldown:

                # shoot
                for projectile in self._projectiles:
                    if not projectile.launched:
                        projectile.launch()
                        break    # allows shooting one projectile at a time

                # decrease cooldown to make the game more challenging
                self.cooldown -= 0.015

                # reset the timer
                self.timer.start()
        else:
            self.timer.start()

    def remove(self, projectile: Projectile):
        """
        Removes the specified Projectile from this container.
        :param projectile: a Projectile object being removed
        """
        self._projectiles.remove(projectile)
