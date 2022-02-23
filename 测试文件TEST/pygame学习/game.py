# coding:utf-8
# @Time : 2021/8/18 14:26
# @Author : Micro_tree
# @File : game.py
# @Software : PyCharm
import random

import pygame
import time
from sprits import *
pygame.init()


class PlayGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((1069, 800))
        self.clock = pygame.time.Clock()
        self.creat_sprit()
        pygame.time.set_timer(pygame.USEREVENT,1000)
        pygame.time.set_timer(pygame.USEREVENT+1, 1500)
    def creat_sprit(self):
        #创建背景精灵
        bg1 = BackGround('./background.jpg')
        bg2 = BackGround('./background.jpg')
        bg2.rect.y = -bg2.rect.height
        self.bg_group = pygame.sprite.Group(bg1,bg2)
        #创建飞机
        self.plane = Plane()


        #创建敌机精灵族
        self.enemy_group = pygame.sprite.Group()



    def event_header(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(1)

            if event.type == pygame.USEREVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)

            if event.type == pygame.USEREVENT+1:
                self.plane.fire()
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.plane.rect.y -= self.plane.speed
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.plane.rect.x += self.plane.speed
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.plane.rect.x -= self.plane.speed
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.plane.rect.y += self.plane.speed
        elif pygame.key.get_pressed()[pygame.K_SPACE]:
            self.plane.fires()




    def collide(self):
        pygame.sprite.groupcollide(self.plane.bult_group,self.enemy_group,True,True)
        colid = pygame.sprite.spritecollide(self.plane,self.enemy_group,True)
        if(len(colid)>0):
            self.plane.kill()
            pygame.quit()
            exit(1)

    def update(self):
        '''绘制背景精灵'''
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        '''绘制敌机'''
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.screen.blit(self.plane.image,self.plane.rect)
        self.plane.update()

        self.plane.bult_group.update()
        self.plane.bult_group.draw(self.screen)
    def start_game(self):
        while True:

            #1.设置刷新帧率
            self.clock.tick(60)
            #2.事件监听
            self.event_header()
            #3.碰撞检查
            self.collide()
            #4.更新精灵组
            self.update()
            #5.更新显示
            pygame.display.update()


if __name__ == '__main__':
    playgame = PlayGame()
    playgame.start_game()







