# coding:utf-8
# @Time : 2021/9/17 19:29
# @Author : Micro_tree
# @File : tankgame.py
# @Software : PyCharm
import pygame
class MySprite(pygame.sprite.Sprite):
    def __init__(self,image_name):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()

    def update(self, *args, **kwargs) -> None:
        pass


class BackGroud(MySprite):
    pass

class MyTank(MySprite):
    pass



