import pygame, sys, random
from Entities.Player import Player
from Entities.Particles import Particles
from Map.Level import Level
from Map.map import level_1
from Map.map import tile_size
from Map.map import WINDOW_WIDTH, WINDOW_HEIGHT
from Entities.Gun import Gun

class AllAssets(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()

        self.level = Level(level_1)

        self.undX, self.undY = 32, 27
        self.cx, self.cy = 110, 110

    def drawing(self, screen):

        self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2


        self.level.draw_map(self.offset).draw(screen)
        player.particling(screen)



        screen.blit(pygame.transform.scale(pygame.image.load("graphics/Underlay.png").convert_alpha(), (self.cx, self.cy)), [WINDOW_WIDTH / 2 - self.undX, WINDOW_HEIGHT / 2 - self.undY])





        for sprite in sorted(self.sprites(), key= lambda a: a.rect.centery):
            offset = sprite.rect.center - self.offset
            screen.blit(sprite.image, offset)
            for item in player.itemification:
                offset1 = item.rect
                screen.blit(item.image, offset)
            for item in items:
                screen.blit(item.image, item.rect.center - self.offset)
                item.draw(screen)
                item.update()




pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("The sparks")
clock = pygame.time.Clock()


allAssets = AllAssets()
items = []
player = Player((336, 622), tile_size, allAssets)

gun = Gun((336, 500))
items.append(gun)
gun1 = Gun((100, 800))
items.append(gun1)




font = pygame.font.SysFont("Arial", 40)
mag = pygame.transform.scale(pygame.image.load("graphics/Magnifying.png").convert_alpha(), (WINDOW_WIDTH + 300, WINDOW_HEIGHT + 300))


f3 = False

# Test




while True:

    screen.fill('red')

    dt = clock.tick() / 1000


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
    allAssets.update(screen, dt, items)



    screen.blit(mag, mag.get_rect(topleft = (-150, -150)))






    if f3 == True:
        screen.blit(pygame.Surface((100, 50)), (50, 50))
        screen.blit(font.render(f"X {player.rect.centerx}", False, (255, 255, 255)), (50, 50))
        screen.blit(pygame.Surface((100, 50)), (50, 100))
        screen.blit(font.render(f"Y {player.rect.centery}", False, (255, 255, 255)), (50, 100))
        screen.blit(pygame.Surface((100, 50)), (50, 150))
        screen.blit(font.render(f"FPS {round(clock.get_fps())}", False, (255, 255, 255)), (50, 150))

    pygame.display.update()