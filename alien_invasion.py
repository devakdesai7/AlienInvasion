import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class which will contain the game logic and game loop"""

    def __init__(self):
        """Initialize the game, and set the settings of the game"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop of the game"""
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redraw the screen through each pass of the loop
            self.screen.fill(self.settings.bg_color)

            #Draw the ship to the game window
            self.ship.blitme()

            #Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()