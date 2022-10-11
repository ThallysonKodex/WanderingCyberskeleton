import pygame, sys
from Entities.Player import Player
from Map.Level import Level
from Map.map import level_1
from Map.map import tile_size
from Map.map import WINDOW_WIDTH, WINDOW_HEIGHT
from Entities.Item import Item
from Objects.Torch import Torch
from Objects.Gun import Gun
import math



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
            mx, my = pygame.mouse.get_pos()
            offset = sprite.rect.center - self.offset
            screen.blit(sprite.image, offset)




            for item in items:
                item.on_player = False
                screen.blit(item.image, item.rect.center - self.offset)

                item.draw(screen)
                item.update()

            surfend = pygame.transform.scale(pygame.image.load("graphics/gui/0.png").convert_alpha(), (200, 100))

            sruf = pygame.Surface((60, 60))
            sruf_rect = sruf.get_rect(x=425, y=420)
            sruf.fill((255, 0, 0))
            screen.blit(sruf, sruf_rect)


            mousing = pygame.Surface((5, 5))
            mouse_rect = mousing.get_rect(x=mx, y=my)

            if mouse_rect.colliderect(sruf_rect) and len(player.itemification) != 0:
                screen.blit(surfend, (230, 400))

            sruf2 = pygame.draw.rect(screen, (255, 255, 255), (425, 420, 60, 60), 2, 10, 1, 1, 20, 1)
            for item in player.itemification:

                img2 = item.gui_image
                screen.blit(img2, (425, 420))






pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("The sparks")
clock = pygame.time.Clock()

allAssets = AllAssets()
items = []
player = Player((336, 622), tile_size, allAssets)

gun = Gun((336, 500), "graphics/guns/0.png")
items.append(gun)
gun1 = Gun((250, 250), "graphics/guns/0.png")
items.append(gun1)





font = pygame.font.SysFont("Arial", 18)
mag = pygame.transform.scale(pygame.image.load("graphics/Magnifying.png").convert_alpha(), (WINDOW_WIDTH + 300, WINDOW_HEIGHT + 300))


f3 = False

# Test



#   0 - image is looking to the right
#  90 - image is looking up
# 180 - image is looking to the left
# 270 - image is looking down
correction_angle = 90



while True:
    player_pos = screen.get_rect().center




    screen.fill('red')


    dt = clock.tick(144) / 1000


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

    for item in player.itemification:
        if item.on_player == True:
            screen.blit(item.rot_image, item.rot_image_rect.topleft)





    if f3 == True:
        screen.blit(pygame.Surface((100, 150)), (50, 50))
        screen.blit(font.render(f"X {player.rect.centerx}", False, (255, 255, 255)), (50, 50))
        screen.blit(font.render(f"Y {player.rect.centery}", False, (255, 255, 255)), (50, 50 + 18))
        screen.blit(font.render(f"FPS {round(clock.get_fps())}", False, (255, 255, 255)), (50, 50 + 18 * 2))

    pygame.display.update()