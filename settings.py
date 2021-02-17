import pygame

class Settings():
    """本类用于描述《alien invasion》中所有设置"""
    def __init__(self):
        VInfo = pygame.display.Info()
        #屏幕长与宽
        self.screen_width = 1200
        self.screen_height = 600
        #背景颜色
        self.bg_color = 230, 230, 230
        #飞船设置
        self.ship_speed_factor = 6
        self.lives = 4
        #子弹设置
        self.bullet_speed_factor = 8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_contain = 3
        #外星人设置
        self.alien_tot_line = 4
        self.alien_one_line = 6
        self.alien_speed_factor = [3, 0]
        #帧率设置
        self.fps = 60
        #难度设置
        self.__level = "Normal"
    
    def up_speed(self):
        if self.ship_speed_factor < 10:
            self.ship_speed_factor += 1

    def down_speed(self):
        if self.ship_speed_factor > 4:
            self.ship_speed_factor -= 1