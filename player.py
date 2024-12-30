#Stores python scripts for the Player Ojbect
import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, int_x, int_y):
        #Kicking values to circleshape.py
        super().__init__(int_x, int_y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
    
    def draw(self, screen):
        #https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon
        #polygon(surface, color, points, width=0) -> Rect
        pygame.draw.polygon(screen, (255,255,255), (self.triangle()), 2)

    def update(self, dt):
        self.shoot_cooldown -= dt

        #lets players "charge" a few shots by not firing
        if self.shoot_cooldown < -.5:
           self.shoot_cooldown = -.5

        #Keyboard Inputs
        #https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_d]:
            self.rotate(dt, keys)
        
        if keys[pygame.K_w] or keys[pygame.K_s]:
            self.move(dt, keys)

        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown < 0:
                self.shoot()
                self.shoot_cooldown += PLAYER_SHOOT_COOLDOWN
                




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


    def shoot(self):
        print("Attempting to create shot")
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
    


    #in the player class        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]