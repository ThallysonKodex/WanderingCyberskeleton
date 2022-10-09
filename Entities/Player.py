import pygame, random
from Map.map import WINDOW_WIDTH, WINDOW_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)

        self.particle_direction = 'down'
        self.size = size
        self.particles = []
        self.path = "graphics/player/"
        self.framage()
        self.frame = 0
        self.image = pygame.transform.scale(self.frames[self.frame], (self.size, self.size))
        self.rect = self.image.get_rect(center = pos)




        self.position = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2((0, 0))
        self.speed = 600




    def movement(self, dt):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.position += self.direction * self.speed * dt
        self.rect.center = self.position

    def framage(self):
        self.frames = [pygame.image.load(f"{self.path}down/{frame}.png").convert_alpha() for frame in range(7)]

    def input(self):
        ks = pygame.key.get_pressed()
        self.direction.y = 0
        self.direction.x = 0

        if ks[pygame.K_w]:
            self.particle_direction = 'up'
            self.frames = [pygame.image.load(f"{self.path}up/{frame}.png").convert_alpha() for frame in range(7)]
            self.direction.y = -1
        elif ks[pygame.K_s]:
            self.particle_direction = 'down'
            self.frames = [pygame.image.load(f"{self.path}down/{frame}.png").convert_alpha() for frame in range(7)]
            self.direction.y = 1
        if ks[pygame.K_a]:
            self.particle_direction = 'right'
            self.frames = [pygame.image.load(f"{self.path}left/{frame}.png").convert_alpha() for frame in range(7)]
            self.direction.x = -1
        elif ks[pygame.K_d]:
            self.particle_direction = 'left'
            self.frames = [pygame.image.load(f"{self.path}right/{frame}.png").convert_alpha() for frame in range(7)]
            self.direction.x = 1

    def animation(self, dt):
        if self.direction.magnitude() != 0:
            self.frame += 5 * (self.speed / 100) * dt
            if self.frame >= 7:
                self.frame = 0
            self.image = pygame.transform.scale(self.frames[int(self.frame)], (self.size, self.size))
        else:
            self.frame = 0
        self.image = pygame.transform.scale(self.frames[int(self.frame)], (self.size, self.size))

    def particling(self, screen):
        if self.direction.magnitude() != 0:
            self.particles.append([[WINDOW_WIDTH / 2 + 25, WINDOW_HEIGHT / 2 + 45],
                                   [random.randint(0, 20) / 10 - 2, random.randint(0, 20) / 10 - 2],
                                    random.randint(4, 6)])

        for particle in self.particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1

            if self.particle_direction == 'down':
                particle[1][1] = -2
                particle[1][0] = random.randint(0, 40) / 10 - 2
            elif self.particle_direction == 'up':
                particle[1][1] = 2
                particle[1][0] = random.randint(0, 40) / 10 - 2
            elif self.particle_direction == 'right':
                particle[1][1] = random.randint(0, 40) / 10 - 2
                particle[1][0] = 2
            elif self.particle_direction == 'left':
                particle[1][1] = random.randint(0, 40) / 10 - 2
                particle[1][0] = -2

            if particle[2] <= 0:
                self.particles.remove(particle)

            pygame.draw.rect(screen, (255, 255, 255), (particle[0][0], particle[0][1], particle[2], particle[2]))



    def update(self, screen, dt):


        self.movement(dt)
        self.input()
        self.animation(dt)

