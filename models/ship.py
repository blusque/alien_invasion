import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图像
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #旧屏幕数据，用于缩放
        self.screen_old_bottom = float(self.screen_rect.bottom)
        self.screen_old_centerx = float(self.screen_rect.centerx)

        #在飞船的属性center中存储小数
        self.center = float(self.rect.centerx)
        self.top = float(self.rect.top)

        #移动标志
        #self.moving_right = False
        #self.moving_left = False
        #上下移动
        #self.moving_up = False
        #self.moving_down = False

    def update(self):
        """根据移动标志调整飞船位置"""
        self.rect.centerx = self.center
        self.rect.top = self.top

    def blitme(self, screen):
        """在指定位置绘制飞船"""
        #将每艘新飞船放在屏幕底部中央
        #在更改屏幕大小时要注意，如果将下面代码放在__init__里，会导致飞船位置无法和屏幕大小一起改变
        #原因是self.screen_rect的参数没有随着screen类中参数的改变而改变
        #解决方法有两种：
        #1.每次刷新屏幕时都更新ship实例，这样可以将下面代码放到__init__里
        #2.做如此处的修改，增加缩放， 并在blitme中添加参数screen，使得self.screen_rect随着screen的改变而改变
        self.screen_rect = screen.get_rect()
        #缩放
        self.rect.centerx = self.rect.centerx * float(self.screen_rect.centerx/self.screen_old_centerx)
        self.rect.bottom = self.rect.bottom * float(self.screen_rect.bottom/self.screen_old_bottom)
        #print(self.rect.centerx)
        #print(self.rect.bottom)
        #更新旧屏幕数据
        self.screen_old_centerx = self.screen_rect.centerx
        self.screen_old_bottom = self.screen_rect.bottom
        #更新位置信息
        self.center = float(self.rect.centerx)
        self.top = float(self.rect.top)
        #跟踪rect位置
        self.screen.blit(self.image, self.rect)


        #self.screen_rect = screen.get_rect()
        #if screen.get_width() == 1200:
        #if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.center += self.ai_settings.ship_speed_factor
            #print(self.moving_right)
        #elif self.moving_left and self.rect.left > 0:
            #self.center -= self.ai_settings.ship_speed_factor
            #elif self.moving_up and self.rect.top > 0:
               #self.top -= self.ai_settings.ship_speed_factor
            #elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
               #self.top += self.ai_settings.ship_speed_factor
        #elif screen.get_width() == 1280:
            #if self.moving_right and self.rect.right < self.screen_rect.right:
               #self.center += self.ai_settings.ship_speed_factor * float(1280/1200)
            #elif self.moving_left and self.rect.left > 0:
               #self.center -= self.ai_settings.ship_speed_factor * float(1280/1200)
            #elif self.moving_up and self.rect.top > 0:
               #self.top -= self.ai_settings.ship_speed_factor * float(697/600)
            #elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
               #self.top += self.ai_settings.ship_speed_factor * float(697/600)
