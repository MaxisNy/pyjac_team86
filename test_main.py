from ProjectileContainer import ProjectileContainer
import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720

# TODO: define a more precise variable
SEA_LEVEL = 601

surface = pygame.display.set_mode((WIDTH, HEIGHT))

game_running = True
FPS = 60

pc = ProjectileContainer()
pc.generate(30)

clock = pygame.time.Clock()

while game_running:
    clock.tick(FPS)

    surface.fill((0, 0, 0))

    if pc.get_size():
        pc.launch()

    for projectile in pc.get_launched():
        projectile.draw(surface)

    pygame.display.update()

    # print(projectile.get_x(0), projectile.get_y())
    # print(projectile.launched)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            # quit()

    # collision check
    for projectile in pc.get_launched():
        if projectile.get_y() >= SEA_LEVEL:
            pc.remove(projectile)
