import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def update(self):
        """Move the alien to the right."""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.alien_speed
        elif not self.moving_right and self.rect.left >= 0:
            self.x -= self.settings.alien_speed

        if self.rect.right == self.screen_rect.right:
            self.moving_right = -1
        elif self.rect.left == 0:
            self.moving_right = 1

        self.rect.x = self.x