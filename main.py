import pygame
from constants import * # * imports everything, not best practice but its a small project
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *

updatable = pygame.sprite.Group() # creates groups for things that need to update on screen each loop
drawable = pygame.sprite.Group() # creates a group of things that need to be drawn on screen each loop
asteroids = pygame.sprite.Group()
Player.containers = (updatable, drawable,) # adds the player to relavent groups
Asteroid.containers = (asteroids, updatable, drawable,) # adds asteroids to relavant groups
AsteroidField.containers = (updatable,)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    dt = 0 # delta time, keep the fps and clock speed tied together and is used in many movement calculations

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # sets the parameters and creates the screen object
    clock = pygame.time.Clock() #creates the clock object
    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # creates the player object in the center of the screen
    asteroidfield = AsteroidField() # creates teh asteroid field objects

    while True: # main game loop
        screen.fill((0,0,0)) # sets background to black

        updatable.update(dt) # upddates everything in the updatable group like players, asteroids, etc. each loop

        for asteroid in asteroids:
            if (player_1.collision(asteroid)) == True:
                print ("Game Over!")
                import sys
                sys.exit()

        for entity in drawable: # draws everything in the drawable group to screen each loop
            entity.draw(screen)
        
        pygame.display.flip() # updates screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # lets the program quit from the windows bar
                return
        dt = clock.tick(60) / 1000 # updates dt based on 60 fps
    

if __name__ == "__main__":
    main()
