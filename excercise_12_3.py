import sys
import pygame


class Exercise:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Exercise 12.1")

    def run(self):
        character = Character(self)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        character.right()
                    elif event.key == pygame.K_LEFT:
                        character.left()
                    elif event.key == pygame.K_UP:
                        character.up()
                    elif event.key == pygame.K_DOWN:
                        character.down()

            self.screen.fill((230, 230, 230))

            character.blitme()
            pygame.display.flip()


class Character:

    def __init__(self, exercise):
        self.step_size = 100
        self.screen = exercise.screen
        self.screen_rect = exercise.screen.get_rect()
        self.image = pygame.image.load('alieninvasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.rotation = 0

    def blitme(self):
        """Draw the ship at its current location."""
        nw_screen = pygame.transform.rotate(self.image, self.rotation)
        self.screen.blit(nw_screen, self.rect)

    def right(self):
        if self.rect.right < self.screen_rect.right:
            self.rotation = 270
            self.rect.x = self.rect.x + self.step_size

    def left(self):
        if self.rect.left > self.screen_rect.left:
            self.rotation = 90
            self.rect.x = self.rect.x - self.step_size

    def up(self):
        if self.rect.top > self.screen_rect.top:
            self.rotation = 0
            self.rect.y = self.rect.y - self.step_size

    def down(self):
        if self.rect.bottom < self.screen_rect.bottom:
            self.rotation = 180
            self.rect.y = self.rect.y + self.step_size


if __name__ == '__main__':
    ex = Exercise()
    ex.run()
