import pygame
from Map.Tile import Tile
from Map.map import tile_size

class Level():
    def __init__(self, map):
        self.map = map

    def draw_map(self, offset):
        self.group = pygame.sprite.Group()
        for row_index, row in enumerate(self.map):
            for column_index, column in enumerate(row):
                if column == "X":
                    x = column_index * tile_size - offset.x
                    y = row_index * tile_size - offset.y
                    tile = Tile((x, y), tile_size, self.group)
                    self.group.add(tile)
        return self.group

