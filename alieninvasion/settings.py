class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        self.debug = False

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 0.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)
        # Number of simultaneous bullets (<= 0 means unlimited)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.alien_speed_upgrade=0.1
        self.alien_points = 50

        self.ship_limit=3
