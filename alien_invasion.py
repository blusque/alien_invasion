from bullet import Bullet
import sys
import  pygame
from pygame.locals import  *
from pygame.constants import *
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import  Group

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), RESIZABLE, 32)
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    bullets = Group()
    ck = gf.CheckEvent(ship, bullets, ai_settings, screen)
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        ck.check_event()
        #更新飞船移动
        ship.update(screen)
        bullets.update(screen)
        #print(len(bullets))

        #每次循环都会重绘屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
