from circleshape import *
from constants import *
from shot import *


class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 180
        self.angle = 180
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, (255, 255, 255), points, 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.angle += PLAYER_TURN_SPEED * dt
        # keeping angle within 0 to 360
        self.angle %= 360

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # print("a pressed ", dt)
            self.rotate(-dt)

        if keys[pygame.K_d]:
            # print("d pressed ", dt)
            self.rotate(dt)

        if keys[pygame.K_w]:
            # print("d pressed ", dt)
            self.move(dt)

        if keys[pygame.K_s]:
            # print("d pressed ", dt)
            self.move(-dt)

        # shot cooldown timer
        if self.timer < 0:
            self.timer = 0

        if self.timer > 0:
            self.timer -= dt

        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
            print("timer, dt ", self.timer, dt)
            self.timer = PLAYER_SHOOT_COOLDOWN

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        # self.angle gets set separately but can probably be removed bc it copies self.rotation
        direction_vector = pygame.Vector2(0, 1).rotate(self.angle)
        direction_vector *= PLAYER_SHOOT_SPEED
        shot.velocity = direction_vector
