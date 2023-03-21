class GameStats:
    """track game statistical information"""

    def __init__(self,ai_game):
        """initialize the statistical information"""
        self.settings = ai_game.settings
        self.reset_stats()
        # be active when the game start
        self.game_active = True

    def reset_stats(self):
        """initialize the variable statistical information during running"""
        self.ships_left = self.settings.ships_limit
