
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from player import Player
pygame.init
import constants
screen=pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
x=0
Clock=pygame.time.Clock()
dt=0
me=Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,20)


def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    while x<1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    screen.fill("black")
    Player.draw(me,screen)
    pygame.display.flip()
    dt = Clock.tick(60) / 1000



if __name__ == "__main__":
        main()
