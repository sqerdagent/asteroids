import pygame
from constants import *
from circleshape import CircleShape

import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        #https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
        #circle(surface, color, center, radius, width=0, 
         # draw_top_right=None, draw_top_left=None, draw_bottom_left=None, draw_bottom_right=None) -> Rect
        pygame.draw.circle(screen, (255,255,255), (self.position), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    



