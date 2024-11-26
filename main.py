import pygame
# import constants
from constants import *
from player import *


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

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

        # player.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
