from ProjectileContainer import ProjectileContainer
import pygame

pygame.init()

WIDTH = 1600
HEIGHT = 900

# TODO: define a more precise variable
SEA_LEVEL = 700

surface = pygame.display.set_mode((WIDTH, HEIGHT))

game_running = True
FPS = 60

pc = ProjectileContainer()
pc.generate(3)

for i in range(len(pc.projectiles)):
    print(f"#{i}, launched: {pc.projectiles[i].launched}")

clock = pygame.time.Clock()


while game_running:
    clock.tick(FPS)

    surface.fill((0, 0, 0))

    # projectiles.launch()

    pc.launch()

    for projectile in pc.projectiles:

        # print(projectile.get_y())

        if projectile.get_y() < SEA_LEVEL:
            projectile.draw(surface)
        else:
            pc.remove(projectile)

    pygame.display.update()

    # print(projectile.get_x(0), projectile.get_y())
    # print(projectile.launched)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            # quit()
