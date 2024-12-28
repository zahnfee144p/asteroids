import pygame as pg
import constants

def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pg.init()
    screen = pg.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.fill("black")
        pg.display.flip()


if __name__ == "__main__":
    main()
