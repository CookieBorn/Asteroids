
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from player import *
pygame.init()
from constants import *
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
Clock=pygame.time.Clock()
player=Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    dt=1
    while 0<1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        dt = Clock.tick(60) / 1000




if __name__ == "__main__":
        main()
