import pygame, math
from Entities.Item import Item
from Map.map import tile_size


class Gun(Item):
    def __init__(self, pos, img):
        super().__init__(pos, img)


        self.img = img
        self.drop = 1
        self.pos = pos
        self.image = pygame.transform.scale(pygame.image.load(self.img).convert_alpha(), (tile_size * self.drop, tile_size * self.drop))
        self.rect = self.image.get_rect(center = self.pos)
        self.gui_image = pygame.transform.scale(pygame.image.load(self.img).convert_alpha(), (tile_size * self.drop, tile_size * self.drop))

        self.on_player = False
        self.correction_angle = 90

        self.rot_image = self.image
        self.rot_image_rect = self.rect



    def looking(self):
        if self.on_player == True:
            del self.rot_image
            del self.rot_image_rect
            self.rect = self.image.get_rect(center = self.pos)
            mx, my = pygame.mouse.get_pos()
            dx, dy = mx - self.rect.centerx, my - self.rect.centery
            angle = math.degrees(math.atan2(-dy, dx)) - self.correction_angle

            self.rot_image = pygame.transform.rotate(self.image, angle)
            self.rot_image_rect = self.rot_image.get_rect(center=self.rect.center)



    def update(self):


        self.looking()
        self.check_on_player()


