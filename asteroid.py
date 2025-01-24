from circleshape import CircleShape
import pygame
from constants import * 
import random 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, ASTEROID_COLOR, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position
        super().update(dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
    
        random_angle = random.uniform(20, 50)
        vector = self.velocity.rotate(random_angle)
        vector1 = self.velocity.rotate(-random_angle)
    
        new_radius = self.radius - ASTEROID_MIN_RADIUS
    
    # First asteroid
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = vector * 1.2
    
    # Second asteroid
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = vector1 * 1.2
    
    # Add BOTH asteroids to groups
        for group in self.groups():
            group.add(new_asteroid1)
            group.add(new_asteroid2)


