import sys
import pygame


class Exercise:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Exercise 12.1")

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((0, 0, 230))
            pygame.display.flip()


if __name__ == '__main__':
    ex = Exercise()
    ex.run()
