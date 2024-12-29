# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import time   #old Method of limiting cpu
from constants import *
# from circleshape import CircleShape

#https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
class CircleShape(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       # self.image = pygame.Surface([width, height])
       # self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       # self.rect = self.image.get_rect()

    
def main():
    #Initializing pygame module see: https://www.pygame.org/docs/ref/pygame.html
    pygame.init()
    print(f"Running Pygame version: {pygame.__version__}")

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    #https://www.pygame.org/docs/ref/time.html#pygame.time.Clock
    delta_time_clock = pygame.time.Clock()
    dt = 0
    print(f"Inititializing Delta Time Object {delta_time_clock} at dt:{dt}")
    

    #creating GUI Window https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Helper variables begin:
    fps_time_to_stdout_timer = 0 #Accumulates delta time



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


        











        #update the clock https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
        dt = delta_time_clock.tick(60)/1000
        # time.sleep(1) old method of limiting cpu usage

        #Simple output to stdout to show game is running.
        fps_time_to_stdout_timer += dt
        if fps_time_to_stdout_timer >=5:
            print(f"delta_time_clock is: {delta_time_clock} dt is: {dt}")
            fps_time_to_stdout_timer = 0
        
        
        



if __name__ == "__main__":
    main()

