import pygame
from Timer import Timer


class Player:
    """
    The Player character class.
    """
    BLOCK_DOWN_SPEED = 4  # Player's regular horizontal movement speed
    BLOCK_UP_SPEED = 1  # Player's movement speed with defense enables

    # TODO: replace WIDTH and HEIGHT with the Player image
    WIDTH = 50
    HEIGHT = 70

    # TODO: move acceleration to the main
    ACCELERATION = 600

    INITIAL_COORDINATES = (300, 450)   # Player's coordinates as the game starts

    x_pos: int  # Player's x coordinate
    y_pos: int  # Player's y coordinate
    block: bool  # True if the shield is up, False otherwise
    jumping: bool  # True if the Player is currently in the air, False otherwise
    speed_hor: int  # Player's horizontal movement speed
    speed_ver: int  # Player's vertical movement speed

    def __init__(self) -> None:
        """
        The Player constructor.
        """
        self.x_pos = self.INITIAL_COORDINATES[0]
        self.y_pos = self.INITIAL_COORDINATES[1]
        self.block = False
        self.jumping = False
        self.speed_hor = self.get_speed()
        self.speed_ver = 450
        self.timer = Timer()

    def get_x(self):
        """
        Returns Player's x coordinate.
        """
        return self.x_pos

    def get_y(self):
        """
        Returns Player's y coordinate.
        """
        if self.jumping:
            self.y_pos = self.INITIAL_COORDINATES[1] - \
                         (self.speed_ver * self.timer.get_time_elapsed()) + \
                         (self.ACCELERATION *
                          (self.timer.get_time_elapsed()**2) / 2)

            # end the jump
            if self.y_pos > self.INITIAL_COORDINATES[1]:
                self.y_pos = self.INITIAL_COORDINATES[1]
                self.jumping = False

        return self.y_pos

    def get_speed(self):
        """
        Returns Player's horizontal movement speed.
        """
        if self.block:
            return self.BLOCK_UP_SPEED
        return self.BLOCK_DOWN_SPEED

    def draw(self, screen):
        """
        Draws the Player avatar on the screen.
        """
        # TODO: implement image drawing
        if self.block:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(
                self.get_x(), self.get_y(), self.WIDTH, self.HEIGHT))
        else:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(
                self.get_x(), self.get_y(), self.WIDTH, self.HEIGHT))

    def move_right(self):
        """
        Moves Player horizontally to the right.
        """
        self.x_pos += self.get_speed()

    def move_left(self):
        """
        Moves Player horizontally to the left.
        """
        self.x_pos -= self.get_speed()

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.timer.start()

    def block_up(self):
        """
        Enables defense. Only possible when the Player is on the ground.
        """
        if not self.jumping:
            self.block = True

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

        print(p.get_x(), p.get_y())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                # quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and p.get_x() > 0:
            p.move_left()
        if keys[pygame.K_d] and p.get_x() + p.WIDTH < WIDTH:
            p.move_right()

        if keys[pygame.K_SPACE]:
            p.jump()

        if keys[pygame.K_LSHIFT]:
            p.block_up()
        else:
            p.block_down()
