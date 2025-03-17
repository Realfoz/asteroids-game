from circleshape import *
from constants import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.shots_group = Shot.containers
        self.rotation = 0
        self.timer = 0
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self,dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
        return self.rotation
    

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        return self.position

    def shoot(self):
        if self.timer > 0:
            return None
        else:
            bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            velocity =  pygame.math.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            bullet.velocity = velocity
            self.timer += PLAYER_SHOT_CD
            


    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        if self.timer != 0:
            self.timer -= dt


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        if Shot.containers:
            for container in Shot.containers:
                container.add(self)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white",(self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
      self.position.x += self.velocity.x * dt
      self.position.y += self.velocity.y * dt
