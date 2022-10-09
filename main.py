import pygame, sys, random
from Entities.Player import Player
from Entities.Particles import Particles
from Map.Level import Level
from Map.map import level_1
from Map.map import tile_size
from Map.map import WINDOW_WIDTH, WINDOW_HEIGHT


class AllAssets(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()

        self.level = Level(level_1)

    def drawing(self, screen):

        self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2


        self.level.draw_map(self.offset).draw(screen)
        player.particling(screen)
        for sprite in sorted(self.sprites(), key= lambda a: a.rect.centery):
            offset = sprite.rect.center - self.offset
            screen.blit(sprite.image, offset)




pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("The sparks")
clock = pygame.time.Clock()

allAssets = AllAssets()

player = Player((336, 622), tile_size, allAssets)

font = pygame.font.SysFont("Arial", 40)

f3 = False

while True:

    screen.fill((50, 50, 50))

    dt = clock.tick(120) / 1000


    for event in pygame.event.get():
        if event.type == 256:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F3 and f3 == False:
                f3 = True
            elif event.key == pygame.K_F3  and f3 == True:
                f3 = False



    allAssets.drawing(screen)
    allAssets.update(screen, dt)




    if f3 == True:
        screen.blit(pygame.Surface((100, 50)), (50, 50))
        screen.blit(font.render(f"X {player.rect.centerx}", False, (255, 255, 255)), (50, 50))
        screen.blit(pygame.Surface((100, 50)), (50, 100))
        screen.blit(font.render(f"Y {player.rect.centery}", False, (255, 255, 255)), (50, 100))

    pygame.display.update()