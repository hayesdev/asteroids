import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    # this needs to be a tuple so remember () with a comma
    AsteroidField.containers = (updatable,)

    # delta time
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # instances
    player = Player(x, y)
    asteroid_field = AsteroidField()

    # initialize game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        # fill() expects a tuple
        screen.fill((0, 0, 0))

        # updates
        for obj in updatable:
            obj.update(dt)

        # collision detection
        for obj in asteroids:
            if obj.collides_with(player):
                print("Game over!")
                pygame.time.wait(500)
                running = False

        # fire shots
        for obj in shots:
            obj.update(dt)

        # shot collision detection
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.kill()
                    shot.kill()

                    # draw sprites
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
