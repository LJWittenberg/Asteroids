import pygame
from circleshape import CircleShape
from constants import *

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self):
        pygame.draw.cricle(self.position, "white",self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt