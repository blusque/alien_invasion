import random as rd
import sys

import pygame

from alien import Alien
from bullet import Bullet
from ship import Ship 
from time import sleep


class CheckEvent():
    """一个用于处理事件的类"""

    def __init__(self, ships, bullets, ai_settings, screen, aliens, play_button, status):
        self.ships = ships
        self.bullets = bullets
        self.ai_settings = ai_settings
        self.screen = screen
        self.aliens = aliens
        self.play_button = play_button
        self.status = status

    def check_keydown_event(self, event):
        if event.key == pygame.K_SPACE:
            #开火
            if len(self.bullets.copy()) < self.ai_settings.bullet_contain:
                for ship in self.ships.copy():
                    new_bullet = Bullet(self.ai_settings, self.screen, ship)
                    self.bullets.add(new_bullet)
        elif event.key == pygame.K_ESCAPE:
            #退出
            sys.exit()
        elif event.key == pygame.K_UP:
            self.ai_settings.up_speed()
        elif event.key == pygame.K_DOWN:
            self.ai_settings.down_speed()

    def check_mousemotion_event(self, event):
        VInfo = pygame.display.Info()
        for ship in self.ships.copy():
            if ship.rect.right < VInfo.current_w and ship.rect.left > 0:
                ship.center = event.pos[0]
            elif ship.rect.right >= VInfo.current_w:
                ship.center -= 2
            elif ship.rect.left <= 0:
                ship.center += 2
        #print("[MOUSEMOTION]: ", event.pos)

    def check_mousebuttondown_event(self, event):
        mouse = {}
        mouse['x'], mouse['y'] = pygame.mouse.get_pos()
        if self.play_button.rect.collidepoint(mouse['x'], mouse['y']):
            self.status.game_active = True


    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                CheckEvent.check_keydown_event(self, event)

            elif event.type == pygame.MOUSEMOTION:
                CheckEvent.check_mousemotion_event(self, event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                CheckEvent.check_mousebuttondown_event(self, event)


class CreateAlien():
    """一个用于创建外星人的类"""

    def __init__(self, ai_settings, screen, aliens):
        self.ai_settings = ai_settings
        self.screen = screen
        self.aliens = aliens
        #创建一个模型外星人
        self.alien = Alien(ai_settings, screen)
        self.screen_height = ai_settings.screen_height
        self.screen_width = ai_settings.screen_width

    def __get_alien_width(self):
        """获取外星人的宽度"""
        alien_width = self.alien.rect.width
        return alien_width

    def __get_alien_height(self):
        """获取外星人的高度"""
        alien_height = self.alien.rect.height
        return alien_height

    def __get_number_aliens_x(self, alien_width):
        """获取一行中外星人的个数"""
        available_space_x = self.screen_width - 2*alien_width
        number_aliens_x = int(available_space_x / (2*alien_width))
        return number_aliens_x

    def __get_number_rows(self, alien_height):
        """获取行数"""
        available_space_y = self.screen_height - 4*alien_height
        number_rows = int(available_space_y / (1.5*alien_height))
        return number_rows

    def __create_alien(self, alien_width, alien_height, alien_number, row):
            """创建一个外星人"""
            alien = Alien(self.ai_settings, self.screen)
            alien.x = alien_width + 2*alien_width*alien_number
            alien.y = alien_height + 1.5*alien_height*row
            alien.rect.x = alien.x
            alien.rect.y = alien.y
            self.aliens.add(alien)

    def create_fleet(self):
        """创建外星人群"""
        #创建一个外星人，并计算一行可容纳多少个外星人
        #外星人间距为外星人宽度
        alien_width = CreateAlien.__get_alien_width(self)
        alien_height = CreateAlien.__get_alien_height(self)
        number_aliens_x = CreateAlien.__get_number_aliens_x(self,alien_width)
        number_rows = CreateAlien.__get_number_rows(self, alien_height)

        #创建多行外星人
        for row in range(number_rows):
            #print(number_rows)
            #创建一行外星人
            for alien_number in range(number_aliens_x):
                #创建一个外星人并将其加入当前行
                CreateAlien.__create_alien(self, alien_width, alien_height, alien_number, row)



def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_down_speed
    ai_settings.alien_x_direct *= -1
    aliens.update()

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings, aliens)

def update_aliens(ai_settings, aliens):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()



def bullet_draw(bullets, screen):
    #重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet(screen)

def update_bullets(ai_settings,  bullets):
    #清除离开屏幕的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= -(ai_settings.bullet_speed_factor * 300):
            bullets.remove(bullet)
    bullets.update()



def ship_died(ships):
    if not len(ships.copy()):
        return True
    else:
        return False

def alien_died(aliens):
    if not len(aliens.copy()):
        return True
    else:
        return False

def create_ships(ai_settings, aliens, bullets, ships, screen):
    if ai_settings.lives > 0:
        new_ship = Ship(ai_settings, screen)
        ships.add(new_ship)

        aliens.empty()
        bullets.empty()

        ai_settings.lives -= 1
        #print(new_ship)
    else: 
        print("Ship hit!")
        sys.exit()

def alien_hitted(aliens):
    if alien_died(aliens):
        print('You Wiiiiiiiiiiiiiiiiiiiiiiiin!')
        sys.exit()


def ship_init(ai_settings, aliens, bullets, ships, screen):
    if ship_died(ships):
        #print('You lose!')
        create_ships(ai_settings, aliens, bullets, ships, screen)
        #定义外星人生成
        my_alien = CreateAlien(ai_settings, screen, aliens)
        my_alien.create_fleet()

        sleep(0.5)



def check_collisions(aliens, bullets, ships):
    #检测碰撞
    collisions1 = pygame.sprite.groupcollide(bullets, aliens, True, True)
    collisions2 = pygame.sprite.groupcollide(aliens, ships, True, True)
    """
    print(collisions1)
    print(collisions2)
    """

def check_alien_get_bottom(aliens):
    #记录一次消失的飞船
    count = 0
    for alien in aliens.copy():
        if alien.rect.top >= alien.screen_rect.height:
            aliens.remove(alien)
            count += 1
    return count



class GameStatus():
    """一个用于处理游戏状态的类"""

    def __init__(self):
        self.game_active = False
        self.screen_avtive = pygame.display.get_active()

    def game_activity(self):
        GameStatus.close_screen_check(self)
        if self.game_active and self.screen_avtive:
            return True
    
    def close_screen_check(self):
        if not pygame.display.get_active():
            self.game_active = False



def update_screen(ai_settings, screen, ships, bullets, aliens, play_button, status):
    """更新屏幕上的图像，将屏幕切换为最新屏幕"""
    #重新填充屏幕
    screen.fill(ai_settings.bg_color)
    #判断碰撞
    check_collisions(aliens, bullets, ships)
    ships.draw(screen)
    aliens.draw(screen)
    bullet_draw(bullets, screen)
    if not status.game_activity():
        play_button.draw_button()
    #让新屏幕可见
    pygame.display.flip()
        
