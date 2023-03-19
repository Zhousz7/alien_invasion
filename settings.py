class Settings:
    """"store the classes in settings of the game"""

    def __init__(self):
        """initialize the settings in the game"""
        # screen settings
        self.screen_width = 1200
        self.screen_height =800
        self.bg_color = (230,230,230)

        # ship settings
        self.ship_speed = 1.5