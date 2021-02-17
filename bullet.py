import  pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #在（0，0）处创建正确的子弹矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        self.screen_old_centerx = float(self.screen_rect.centerx)
        self.screen_old_bottom = float(self.screen_rect.bottom)

        self.bullet_fired = False

    def update(self):
        #if screen.get_width() == 1200:
        self.y -= self.speed_factor
        #elif screen.get_width() == 1280:
            #self.y -= self.speed_factor * (1280/1200)
        self.rect.y = self.y

    def draw_bullet(self, screen):
        self.screen_rect = screen.get_rect()
        #缩放
        self.rect.centerx = self.rect.centerx * (self.screen_rect.centerx/self.screen_old_centerx)
        self.rect.bottom = self.rect.bottom * (self.screen_rect.bottom/self.screen_old_bottom)
        #更新旧屏幕数据
        self.screen_old_centerx = self.screen_rect.centerx
        self.screen_old_bottom = self.screen_rect.bottom
        #更新子弹位置
        self.y = float(self.rect.y)

        pygame.draw.rect(self.screen, self.color, self.rect)
