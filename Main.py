import pygame
import Settings
from Timer import Timer
from Ship import Ship, PlayerShip
from load_img import load_image
from Player import Player
from ProjectileContainer import ProjectileContainer


class Screen:
    """
    The main screen for the game.
    """
    SCREEN_WIDTH: int
    SCREEN_HEIGHT: int
    screen: pygame.surface
    background: pygame.image
    game_running: bool
    intro_running: bool
    running: bool
    actors: pygame.sprite.Group
    main_ship: PlayerShip
    game_timer: Timer
    best_time: float
    player: Player
    projectile_container: ProjectileContainer

    def __init__(self) -> None:
        """
        Initializes the screen
        """
        self.SCREEN_WIDTH = Settings.SCREEN_WIDTH
        self.SCREEN_HEIGHT = Settings.SCREEN_HEIGHT
        self.running = True
        self.intro_running = True
        self.game_running = True
        self.running = True
        pygame.init()
        pygame.display.set_caption("HackathonGame")
        self.screen = \
            pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.actors = pygame.sprite.Group()
        self._initialize_actors()
        self.background = load_image(Settings.BACKGROUND_IMG)
        self.game_timer = Timer()
        self.best_time = 0
        self.win_running = False
        self.lose_running = False

    def _initialize_actors(self) -> None:
        """
        Initializes all the game actors
        """
        self.player = Player()

        ships = Ship.initialize_game_ships()
        self.main_ship = ships[1]
        self.actors.add(ships[0], ships[1], ships[2])

    def draw(self) -> None:
        """
        Draw all the game elements.
        """
        self.draw_background()
        self.player.draw(self.screen)
        self.actors.draw(self.screen)
        self.draw_projectiles()
        self.draw_health_bar()
        self.draw_remaining_projectiles()
        pygame.display.update()

    def draw_background(self) -> None:
        """
        Draws the background of the game.
        """
        # Genuine background
        self.screen.blit(self.background, (0, 0))
        # Background of Main Ship
        self.screen.blit(
            PlayerShip.load_ship_background(),
            (self.main_ship.rect.x + 18, self.main_ship.rect.y -
             self.main_ship.rect.size[1] * 2.35))

    def draw_health_bar(self) -> None:
        """
        Draws the health bar of the ship.
        """
        heart = load_image(Settings.HEART_IMG, self.SCREEN_WIDTH // 30,
                           self.SCREEN_WIDTH // 30)
        for i in range(0, self.main_ship.get_ship_health()):
            self.screen.blit(heart, (10 + 55*i, 10))

    def draw_remaining_projectiles(self) -> None:
        """
        Draws the elapsed time since the game started.
        """
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(
            ("Remaining: " + str(self.projectile_container.get_size()) + " / "
             + str(self.projectile_container.size)), True,
            Settings.BLACK)
        text_rect = text.get_rect()
        text_rect.x = self.SCREEN_WIDTH - text_rect.size[0]
        text_rect.y = 0
        self.screen.blit(text, text_rect)

    def draw_intro_text(self):
        """
        Responsible for drawing the text for the introduction.
        Includes summary of game and instructions
        """
        font = pygame.font.Font('freesansbold.ttf', 25)
        height = self.SCREEN_HEIGHT // 6
        for text in Settings.intro_texts:
            temp_text = font.render(text, True, Settings.DARK_GRAY)
            text_rect1 = temp_text.get_rect()
            text_rect1.center = (self.SCREEN_WIDTH // 2, height)
            height += 3 * text_rect1.size[1]
            self.screen.blit(temp_text, text_rect1)

    def draw_paused_text(self):
        """
        Responsible for drawing the text while game is paused.
        """
        font = pygame.font.Font('freesansbold.ttf', 25)
        text = font.render(Settings.paused_text, True, Settings.DARK_GRAY)
        text_rect = text.get_rect()
        text_rect.center = (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 4)
        self.screen.blit(text, text_rect)

    def draw_win_text(self):
        """
        Responsible for drawing the text when the player wins.
        """
        font = pygame.font.Font('freesansbold.ttf', 25)
        height = self.SCREEN_HEIGHT // 6
        for text in Settings.win_texts:
            temp_text = font.render(text, True, Settings.DARK_GRAY)
            text_rect1 = temp_text.get_rect()
            text_rect1.center = (self.SCREEN_WIDTH // 2, height)
            height += 4 * text_rect1.size[1]
            self.screen.blit(temp_text, text_rect1)

    def draw_lose_text(self):
        """
        Responsible for drawing the text when the player loses.
        """
        font = pygame.font.Font('freesansbold.ttf', 25)
        height = self.SCREEN_HEIGHT // 6
        for text in Settings.lose_texts:
            temp_text = font.render(text, True, Settings.DARK_GRAY)
            text_rect1 = temp_text.get_rect()
            text_rect1.center = (self.SCREEN_WIDTH // 2, height)
            height += 7 * text_rect1.size[1]
            self.screen.blit(temp_text, text_rect1)

    def draw_projectiles(self):
        """
        Responsible for drawing projectiles.
        """
        for projectile in self.projectile_container.get_launched():
            projectile.draw(self.screen)

    def draw_explosion(self, x, y):
        img = load_image(Settings.EXPLOSION_IMG, Settings.SCREEN_WIDTH // 60,
                         (29 / 28) * Settings.SCREEN_WIDTH // 60)
        self.screen.blit(img, (x, y))

    def run_intro(self):
        """
        Responsible for running the game introduction.
        """
        while self.intro_running and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.intro_running = False
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        correct_input = False
                        while not correct_input:
                            if event.key == pygame.K_e:
                                difficulty = "EASY"
                                correct_input = True
                            elif event.key == pygame.K_n:
                                difficulty = "NORMAL"
                                correct_input = True
                            elif event.key == pygame.K_h:
                                difficulty = "HARD"
                                correct_input = True
                    self.projectile_container = ProjectileContainer(difficulty)
                    self.intro_running = False
            self.screen.blit(self.background, (0, 0))
            self.draw_intro_text()
            pygame.display.update()

    def run_game(self):
        """
        Responsible for running the main loop of the game.
        """
        self.projectile_container.generate()
        while self.game_running and self.running:

            if self.projectile_container.get_size():
                self.projectile_container.launch()

            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    self.running = False
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and self.player.get_x() > \
                    self.main_ship.rect.x:
                self.player.move_left()
            if keys[pygame.K_d] and self.player.get_x() < \
                    self.main_ship.rect.x + self.main_ship.rect.width - 50:
                self.player.move_right()
            if keys[pygame.K_LSHIFT]:
                self.player.block_up()
            else:
                self.player.block_down()
                if keys[pygame.K_SPACE]:
                    self.player.jump()

            # collision check
            for projectile in self.projectile_container.get_launched():
                if pygame.sprite.collide_rect(self.player, projectile) and \
                        self.player.block:
                    self.projectile_container.remove(projectile)
                if pygame.sprite.collide_rect(self.main_ship, projectile):
                    self.projectile_container.remove(projectile)
                    self.main_ship.damage()
                    if self.main_ship.ship_health <= 0:
                        self.game_running = False
                if projectile.get_y() >= Settings.SEA_LEVEL:
                    self.projectile_container.remove(projectile)

            if self.projectile_container.get_size() == 0:
                self.game_running = False

    def run_win_screen(self):
        """
        Responsible for running the win screen.
        """
        self.win_running = True
        while self.win_running and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.win_running = False
                    self.running = False
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.win_running = False
                        self.running = False
                        quit()
                    else:
                        self.win_running = False
                        self.game_running = True
                        self.main_ship.ship_health = 5
            self.screen.blit(self.background, (0, 0))
            self.draw_win_text()
            pygame.display.update()

    def run_lose_screen(self):
        """
        Responsible for running the lose screen
        """
        self.lose_running = True
        while self.lose_running and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.lose_running = False
                    self.running = False
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.lose_running = False
                        self.running = False
                        quit()
                    else:
                        self.lose_running = False
                        self.game_running = True
                        self.main_ship.ship_health = 5
            self.screen.blit(self.background, (0, 0))
            self.draw_lose_text()
            pygame.display.update()

    def run(self):
        """
        Responsible for the entire game loop.
        """
        self.run_intro()
        while self.running:
            self.run_game()
            if self.main_ship.get_ship_health() > 0:
                self.run_win_screen()
            else:
                self.run_lose_screen()


if __name__ == '__main__':
    screen = Screen()
    screen.run()
