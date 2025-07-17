import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class which will contain the game logic and game loop"""

    def __init__(self):
        """Initialize the game, and set the settings of the game"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop of the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_alien()
            self._update_screen()

        
    def _check_events(self):
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def _fire_bullet(self):
        """Create new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_alien(self):
        """Check if an alien is at an edge and appropriately 
        update the positions of all aliens in a fleet"""
        self._check_edges()
        self.aliens.update()

    def _check_edges(self):
        """Return true if alien is at any one of the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        """Create the fleet of aliens"""
        #Create an alien and find the number of aliens in a row
        #Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 *alien_width)
        number_of_aliens = available_space_x // (2 * alien_width)

        #Determining the number of rows that can fit into the screen
        available_vertical_space = self.settings.screen_height - (3 * alien_height) - (self.ship.rect.height)
        number_of_rows = available_vertical_space // (2 * alien_height)

        #Create the full fleet of the aliens
        for number_row in range(number_of_rows):
            for alien_number in range(number_of_aliens):
                self._create_alien(alien_number, number_row)

    def _create_alien(self, alien_number, number_row):
         #Create an alien and place it in the first row
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + (2 * alien_width * alien_number)
            alien.rect.x = alien.x
            alien.rect.y = alien_height + (2 * alien_height * number_row)
            self.aliens.add(alien)      

    def _update_screen(self):
        #Redraw the screen through each pass of the loop
        self.screen.fill(self.settings.bg_color)

        #Draw the ship to the game window
        self.ship.blitme()

        #Draw bullets from the self.bullets.sprites list to shoot
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #Draw alien fleet on the screen from the self.aliens group
        self.aliens.draw(self.screen)
        
        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()