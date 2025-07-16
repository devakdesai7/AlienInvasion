import pygame
import settings

class Ship:
    """A class to represent the player's Shooting Ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = settings.Settings()

        #Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.scaled_image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.scaled_image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Movement flags
        self.move_right = False
        self.move_left = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.scaled_image, self.rect)
    
    def update(self):
        """Update the ship's position based on the movement flags"""
        if self.move_right:
            self.rect.x += 1
            if self.rect.right > self.settings.screen_width:
                self.rect.right = self.settings.screen_width
        if self.move_left:
            self.rect.x -= 1
            if self.rect.left < 0:
                self.rect.left = 0