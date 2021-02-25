import pygame as pg
import settings.game_functions as gf
import os
import json
import time

class Statistic:
    def __init__(self, ai_settings, aliens = None, bullets = None, ships = None):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # __file__获取执行文件相对路径，整行为取上一级的上一级目录
        self.filename = BASE_DIR + "\saves\data\score_data.json"
        #print(self.filename)

        self.ai_settings = ai_settings
        self.aliens = aliens
        self.bullets = bullets
        self.ships = ships
        self.lives = ai_settings.lives
        self.score = ai_settings.basic
        self.read_topscore()
        self.old_top = self.topscore
        self.aliens_num = len(aliens.copy())
        self.bullets_num = ai_settings.bullet_contain
        self.time = pg.time.Clock()
        self.level = 0

        #最近一次刷新时击落的外星人
        self.now_kill = 0

    def read_topscore(self):
        try:
            with open(self.filename, 'r') as file_obj:
                self.topscore = json.load(file_obj)
        except FileNotFoundError:
            self.topscore = 0

    def fresh_topscore(self):
        if self.score > self.topscore:
            self.topscore = self.score

    def write_topscore(self):
        if self.topscore > self.old_top:
            with open(self.filename, 'w') as file_obj:
                json.dump(self.topscore, file_obj)

    def get_alien_lose_score(self):
        lose_alien = gf.check_alien_get_bottom(self.aliens)
        self.score += lose_alien * self.ai_settings.miss_alien
        if lose_alien:
            print("lose alien")

    def get_score(self):
        self.score += self.now_kill * self.ai_settings.alien_point

    def get_ship_lose_score(self):
        if self.score >= -(self.ai_settings.ship_hitted):
            self.score += self.ai_settings.ship_hitted
        elif self.score > 0 and self.score < -(self.ai_settings.ship_hitted):
            self.score = 0
        print("lose ship")

    def check_collisions(self):
        #检测碰撞
        self.now_kill = 0
        for bullet in self.bullets:
            if bullet.rect.top >= 40:
                alien = None
                alien = pg.sprite.spritecollideany(bullet, self.aliens)
                if alien != None:
                    #print("lose alien")
                    self.aliens.remove(alien)
                    self.bullets.remove(bullet)
                    self.now_kill += 1
        self.get_score()
                #collisions1 = pygame.sprite.spritecollideany(bullet, aliens)
        collisions = {}
        collisions = pg.sprite.groupcollide(self.aliens, self.ships, True, True)
        if collisions != {}:
            self.get_ship_lose_score()
        
