import pygame as pg
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroids = pg.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.fill("black")
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        pg.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
