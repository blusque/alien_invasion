
class Settings():
    """本类用于描述《alien invasion》中所有设置"""
    def __init__(self):
        #屏幕长与宽
        self.screen_width = 1200
        self.screen_height = 600
        #背景颜色
        self.bg_color = 230, 230, 230
        #飞船设置
        self.ship_speed_factor = 6
        self.origin_lives = 4
        self.lives = 4
        #子弹设置
        self.bullet_speed_factor = 8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_contain = 3
        #外星人设置
        self.alien_one_line = 9
        self.alien_speed_factor = 4
        self.alien_down_speed = 15
        self.alien_x_direct = 1
        #帧率设置
        self.fps = 60
        #难度设置
        self.__level = "Normal"
        #点数设置
        self.alien_point = 300
        self.miss_alien = -450
        self.lose_bullet = -60
        self.ship_hitted = -1200
        self.basic = 0
        #主要按钮设置
        self.button_size = 200, 50
        self.button_color = 255, 0, 0
        self.text_color = 255, 255, 255
        #次级按钮设置
        self.s_button_size = 80, 40
        self.s_button_color = 0, 255, 0
        self.s_text_color = 255, 255, 255
        #字体
        self.title_font_size = 48
        self.next_title_font_size = 32
        self.score_font_size = 32
        self.other_font_size = 24