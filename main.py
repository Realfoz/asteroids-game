import pygame
from constants import *
from player import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() 
    player_1 = player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    rocket = player_1.triangle()

    while True: # main game loop
        screen.fill((0,0,0)) # sets background to black
        player_1.draw(screen)
        player_1.update(dt)
        pygame.display.flip() # updates screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # lets the program quit from the windows bar
                return
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
