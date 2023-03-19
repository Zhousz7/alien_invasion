import sys
import pygame


class AlienInvasion:
    """"the class which control gaming resources and actions"""
    def __init__(self):
        """initialize the game and create gaming resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pyagme.display.set_caption("Alien Invasion")

    def run_game(self):
        """start the main circulation"""
        while True:
            # monitor the keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUiT:
                    sys.exit()

            # make the lately screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # create the game example and run the game
    ai = AlienInvasion()
    ai.run_game()