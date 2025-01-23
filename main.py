import pygame
from constants import *
from player import *
from asteroidfield import *

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create the screen and the clock object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    game_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True: 
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  

        # Update the screen
        screen.fill((0, 0, 0))
 # Update all objects in the updatable group
        for obj in updatable:
            obj.update(dt)

# Draw all objects in the drawable group
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

      

        # Limit FPS and update delta time
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()