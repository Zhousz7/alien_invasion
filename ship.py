import pygame
class Ship:
    """the class the manage the ship"""

    def __init__(self,ai_game):
        """initialize the ship and its biginning position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its bounding rectangle
        self.image = pyagme.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # for every new ship,put it on the middle of bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """draw the ship on giving position"""
        self.screen.blit(self.image,self.rect)
        