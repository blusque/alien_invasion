import pygame as pg
import game_functions as gf

class Statistic:
    def __init__(self, ai_settings, aliens = None, bullets = None, ships = None):
        self.ai_settings = ai_settings
        self.aliens = aliens
        self.bullets = bullets
        self.ships = ships
        self.lives = ai_settings.lives
        self.score = ai_settings.basic
        self.aliens_num = len(aliens.copy())
        self.bullets_num = ai_settings.bullet_contain
        self.time = pg.time.Clock()
        self.level = 0

        #最近一次刷新时击落的外星人
        self.now_kill = 0

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
        
