import  pygame
import  sys
from bullet import Bullet

class CheckEvent():
    def __init__(self, ship, bullets, ai_settings, screen):
        self.ship = ship
        self.bullets = bullets
        self.ai_settings = ai_settings
        self.screen = screen

    def check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            #飞船向右移动
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #飞船向左移动
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            #飞船向上移动
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            #飞船向下移动
            self.ship.moving_down = True
        elif event.key == pygame.K_RETURN:
            #开火
            if len(self.bullets.copy()) < self.ai_settings.bullet_contain:
                new_bullet = Bullet(self.ai_settings, self.screen, self.ship)
                self.bullets.add(new_bullet)

    def check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                CheckEvent.check_keydown_event(self, event)

            elif event.type == pygame.KEYUP:
                CheckEvent.check_keyup_event(self, event)

def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，将屏幕切换为最新屏幕"""
    #重新填充屏幕
    screen.fill(ai_settings.bg_color)
    #print(screen.get_height())
    #清除离开屏幕的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= -(ai_settings.bullet_speed_factor * 500):
            bullets.remove(bullet)
    #重绘所有子弹
    for bullet in bullets.sprites():
           bullet.draw_bullet(screen)
    ship.blitme(screen)
    #让新屏幕可见
    pygame.display.flip()
