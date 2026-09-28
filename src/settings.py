class Settings:
    # Class to store all settings for Alien Invasion

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 0, 230)

        # Ship settings
        self.ship_speed = 5.0
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 8.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 0.01
        self.fleet_drop_speed = 5
        # fleet_direction of 1 = right, -1 = left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Settings that change throughout the game
        self.ship_speed = 5.0
        self.bullet_speed = 8.0
        self.alien_speed = 1.5
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
