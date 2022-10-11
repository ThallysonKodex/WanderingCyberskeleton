import pygame
from Map.map import tile_size

class Item(pygame.sprite.Sprite):
    def __init__(self, pos, img):
        super().__init__()



        self.anim_y = 0
        self.img = img
        self.drop = 1
        self.pos = pos
        self.angle = 1
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(self.img).convert_alpha(), (tile_size * self.drop, tile_size * self.drop)), self.angle)
        self.rect = self.image.get_rect(center = pos)
        self.on_player = False

        self.position = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2((0, 0))


    def movement(self, dt):
        self.position += self.direction * 50 * dt
        self.rect.center = self.position

    def animation(self):


        surface = pygame.Surface((self.rect.width, 10))
        # bottom
        rect = surface.get_rect(x=self.rect.x, y=self.rect.y + self.rect.height + 20)

        # top
        rect2 = surface.get_rect(x=self.rect.x, y=self.rect.y - 20)
        if self.on_player == False:
            if self.rect.colliderect(rect):
                self.direction.y = -1
            if self.rect.colliderect(rect2):
                self.direction.y = 1





    def draw(self, screen):
        pass

    def check_on_player(self):
        if self.on_player == True:
            self.drop = 1.2
        elif self.on_player == False:
            self.drop = 1
        self.image = pygame.transform.scale(pygame.image.load(self.img).convert_alpha(), (tile_size * self.drop, tile_size * self.drop))
    def update(self):


        self.check_on_player()



