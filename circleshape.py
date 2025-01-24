import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position  # Keep the rect aligned with position

    def draw(self, screen):
        # Sub-classes must override
        pass

    def collisions(self, other_shape):
        distance = self.position.distance_to(other_shape.position)
        combined_radius = self.radius + other_shape.radius
        return distance <= combined_radius
