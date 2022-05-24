import sys
from random import choice

import pygame

from exercise_15_3.random_walk import RandomWalk


class RwGame:

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.walk = RandomWalkGame(self)

    def start(self):
        while True:
            self._check_events()
            self.walk.step()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Redraw the screen during each pass through the loop."""
        # Make the most recently drawn screen visible.
        self.screen.fill((230, 230, 230))
        self.walk.blitme()
        pygame.display.flip()


class RandomWalkGame:

    def __init__(self, the_game, distance_x=None, distance_y=None):
        if distance_x is None:
            distance_x = [0, 1, 2, 3, 4]
        if distance_y is None:
            distance_y = [0, 1, 2, 3, 4]

        self.distance_x = distance_x
        self.distance_y = distance_y

        self.game = the_game
        self.screen = self.game.screen
        self.screen_rect = self.game.screen.get_rect()

        self.image = pygame.image.load('../alieninvasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def step(self):
        x_direction = choice([1, -1])

        x_distance = choice(self.distance_x)
        x_step = x_direction * x_distance
        y_direction = choice([1, -1])
        y_distance = choice(self.distance_y)
        y_step = y_direction * y_distance
        # Reject moves that go nowhere.

        if x_step == 0 and y_step == 0:
            # If no movement, take another step
            self.step()
            return

        new_x = self.rect.x + x_step
        new_y = self.rect.y + y_step
        # Validate new values

        if new_x <= 0:
            self.step()
            return
        elif new_x >= self.screen_rect.right:
            self.step()
            return
        else:
            self.rect.x = new_x

        if new_y <= 0:
            self.step()
            return
        elif new_y >= self.screen_rect.bottom:
            self.step()
            return
        else:
            self.rect.y = new_y


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = RwGame()
    game.start()
