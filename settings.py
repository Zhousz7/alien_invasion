class Settings:
    """"store the classes in settings of the game"""

    def __init__(self):
        """initialize the static settings in the game"""
        # screen settings
        self.screen_width = 1200
        self.screen_height =800
        self.bg_color = (230,230,230)

        # ship settings
        self.ship_speed = 1.5

        # bullet settings
        self.bullet_speed = 1.5
        self.ships_limit = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction indicates move towards right when 1,towards left when -1
        self.fleet_direction = 1

        # fasten the game pace
        self.speedup_scale = 1.1

        # increase alien scores
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize the varible settings"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction indicates right when 1, left when -1
        self.fleet_direction = 1

        # record scores
        self.alien_points = 50

    def increase_speed(self):
        """fasten speed settings and alien scores"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.aliens_points = int(self.alien_points * self.score_scale)