from circleshape import CircleShape
import constants
import pygame
class Player(CircleShape):
    def __init__(self,x, y,radius):
        super().__init__(x,y,constants.PLAYER_RADIUS)
        self.rotation=0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * 20 / 1.5
        a = self.position + forward * 20
        b = self.position - forward * 20 - right
        c = self.position - forward * 20 + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
