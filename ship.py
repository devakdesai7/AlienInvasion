import pygame

class Ship:
    """A class to represent the player's Shooting Ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.scaled_image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.scaled_image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.scaled_image, self.rect)