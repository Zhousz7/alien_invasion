import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """"the class which control gaming resources and actions"""
    def __init__(self):
        """initialize the game and create gaming resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)


    def run_game(self):
        """start the main circulation"""
        while True:
            # monitor the keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # fill the screen after every circulation
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # make the lately screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # create the game example and run the game
    ai = AlienInvasion()
    ai.run_game()
