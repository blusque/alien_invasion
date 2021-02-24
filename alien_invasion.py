#-----------------------------引用部分------------------------------
import pygame
from pygame.constants import *
from pygame.locals import *
from pygame.sprite import Group

import game_functions as gf
from button import Button, SButton
from game_functions import GameStatus
from game_stats import Statistic
from settings import Settings
from scoreboard import Bar, ScoreBoard

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
    #定义统计数据
    stats = Statistic(ai_settings, aliens, bullets, ships)
    #定义头顶菜单
    bar = Bar(screen)
    score = ScoreBoard(ai_settings, stats, screen = screen)
    #定义按钮
    play_button = Button(ai_settings, screen, "Play")
    restart_button = SButton(ai_settings, screen, "Restart", 540, 360, 32)
    exit_button = SButton(ai_settings, screen, "Exit", 660, 360, 32)
    #定义状态
    status = GameStatus()
    #new_alien = Alien(ai_settings, screen)
    #aliens.add(new_alien)
    #定义是否是第一次
    class Init():
        def __init__(self):
            self.bool = True
        
        def assign(self, bool_sign):
            self.bool = bool_sign
    
    init = Init()
    #定义事件检测
    ck = gf.CheckEvent(ships, bullets, ai_settings, 
    screen, aliens, play_button, restart_button, exit_button, status, stats, init)
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
        aliens, play_button, restart_button, exit_button, bar, score, status, stats)
        fclk.tick(ai_settings.fps)
#--------------------------------------------------------------------

run_game()
