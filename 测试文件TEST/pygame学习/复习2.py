# coding:utf-8
# @Time : 2021/9/10 12:55
# @Author : Micro_tree
# @File : 复习2.py
# @Software : PyCharm
import pygame
import random

class MySprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed = 1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        self.rect.y += self.speed

class BK(MySprite):
    def update(self):
        self.rect.y+=self.speed
        if self.rect.y == self.rect.height:
            self.rect.y = -self.rect.height

class Plane(MySprite):
    def __init__(self,image_name,speed = 0):
        super(Plane, self).__init__(image_name,speed=0)
        self.rect.y = 700 - self.rect.height
        self.rect.x = 200


    def update(self):
        self.rect.x += self.speed


class Emeny(MySprite):
    def __init__(self):
        super().__init__('./emeny.png')
        self.speed = random.randint(0,5)+1
        self.rect.x = random.randint(0,7)*self.rect.width*0.2


    def update(self):
        super(Emeny, self).update()
        if self.rect.top >= 690:
            self.kill()
            print('敌机死亡')


class Buleet(MySprite):
    def __init__(self):
        super(Buleet, self).__init__('./子弹.png')

    def update(self):
        self.rect.y -= 3
        if(self.rect.bottom==0):
            self.kill()
