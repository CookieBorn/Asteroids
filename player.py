from circleshape import CircleShape
from constants import *
import pygame
from main import *
pygame.init()
class Player(CircleShape):
    def __init__(self,x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation=0
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED*dt
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
               Player.rotate(self,dt)
        if keys[pygame.K_RIGHT]:
               Player.rotate(self,-dt)
        if keys[pygame.K_UP]:
               Player.move(self,dt)
        if keys[pygame.K_DOWN]:
               Player.move(self,-dt)
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
