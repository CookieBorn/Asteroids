# import pygame module

import pygame


class Label():
    def __init__(self, txt, screen, fg="White", font_name="freesansbold.ttf", font_size=20):
        self.fg = fg
        self.screen=screen


        self.font = pygame.font.Font(font_name, font_size)
        self.txt = txt

    def render(self):
        return self.font.render(self.txt, True, self.fg)

    def draw(self, screen):
        screen.blit(self.render(), (10,10))


    def update(self, dt):
        self.font.render(self.txt, True, self.fg)
