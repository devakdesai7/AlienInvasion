import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:

    def __init__(self, ai_game):
        """initialize score keeping attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_current_level()
        self.prep_ships()

    def prep_score(self):
        """Create the image of scoreboard to display on screen"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)    
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #Display the score at the top right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Create the image of high score to display on screen"""
        rounded_high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(f"High Score: {high_score_str}", True, self.text_color, self.settings.bg_color)

        #Display the high score at the top right corner of the and below the current score
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_current_level(self):
        """Create the image of current level of player to display on screen"""
        level_str = str(self.stats.current_level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()

        self.level_rect.top = self.score_rect.bottom + 5
        self.level_rect.right = self.score_rect.right

    def prep_ships(self):
        """Create a group of ship sprites and initialize their positions"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.size = (5, 5)
            ship.rect.x = 10 + (ship_number * ship.rect.width)
            ship.rect.y = 10
            self.ships.add(ship)


    def show_score(self):
        """Draw score, number of ships left and level to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
