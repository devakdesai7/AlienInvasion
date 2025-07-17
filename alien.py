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
        self.scaled_image = pygame.transform.scale(self.image, (150,150))
        self.rect = self.scaled_image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y - self.rect.height

        #Store the alien's horizontal position as a decimal
        self.x = float(self.rect.x)