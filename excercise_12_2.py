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

            pygame.event.get()
            self.screen.fill((250, 250, 250))
            character = Character(self)
            character.blitme()
            pygame.display.flip()


class Character:

    def __init__(self, exercise):
        self.screen = exercise.screen
        self.screen_rect = exercise.screen.get_rect()
        self.image = pygame.image.load('alieninvasion/images/spaceship.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    ex = Exercise()
    ex.run()
