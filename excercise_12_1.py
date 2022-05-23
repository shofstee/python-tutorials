import sys
import pygame


class Excercise:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Exercise 12.1")

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.event.get()
            self.screen.fill((0, 0, 230))
            pygame.display.flip()


if __name__ == '__main__':
    ex = Excercise()
    ex.run()
