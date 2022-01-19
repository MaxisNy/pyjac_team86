import pygame


class Player:
    """
    The Player character class.
    """
    BLOCK_DOWN_SPEED = 3  # Player's regular horizontal movement speed
    BLOCK_UP_SPEED = 1  # Player's movement speed with defense enables
    # TODO: replace WIDTH and HEIGHT with the Player image
    WIDTH = 50
    HEIGHT = 70

    x_pos: int  # Player's x coordinate
    y_pos: int  # Player's y coordinate
    block: bool  # True when the shield is up, False otherwise
    speed: int  # Player's horizontal movement speed

    def __init__(self, x_pos, y_pos) -> None:
        """
        :param x_pos: Player's x coordinate
        :param y_pos: Player's y coordinate
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.block = False
        self.speed = self.get_speed()

    def get_x(self):
        """
        Returns Player's x coordinate.
        """
        return self.x_pos

    def get_y(self):
        """
        Returns Player's y coordinate.
        """
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
                self.x_pos, self.y_pos, self.WIDTH, self.HEIGHT))
        else:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(
                self.x_pos, self.y_pos, self.WIDTH, self.HEIGHT))

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
        # TODO: implement jumping
        pass

    def block_up(self):
        """
        Enables defense.
        """
        self.block = True

    def block_down(self):
        """
        Disables defense.
        """
        self.block = False


if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((700, 700))

    p = Player(300, 120)

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
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    p.move_left()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            p.move_left()
        if keys[pygame.K_d]:
            p.move_right()
        if keys[pygame.K_LSHIFT]:
            p.block_up()
        else:
            p.block_down()
