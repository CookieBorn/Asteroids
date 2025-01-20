# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
pygame.init
import constants
screen=pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
x=0

def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    while x<1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    screen.fill("black")
    pygame.display.flip()

if __name__ == "__main__":
        main()
