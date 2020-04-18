class Settings():
    """A class to store all settings for Alien invasion"""

    def __init__(self):
        """Initialize the game's static settings"""
        #Screen settings:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #ship setting

        self.ship_limit = 3
        #alien setting

        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right; -1 represent left.
        self.fleet_direction = 1

        #bullet settings

        self.bullet_width = 3
        self.bullet_heigh = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #how quick the game speeds up
        self.speedup_scale = 1.1
        #How quick the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """"initialize settings that change throught the time"""

        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 3
        #fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50


    def increase_speed(self):
        """increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

