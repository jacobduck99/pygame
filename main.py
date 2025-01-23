import pygame
from constants import *
from player import *
from asteroidfield import *
import sys

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    pygame.init()

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
        
 # Update all objects in the updatable group
        for obj in updatable:
            obj.update(dt)

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