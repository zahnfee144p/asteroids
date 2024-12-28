from circleshape import CircleShape
import pygame as pg

from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(screen, "white", (self.position), self.radius, width=LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
