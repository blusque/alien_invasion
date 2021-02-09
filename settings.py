class Settings():
    """本类用于描述《alien invasion》中所有设置"""
    def __init__(self):
        #屏幕长与宽
        self.screen_width = 1200
        self.screen_height = 600
        #背景颜色
        self.bg_color = (230, 230, 230)
        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_contain = 3
