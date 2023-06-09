import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """the class which control gaming resources and actions"""

    def __init__(self):
        """initialize the game and create gaming resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # create project for restoring statistical information
        # and create scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)


        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # create Play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """start the main circulation"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """response for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """start new game when click the Play button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # reset game settings
            self.settings.initialize_dynamic_settings()

            # reset game statistical information
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # clear left bullets and aliens
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet of aliens and let ship in the middle
            self._create_fleet()
            self.ship.center_ship()

            # set mouse invisible
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """response for keydown"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """response for keyup"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """create a bullet and add it to bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """refresh the bullet's position and delete dispearing bullet"""
        # refresh the bullet's position
        self.bullets.update()

        # delete dispearing bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """respond to the collision"""
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # delete existing bullet and create a new group of aliens
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # increase level
            self.stats.level += 1
            self.sb.prep_level()

            # increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """check if any alien by the edge,
        refresh all the aliens' position in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        # check collision between ship and alien
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # check if any alien arrive the bottom
        self._check_aliens_bottom()

        if not self.aliens:
            # delete existing bullet and create a new group of aliens
            self.bullets.empty()
            self._create_fleet()

    def _ship_hit(self):
        """responding for ship hit by aliens"""
        if self.stats.ships_left > 0:
            # ships_left substract 1
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # delete the rest aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet aliens and put the ship to the middle
            self._create_fleet()
            self.ship.center_ship()

            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """check if any alien reach the bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # manage it as same as collision
                self._ship_hit()
                break

    def _create_fleet(self):
        """create alien groups"""
        # create an alien and calculate how many aliens a line can hold
        # the space between aliens is its width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # calculate how many rows the screen can hold
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # create the alien fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number,  row_number):
        """create an alien and add it to the line"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """move the aliens fleet downward and change their direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """update the image and switch to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # show scores
        self.sb.show_score()

        # if the game being False, draw Play button
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # create the game example and run the game
    ai = AlienInvasion()
    ai.run_game()
