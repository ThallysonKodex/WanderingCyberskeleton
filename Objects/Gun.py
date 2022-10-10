import pygame
from Entities.Item import Item
from Map.map import tile_size

class Gun(Item):
    def __init__(self, pos, img):
        super().__init__(pos, img)

        self.img = img
        self.drop = 1
        self.pos = pos
        self.image = pygame.transform.scale(pygame.image.load(self.img).convert_alpha(), (tile_size * self.drop, tile_size * self.drop))
        self.rect = self.image.get_rect(center = pos)
        self.on_player = False




