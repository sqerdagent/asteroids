#Stores python scripts for the Player Ojbect
import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, int_x, int_y):
        #Kicking values to circleshape.py
        super().__init__(int_x, int_y, PLAYER_RADIUS)
        self.rotation = 0
    
    def draw(self, screen):
        #https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon
        #polygon(surface, color, points, width=0) -> Rect
        pygame.draw.polygon(screen, (255,255,255), (self.triangle()), 2)

    def update(self, dt):
        #Keyboard Inputs
        #https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_d]:
            self.rotate(dt, keys)
        
        if keys[pygame.K_w] or keys[pygame.K_s]:
            self.move(dt, keys)


    def rotate(self, dt, keys):
        #I do not like the concept of negative dt
        clockwise_or_counterclockwise = 0
        if keys[pygame.K_a]:
            clockwise_or_counterclockwise +=1
        if keys[pygame.K_d]:
            clockwise_or_counterclockwise -=1

        #I could make it fancier by taking the true/fasle values, but GOOD ENOUGH
        self.rotation += (PLAYER_TURN_SPEED * dt) * clockwise_or_counterclockwise

        #Keep it within one circle
        self.rotation %= 360
    
    def move(self, dt, keys):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        forward_or_backward = 0
        if keys[pygame.K_w]:
            forward_or_backward +=1
        if keys[pygame.K_s]:
            forward_or_backward -=1
        self.position += forward * PLAYER_SPEED * dt * forward_or_backward

    #in the player class        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]