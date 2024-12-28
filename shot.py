from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame as pg
from constants import LINE_WIDTH


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pg.draw.circle(screen, "white", (self.position), self.radius, width=LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
