#-----------------------------引用部分------------------------------
import sys

import pygame
from pygame.constants import *
from pygame.locals import *
from pygame.sprite import Group

import game_functions as gf
from settings import Settings

#--------------------------------------------------------------------

#----------------------------初始化部分----------------------------
def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    #定义设置
    ai_settings = Settings()
    #定义屏幕
    #screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #定义飞船
    ships = Group()
    #定义子弹组
    bullets = Group()
    #定义外星人组
    aliens = Group()
    lines = gf.create_fleet(ai_settings, aliens, screen)
    #new_alien = Alien(ai_settings, screen)
    # aliens.add(new_alien)
    #定义时间检测
    ck = gf.CheckEvent(ships, bullets, ai_settings, screen, aliens)
    #定义帧率
    fclk = pygame.time.Clock()
#--------------------------------------------------------------------

#-----------------------------事件部分------------------------------
    #开始游戏的主循环
    while True:
        if gf.ship_died(ships):
            #print('You lose!')
            ship = gf.create_ships(ai_settings, ships, screen)
        
        if gf.alien_died(aliens):
            print('You Wiiiiiiiiiiiiiiiiiiiiiiiin!')
            sys.exit()

        #监视键盘和鼠标事件
        ck.check_event() 
        #更新飞船移动
        ship.update()
        if pygame.display.get_active():
            bullets.update()
            aliens.update(lines)
#--------------------------------------------------------------------

            #print(len(bullets))
#-------------------------窗口刷新部分-----------------------------
        #每次循环都会重绘屏幕
        gf.update_screen(ai_settings, screen, ships, bullets, aliens)
        fclk.tick(ai_settings.fps)
#--------------------------------------------------------------------

run_game()
