import pygame.font

class Scoreboard:

    def __init__(self, ai_game):
        """initialize score keeping attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        """Create the image of scoreboard to display on screen"""
        self.score_str = str(self.stats.score)
        self.score_image = self.font.render(self.score_str, True, self.text_color, self.settings.bg_color)

        #Display the score at the top right corner of the screen
        self.rect = self.score_image.get_rect()
        self.rect.right = self.screen_rect.right - 20
        self.rect.top = 20

    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.rect)