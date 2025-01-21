
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroid import *
from asteroidfield import *
from player import *
pygame.init()
from constants import *
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
Clock=pygame.time.Clock()


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    dt=1
    n=0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)

    asteroidfield = AsteroidField()
    player=Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while 0<1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for up in updatable:
            up.update(dt)
        screen.fill("black")
        for ast in asteroids:
            if ast.Colision(player):
               exit("Game Over!")
        for dra in drawable:
            dra.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(60) / 1000




if __name__ == "__main__":
        main()
