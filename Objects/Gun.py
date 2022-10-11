import pygame, math
from Entities.Item import Item
from Map.map import tile_size
from Entities.Bullet import Bullet


class Gun(Item):

    def __init__(self, pos, img):
        super().__init__(pos, img)

        self.framage()

        self.frame = 0

        self.img = img
        self.drop = 1
        self.pos = pos
        self.image = pygame.transform.scale(self.frames[self.frame], (tile_size * self.drop, tile_size * self.drop))
        self.rect = self.image.get_rect(center = self.pos)
        self.gui_image = pygame.transform.scale(pygame.image.load("graphics/guns/gui.png").convert_alpha(), (tile_size * self.drop, tile_size * self.drop))
        self.on_player = False
        self.correction_angle = 90
        self.bullet_group = pygame.sprite.Group()
        self.rot_image = self.image
        self.rot_image_rect = self.rect
        self.animation_speed = 2500
    def animate(self, dt):
        m = pygame.mouse.get_pressed()
        if m[0]:
            self.frame += 1 * (self.animation_speed / 100) * dt
            if self.frame >= 2:
                self.frame = 0
            self.image = pygame.transform.scale(self.frames[int(self.frame)], (tile_size * self.drop, tile_size * self.drop))
        else:
            self.frame = 0
        self.image = pygame.transform.scale(self.frames[int(self.frame)], (tile_size * self.drop, tile_size * self.drop))
    def framage(self):
        self.frames = [pygame.image.load(f"graphics/guns/{frame}.png").convert_alpha() for frame in range(2)]

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
            self.x, self.y = self.rot_image_rect.x, self.rot_image_rect.y


    def update(self, dt):


        self.animate(dt)
        self.looking()
        self.check_on_player()


