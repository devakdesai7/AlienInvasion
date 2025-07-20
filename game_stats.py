import pygame

class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self._reset_stats()

    def _reset_stats(self):
        self.ships_left = self.settings.ship_limit