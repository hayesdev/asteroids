import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


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

    # containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
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

        # fill() expects a tuple so be sure to use ()
        screen.fill((0, 0, 0))

        # player.update(dt)
        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.collide(player):
                print("Game over!")
                running = False

        # player.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
