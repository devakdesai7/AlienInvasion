import pygame

class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self._reset_stats()
        self.game_active = False #making game_active = False because we want the game loop to run after we press the play button
        self.high_score = 0

    def _reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.current_level = 1