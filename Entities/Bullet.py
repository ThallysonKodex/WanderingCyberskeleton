import pygame, math


class Bullet:
    def __init__(self, pos):

        self.timer = 0
        self.pos = pos
        self.x, self.y = self.pos.x, self.pos.y
        self.pmx, self.pmy = self.x, self.y
        self.dx, self.dy = 0, 0
        self.distance = 0

    def update(self, screen, dt):
        self.countdown = 1
        self.timer += self.countdown
        if self.timer >= 60:
            self.countdown = 0
            self.timer = 60
        if self.timer == 0:
            self.countdown = 1

        m = pygame.mouse.get_pressed()
        if m[0] and self.distance == 0 and self.timer == 60:
            self.timer = 0
            mx, my = pygame.mouse.get_pos()

            radians = math.atan2(my - self.pmy, mx - self.pmx)
            distance = math.hypot(mx - self.pmx, my - self.pmy)
            distance = int(distance)

            self.dx = math.cos(radians)
            self.dy = math.sin(radians)

            pmx, pmy = mx, my

        self.x += self.dx * 1000 * dt
        self.y += self.dy * 1000 * dt

        pygame.draw.circle(screen, 'white', (int(self.x), int(self.y)), 5, 0)
        if self.distance:
            pygame.draw.circle(screen, 'red', (self.pmx, self.pmy), 5, 0)






