#-----------------------------引用部分------------------------------
import pygame
from pygame.constants import *
from pygame.locals import *
from pygame.sprite import Group

import game_functions as gf
from game_functions import GameStatus
from game_statis import Statistic
from settings import Settings
from button import Button

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
    #定义按钮
    play_button = Button(ai_settings, screen, "Play")
    #定义统计数据
    stats = Statistic(ai_settings, aliens, bullets, ships)
    #定义状态
    status = GameStatus()
    #new_alien = Alien(ai_settings, screen)
    #aliens.add(new_alien)
    #定义事件检测
    ck = gf.CheckEvent(ships, bullets, ai_settings, 
    screen, aliens, play_button, status)
    #定义帧率
    fclk = pygame.time.Clock()
#--------------------------------------------------------------------

#-----------------------------事件部分------------------------------
    #开始游戏的主循环
    while True:
        gf.ship_init(ai_settings, aliens, bullets, ships, screen)
        
        gf.alien_hitted(aliens)

        #监视键盘和鼠标事件
        ck.check_event()

        if status.game_activity():
            ships.update()
            gf.update_bullets(ai_settings, bullets)   
            gf.update_aliens(ai_settings, aliens)
#--------------------------------------------------------------------

            #print(len(bullets))
#-------------------------窗口刷新部分-----------------------------
        #每次循环都会重绘屏幕
        gf.update_screen(ai_settings, screen, ships, bullets, 
        aliens, play_button, status)
        fclk.tick(ai_settings.fps)
#--------------------------------------------------------------------

run_game()
