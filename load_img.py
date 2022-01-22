import Settings
import pygame


def load_image(img_name: str, width: int = Settings.SCREEN_WIDTH,
               height: int = Settings.SCREEN_HEIGHT) -> pygame.image:
    """
    Return a pygame img of the PNG img_name that has been scaled according
    to the given width and size
    """
    img = pygame.image.load(img_name).convert_alpha()
    return pygame.transform.scale(img, (int(width), int(height)))
