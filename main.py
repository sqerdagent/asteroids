# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import time
from constants import *

def main():
    #Initializing pygame module see: https://www.pygame.org/docs/ref/pygame.html
    pygame.init
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    #creating GUI Window https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        #get events from the queue https://www.pygame.org/docs/ref/event.html#pygame.event.get
        for event in pygame.event.get():
            #uninitialize all pygame modules https://www.pygame.org/docs/ref/pygame.html#pygame.quit
            if event.type == pygame.QUIT:
                return

        #Fill Screen: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
        screen.fill((0,0,0))
        #Refresh Screen: https://www.pygame.org/docs/ref/display.html#pygame.display.flip
        pygame.display.flip()
        time.sleep(1)



if __name__ == "__main__":
    main()

