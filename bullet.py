import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """the class that manage the bullets shot by ship"""

    def __init__(self, ai_game):
        """create a bullet object on the ship's position"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a rectangle on (0,0), then put it on porper position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet's position decimally
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet upward"""
        # refresh the number which indicates the bullet's position
        self.y -= self.settings.bullet_speed
        # refresh the bullet's rect that represents the bullet's position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
