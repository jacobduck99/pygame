import pygame
from constants import *
from player import *
from asteroidfield import *
import sys
from shot import *

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots_group)

    pygame.init()

    # Create the screen and the clock object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    game_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots_group)
    asteroid_field = AsteroidField()

    while True: 
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  

        # Update all objects in the updatable group
        for obj in updatable:
            obj.update(dt)

        # Collision check between bullets and asteroids
        collisions = pygame.sprite.groupcollide(
            asteroids, shots_group, True, True, pygame.sprite.collide_circle
        )
        if collisions:
            print(f"Collisions detected: {len(collisions)}")

        # Player collision check
        for asteroid in asteroids: 
            if game_player.collisions(asteroid):
                print("Game over!")
                sys.exit()

        # Draw all objects in the drawable group
        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # Limit FPS and update delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
