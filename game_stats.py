import pygame

class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self._reset_stats()
        self.game_active = False #making game_active = False because we want the game loop to run after we press the play button

    def _reset_stats(self):
        self.ships_left = self.settings.ship_limit