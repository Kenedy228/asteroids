from circleshape import CircleShape
from constants import *
import random
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        positive_asteroid_velocity = self.velocity.rotate(random_angle)
        negative_asteroid_velocity = self.velocity.rotate(-random_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        first_asteroid.velocity = positive_asteroid_velocity * 1.2
        second_asteroid.velocity = negative_asteroid_velocity * 1.2

