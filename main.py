import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init() # Initialize Pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create a window
    clock = pygame.time.Clock() # Create a clock object
    dt = 0 # Delta time (time since last frame)
    updatable = pygame.sprite.Group() # Create a group for objects that need to be updated
    drawable = pygame.sprite.Group() # Create a group for objects that need to be drawn
    asteroids = pygame.sprite.Group() # Create a group for asteroids
    shots = pygame.sprite.Group() # Create a group for shots
    Asteroid.containers = (updatable, drawable, asteroids) # Set the containers for the asteroid object
    Player.containers = (updatable, drawable) # Set the containers for the player object
    AsteroidField.containers = (updatable) # Set the containers for the asteroid field object
    Shot.containers = (updatable, drawable, shots) # Set the containers for the shot object
    asteroid_field = AsteroidField() # Create an asteroid
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Create a player object
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #player.update(dt)
        updatable.update(dt) # Update all objects in the updateable group
        screen.fill("black")  # Clear the screen
        #player.draw(screen)
        for obj in drawable:
            obj.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip() # Update the display

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()