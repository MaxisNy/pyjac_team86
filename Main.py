from typing import List
import pygame
import Settings
from Timer import Timer
from Ship import Ship, EnemyShip, PlayerShip
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

    def _initialize_actors(self) -> None:
        """
        Initializes all the game actors
        """
        self.player = Player()

        ships = Ship.initialize_game_ships()
        self.main_ship = ships[1]
        self.actors.add(ships[0], ships[1], ships[2])

        self.projectile_container = ProjectileContainer()
        self.projectile_container.generate(Settings.NUM_OF_PROJECTILES)

    def draw(self) -> None:
        """
        Draw all the game elements.
        """
        self.draw_background()
        self.actors.draw(self.screen)
        self.player.draw(self.screen)
        self.draw_projectiles()
        self.draw_health_bar()
        self.draw_elapsed_time()
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
            (self.main_ship.rect.x, self.main_ship.rect.y -
             self.main_ship.rect.size[1] / 5))

    def draw_health_bar(self) -> None:
        """
        Draws the health bar of the ship.
        """
        heart = load_image(Settings.HEART_IMG, self.SCREEN_WIDTH // 30, self.SCREEN_WIDTH // 30)
        for i in range(0, self.main_ship.get_ship_health()):
            self.screen.blit(heart, (10 + 55*i, 10))

    def draw_elapsed_time(self) -> None:
        """
        Draws the elapsed time since the game started.
        """
        current_time = self.game_timer.get_time_elapsed()
        if current_time > self.best_time:
            self.best_time = current_time
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(("Time: {0:.1f}".format(
            current_time)), True, Settings.BLACK)
        font2 = pygame.font.Font('freesansbold.ttf', 32)
        text2 = font.render("Best time {0:.1f}".format(self.best_time), True,
                            Settings.LIGHT_GRAY)
        text_rect = text.get_rect()
        text_rect.x = self.SCREEN_WIDTH - text_rect.size[0]
        text_rect.y = 0
        text_rect2 = text2.get_rect()
        text_rect2.x = self.SCREEN_WIDTH - text_rect2.size[0]
        text_rect2.y = 10 + text_rect.size[1]
        self.screen.blit(text, text_rect)
        self.screen.blit(text2, text_rect2)

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

    def draw_projectiles(self):
        """
        Responsible for drawing projectiles.
        """
        for projectile in self.projectile_container.get_launched():
            projectile.draw(self.screen)

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
                    self.intro_running = False
            self.screen.blit(self.background, (0, 0))
            self.draw_intro_text()
            pygame.display.update()

    def run_game(self):
        """
        Responsible for running the main loop of the game.
        """
        self.game_timer.start()
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
            if keys[pygame.K_a] and self.player.get_x() > 0:
                self.player.move_left()
            if keys[pygame.K_d] and self.player.get_x() < Settings.SCREEN_WIDTH:
                self.player.move_right()
            if keys[pygame.K_SPACE]:
                self.player.jump()
            if keys[pygame.K_LSHIFT]:
                self.player.block_up()
            else:
                self.player.block_down()

            # collision check
            for projectile in self.projectile_container.get_launched():
                if projectile.get_y() >= Settings.SEA_LEVEL:
                    self.projectile_container.remove(projectile)

    def run(self):
        """
        Responsible for the entire game loop.
        """
        while self.running:
            self.run_intro()
            self.run_game()


if __name__ == '__main__':
    screen = Screen()
    screen.run()
