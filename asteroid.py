from circleshape import CircleShape
import pygame
from constants import * 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, ASTEROID_COLOR, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position
        super().update(dt)