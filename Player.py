import pygame
import Settings
from load_img import load_image
from Timer import Timer
from typing import Dict


class Player(pygame.sprite.Sprite):
    """
    The Player character class.
    """

    # TODO: replace WIDTH and HEIGHT with the Player image
    WIDTH = 50
    HEIGHT = 70

    INITIAL_COORDINATES = (300.00, 550.00)   # Player's coordinates as the game starts

    x: int  # Player's x coordinate
    y: int  # Player's y coordinate
    block: bool  # True if the shield is up, False otherwise
    jumping: bool  # True if the Player is currently in the air, False otherwise
    speed_hor: int  # Player's horizontal movement speed
    speed_ver: int  # Player's vertical movement speed

    def __init__(self) -> None:
        """
        The Player constructor.
        """
        super().__init__()
        self.block = False
        self.jumping = False
        self.speed_hor = Settings.PLAYER_BLOCK_DOWN_SPEED
        self.speed_ver = Settings.PLAYER_JUMP_SPEED
        self.timer = Timer()
        self.images = self.generate_player_images()
        self.direction = "LEFT"
        self.rect = self.images["LEFT"].get_rect()
        self.rect.x = self.INITIAL_COORDINATES[0]
        self.rect.y = self.INITIAL_COORDINATES[1]

    @staticmethod
    def generate_player_images() -> Dict:
        return {"LEFT": load_image(Settings.PLAYER_IMG, Settings.SCREEN_WIDTH // 37, (38 / 24) * Settings.SCREEN_WIDTH // 37),
                "RIGHT": pygame.transform.flip(load_image(Settings.PLAYER_IMG, Settings.SCREEN_WIDTH // 37, (38 / 24) * Settings.SCREEN_WIDTH // 37), True, False),
                "LEFT_JUMP": load_image(Settings.PLAYER_JUMP_IMG, Settings.SCREEN_WIDTH // 34, (41 / 35) * Settings.SCREEN_WIDTH // 34),
                "RIGHT_JUMP": pygame.transform.flip(load_image(Settings.PLAYER_JUMP_IMG, Settings.SCREEN_WIDTH // 34, (41 / 35) * Settings.SCREEN_WIDTH // 34), True, False),
                "LEFT_BLOCK": load_image(Settings.PLAYER_BLOCK_IMG, Settings.SCREEN_WIDTH // 27, (31 / 24) * Settings.SCREEN_WIDTH // 27),
                "RIGHT_BLOCK": pygame.transform.flip(load_image(Settings.PLAYER_BLOCK_IMG, Settings.SCREEN_WIDTH // 27, (31 / 24) * Settings.SCREEN_WIDTH // 27), True, False)}

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
            self.rect.y = self.INITIAL_COORDINATES[1] - \
                         (self.speed_ver * self.timer.get_time_elapsed()) + \
                         (Settings.PLAYER_ACCELERATION *
                          (self.timer.get_time_elapsed()**2) / 2)

            # end the jump
            if self.rect.y > self.INITIAL_COORDINATES[1]:
                self.rect.y = self.INITIAL_COORDINATES[1]
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
        if not self.jumping:
            self.jumping = True
            self.timer.start()
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


if __name__ == '__main__':
    pygame.init()

    WIDTH = 1600
    HEIGHT = 900

    surface = pygame.display.set_mode((WIDTH, HEIGHT))

    p = Player()

    game_running = True
    FPS = 60

    clock = pygame.time.Clock()

    while game_running:
        clock.tick(FPS)
        surface.fill((0, 0, 0))
        p.draw(surface)
        pygame.display.update()

        print(p.direction)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                # quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and p.get_x() > 0:
            p.move_left()
        if keys[pygame.K_d] and p.get_x() + p.WIDTH < WIDTH:
            p.move_right()

        if keys[pygame.K_LSHIFT]:
            p.block_up()
        else:
            p.block_down()
            if keys[pygame.K_SPACE]:
                p.jump()
