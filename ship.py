import pygame
class Ship:
    """the class the manage the ship"""

    def __init__(self,ai_game):
        """initialize the ship and its biginning position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its bounding rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # for every new ship,put it on the middle of bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store x with decimal numbers
        self.x = float(self.rect.x)

        # moving signal
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update ship's position according to the moving signal"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update the rect object according to self.x
        self.rect.x = self.x


    def blitme(self):
        """draw the ship on giving position"""
        self.screen.blit(self.image,self.rect)
