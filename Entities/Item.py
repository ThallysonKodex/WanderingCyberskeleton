import pygame
from Map.map import tile_size

class Item(pygame.sprite.Sprite):
    def __init__(self, pos, img):
        super().__init__()

        self.img = img
        self.drop = 1
        self.pos = pos
        self.image = pygame.transform.scale(pygame.image.load(self.img).convert_alpha(), (tile_size * self.drop, tile_size * self.drop))
        self.rect = self.image.get_rect(center = pos)
        self.on_player = False

    def draw(self, screen):
        pass

    def update(self):
        if self.on_player == True:
            self.drop = 1.2
        elif self.on_player == False:
            self.drop = 1
        self.image = pygame.transform.scale(pygame.image.load(self.img).convert_alpha(), (tile_size * self.drop, tile_size * self.drop))


