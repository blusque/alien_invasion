import pygame
from pygame.sprite import Sprite

class  Alien(Sprite):
    def __init__(self, ai_settings, screen, row, column):
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
        self.rect.x = column*120 + 36
        self.rect.y = row*80 + 30

        #储存外星人准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.speed_x = self.ai_settings.alien_speed_factor[0]
        self.speed_y = self.ai_settings.alien_speed_factor[1]

        self.down_stairs = False
        
    def update(self, lines):
        self.x += self.speed_x
        self.y += self.speed_y

        for line in lines:
            for alien in line:
                if alien.rect.right >= self.screen_rect.width:
                    if self.speed_x > 0:
                        self.speed_x = -self.speed_x
                    self.x += self.speed_x
                    self.y += 3
                elif alien.rect.left <= 0:
                    if self.speed_x < 0:
                        self.speed_x = -self.speed_x
                    self.x += self.speed_x
                    self.y += 3

        self.rect.x = self.x
        self.rect.y = self.y

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
