# coding:utf-8
# @Time : 2021/9/10 12:54
# @Author : Micro_tree
# @File : 复习.py
# @Software : PyCharm
import pygame.sprite

from 复习2 import *
pygame.init()
class Play(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.create_sprite()
        self.screen = pygame.display.set_mode((480,700))
        self.ti = pygame.USEREVENT
        self.ti1 = pygame.USEREVENT+1
        pygame.time.set_timer(self.ti,1000)
        pygame.time.set_timer(self.ti1,1500)        #设置定时器
    def event_header(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       #这里是event type
                pygame.quit()
                exit(1)
            if event.type == self.ti:
                enemy = Emeny()
                self.enemy_group.add(enemy)
            if event.type == self.ti1:
                self.bullt = Buleet()
                self.bullt.rect.centerx = self.plane.rect.centerx
                self.bullt.rect.bottom = self.plane.rect.top - 10
                self.buleet_list.add(self.bullt)

                #键盘按键
        if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.plane.rect.x -= 2
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.plane.rect.x += 2

    def collision(self):
        pygame.sprite.spritecollide(self.plane,self.enemy_group,True)
        pygame.sprite.groupcollide(self.buleet_list,self.enemy_group,True,True)
    def update_all(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.plane.update()
        self.screen.blit(self.plane.image,self.plane.rect)


        self.enemy_group.draw(self.screen)
        self.enemy_group.update()

        self.buleet_list.update()
        self.buleet_list.draw(self.screen)      #draw方法
    def create_sprite(self):
        self.bg1 = BK('./background.jpg')
        self.bg2 = BK('./background.jpg')
        self.bg2.rect.y = -self.bg2.rect.height
        self.bg_group = pygame.sprite.Group(self.bg1,self.bg2)


        self.plane = Plane('./plane.png')



        self.enemy_group = pygame.sprite.Group()


        self.buleet_list = pygame.sprite.Group()

        self.buleet_list = pygame.sprite.Group()
    def start_game(self):
        while True:
            self.clock.tick(60)
            self.event_header()
            self.update_all()
            self.collision()
            pygame.display.update()     #注意更新显示

if __name__ == "__main__":
    game = Play()
    game.start_game()

