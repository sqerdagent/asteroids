import pygame
import random
from constants import *
from circleshape import CircleShape


import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        #https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
        #circle(surface, color, center, radius, width=0, 
         # draw_top_right=None, draw_top_left=None, draw_bottom_left=None, draw_bottom_right=None) -> Rect
        pygame.draw.circle(screen, (255,255,255), (self.position), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        #https://docs.python.org/3/library/random.html#random.uniform
        random_angle = random.uniform(20, 50)
        
        #https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.rotate
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2



        


