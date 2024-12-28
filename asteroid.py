from circleshape import CircleShape
import pygame as pg
import random

from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(screen, "white", (self.position), self.radius, width=LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        pos_vel = self.velocity.rotate(angle)
        neg_vel = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first = Asteroid(self.position.x, self.position.y, new_radius)
        first.velocity = pos_vel * 1.2
        second = Asteroid(self.position.x, self.position.y, new_radius)
        second.velocity = neg_vel * 1.2
