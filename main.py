# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import time   #old Method of limiting cpu
from constants import *
#from circleshape import CircleShape
from player import Player


def main():
    #Initializing pygame module see: https://www.pygame.org/docs/ref/pygame.html
    pygame.init()
    print(f"Running Pygame version: {pygame.__version__}")

    #creating GUI Window https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    print("Starting asteroids!")

    #https://www.pygame.org/docs/ref/time.html#pygame.time.Clock
    delta_time_clock = pygame.time.Clock()
    dt = 0
    print(f"Inititializing Delta Time Object {delta_time_clock} at dt:{dt}")

    #Groups to handle objects
    updatable_objects = pygame.sprite.Group()
    drawable_objects = pygame.sprite.Group()



    #Helper variables begin:
    fps_time_to_stdout_timer = 0 #Accumulates delta time

    #Make Player(s) Updatable and Drawable https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
    Player.containers = (updatable_objects, drawable_objects)
    #Instanciate the player with a default center of screen position
    user_player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    



    while True:
        #get events from the queue https://www.pygame.org/docs/ref/event.html#pygame.event.get
        for event in pygame.event.get():
            #uninitialize all pygame modules https://www.pygame.org/docs/ref/pygame.html#pygame.quit
            if event.type == pygame.QUIT:
                return

        #Fill Screen: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
        screen.fill((0,0,0))
        
        #updates objects in the updateable_objects
        for object in updatable_objects:
            object.update(dt)

        for object in drawable_objects:
            object.draw(screen)
        

        #Refresh Screen: https://www.pygame.org/docs/ref/display.html#pygame.display.flip
        pygame.display.flip()

        #update the clock https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
        dt = delta_time_clock.tick(60)/1000
        # time.sleep(1) old method of limiting cpu usage

        #Simple output to stdout to show game is running.
        fps_time_to_stdout_timer += dt
        if fps_time_to_stdout_timer >=5:
            print(f"delta_time_clock is: {delta_time_clock} dt is: {dt}")
            #print(f"Rotation: {user_player1.rotation}")
            fps_time_to_stdout_timer = 0
        
        
        



if __name__ == "__main__":
    main()

