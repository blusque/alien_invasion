import random as rd
import sys

import pygame

from alien import Alien
from bullet import Bullet
from ship import Ship 


class CheckEvent():
    def __init__(self, ships, bullets, ai_settings, screen, aliens):
        self.ships = ships
        self.bullets = bullets
        self.ai_settings = ai_settings
        self.screen = screen
        self.aliens = aliens

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

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                CheckEvent.check_keydown_event(self, event)

            elif event.type == pygame.MOUSEMOTION:
                CheckEvent.check_mousemotion_event(self, event)

def create_fleet(ai_settings, aliens, screen):
    lines = []
    for line in range(ai_settings.alien_tot_line):
        alien = []
        lines.append(alien)
        for i in range(ai_settings.alien_one_line):
            row = line
            column = i
            alien.append(Alien(ai_settings, screen, row, column))
            aliens.add(alien[i])
    return lines

def ship_died(ships):
    if not len(ships.copy()):
        return True
    else:
        return False

def create_ships(ai_settings, ships, screen):
    new_ship = Ship(ai_settings, screen)
    if ai_settings.lives > 0:
        ships.add(new_ship)
        ai_settings.lives -= 1
        #print(new_ship)
        return new_ship
    else: sys.exit()

def alien_died(aliens):
    if not len(aliens.copy()):
        return True
    else:
        return False

def alien_draw(ai_settings, aliens, screen):
    #重绘所有外星人
    for alien in aliens.sprites():
        alien.blitme(screen)
    #清除离开屏幕的外星人
    for alien in aliens.copy():
        if alien.rect.top >= (ai_settings.screen_height):
            aliens.remove(alien)


def bullet_draw(ai_settings, bullets, screen):
    #清除离开屏幕的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= -(ai_settings.bullet_speed_factor * 300):
            bullets.remove(bullet)
    #重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet(screen)


def update_screen(ai_settings, screen, ships, bullets, aliens):
    """更新屏幕上的图像，将屏幕切换为最新屏幕"""
    #重新填充屏幕
    screen.fill(ai_settings.bg_color)
    #print(screen.get_height())
    alien_draw(ai_settings, aliens, screen)
    bullet_draw(ai_settings, bullets, screen)
    #检测碰撞
    collisions1 = pygame.sprite.groupcollide(bullets, aliens, True, True)
    collisions2 = pygame.sprite.groupcollide(aliens, ships, True, True)
    for ship in ships.copy():
        ship.blitme(screen)
    #让新屏幕可见
    pygame.display.flip()
