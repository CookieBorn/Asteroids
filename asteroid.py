from circleshape import *
import pygame
import random

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
       super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self, dt):
        self.position+=(self.velocity * dt)
    def Split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        else:
            x=random.uniform(20,50)
            z1=self.velocity.rotate(x)
            z2=self.velocity.rotate(-x)
            r2=self.radius-ASTEROID_MIN_RADIUS
            ast1=Asteroid(self.position.x,self.position.y,r2)
            ast1.velocity=z1*1.2
            ast2=Asteroid(self.position.x,self.position.y,r2)
            ast2.velocity=z2*1.2
