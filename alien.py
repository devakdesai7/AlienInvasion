import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to manage alien fleet"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the image and make its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's horizontal position as a decimal
        self.x = float(self.rect.x)

    def update(self):
        """Making the fleet move left and right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return true if alien has touched an edge"""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True