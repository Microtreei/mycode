# coding:utf-8
# @Time : 2021/8/19 10:30
# @Author : Micro_tree
# @File : sprits.py
# @Software : PyCharm
import random
import pygame


class GameSprits(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class BackGround(GameSprits):

    def update(self):
        super().update()
        if self.rect.y == self.rect.height:
            self.rect.y = -self.rect.height


class Ballut(GameSprits):
    def __init__(self):
        super(Ballut, self).__init__('./子弹.png',speed=-1)

    def update(self):
        super(Ballut, self).update()
        if self.rect.bottom < 0:
            self.kill()


class Plane(GameSprits):
    def __init__(self):
        super(Plane, self).__init__('./plane.png')

        self.rect.center = (1048/2,800-self.rect.height)

        self.speed = 2
        self.bult_group = pygame.sprite.Group()

    def update(self):
        if self.rect.right <0:
            self.rect.left = 1069
        if self.rect.left > 1069:
            self.rect.right =0
        if self.rect.top >= 800-1:
            self.rect.y =-self.rect.height/2
        if self.rect.bottom <=0:
            self.rect.top =800
    def fire(self):
        bult = Ballut()
        bult.rect.bottom = self.rect.top
        bult.rect.centerx = self.rect.centerx
        self.bult_group.add(bult)
    def fires(self):
        for i in range(0,2):
            bult = Ballut()
            bult.rect.bottom = self.rect.top-bult.speed*i*30
            bult.rect.centerx = self.rect.centerx
            self.bult_group.add(bult)

class Enemy(GameSprits):
    def __init__(self):
        super().__init__('./emeny.png')
        self.speed = random.randint(1,5)
        self.rect.x = random.randint(0,1048-self.rect.width)
        self.rect.bottom = 0
    def update(self):
        super(Enemy, self).update()
        if self.rect.y>800:
            self.kill()


