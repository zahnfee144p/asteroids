import pygame as pg
from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    def triangle(self):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        right = pg.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pg.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pg.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        self.shot_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        self.shot_timer -= dt
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rotate(-dt)
        if keys[pg.K_d]:
            self.rotate(dt)
        if keys[pg.K_w]:
            self.move(dt)
        if keys[pg.K_s]:
            self.move(-dt)
        if keys[pg.K_SPACE]:
            if self.shot_timer > 0:
                pass
            else:
                self.shoot()
