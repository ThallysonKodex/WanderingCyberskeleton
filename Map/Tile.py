import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)

        self.image = pygame.transform.scale(pygame.image.load("graphics/Tiles/BlueTile.png").convert(), (size, size))
        self.rect = self.image.get_rect(center = pos)