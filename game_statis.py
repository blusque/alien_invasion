import pygame as pg
import game_functions as gf

class Statistic:
    def __init__(self, ai_settings, aliens, bullets, ships):
        self.ai_settings = ai_settings
        self.aliens = aliens
        self.bullets = bullets
        self.ships = ships
        self.lives = ai_settings.lives
        self.scores = ai_settings.basic
        self.aliens_num = len(aliens.copy())
        self.bullets_num = ai_settings.bullet_contain
        self.time = pg.time.Clock()
        self.level = 1

    def get_alien_lose_score(self):
        lose_alien = gf.check_alien_get_bottom(self.aliens)
        self.scores += lose_alien * self.ai_settings.miss_alien
        