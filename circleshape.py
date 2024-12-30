import pygame

# Base class for game objects

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collide_check(self, other_circle_shape):
        #https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.distance_to
        if pygame.math.Vector2.distance_to(self.position, other_circle_shape.position) < self.radius + other_circle_shape.radius:
            #print("Collision Detected")
            return True