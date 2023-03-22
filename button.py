import pygame.font

class Button:

    def __init__(self,ai_game,msg):
        """initailize the button settings"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set the size of the button and other settings
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # create button's rect and make it in the middle
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # create the button only once
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """render msg to image and make it in the botton's middle"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw a button filled with color,then draw the text
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)