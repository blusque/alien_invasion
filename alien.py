import pygame
from pygame.sprite import Sprite

class  Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #初始化屏幕信息
        self.screen_rect = screen.get_rect()
        self.screen_old_bottom = self.screen_rect.bottom
        self.screen_old_centerx = self.screen_rect.centerx

        #加载外星人图像，并设置其rect值
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #储存外星人准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.speed_x = self.ai_settings.alien_speed_factor
        self.down_speed = self.ai_settings.alien_down_speed

        self.down_stairs = False
        
    def update(self):
        """水平移动外星人"""
        self.x += self.speed_x * self.ai_settings.alien_x_direct
        self.rect.x = self.x

    def check_edge(self):
        """检测外星人是否在边缘"""
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True

    def blitme(self, screen):
        """在准确位置绘制外星人"""
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
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.top = float(self.rect.top)
        #跟踪rect位置
        self.screen.blit(self.image, self.rect)
