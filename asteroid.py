import pygame
from circleshape import CircleShape
from logger import log_event
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (dt * self.velocity)
    
    def get_radius(self):
        return self.radius
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            first_asteroid_mov = self.velocity.rotate(angle)
            second_asteroid_mov = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = first_asteroid_mov * 1.2
            asteroid2.velocity = second_asteroid_mov * 1.2

