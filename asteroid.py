import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white",(self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
      self.position.x += self.velocity.x * dt
      self.position.y += self.velocity.y * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            vector_1 = pygame.math.Vector2.rotate(self.velocity, angle)
            vector_2 = pygame.math.Vector2.rotate(self.velocity, (angle * -1))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = vector_1 * 1.2
            asteroid_2.velocity = vector_2 * 1.2