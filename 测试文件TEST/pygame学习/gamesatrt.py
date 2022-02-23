# coding:utf-8
# @Time : 2021/9/17 19:34
# @Author : Micro_tree
# @File : gamesatrt.py
# @Software : PyCharm
from tankgame import *

SCREEN_RECT  = (1024,800)

class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT)
        self.clock = pygame.time.Clock()
        self.create_sprite()
    def create_sprite(self):
        self.bg = BackGroud('./background.jpg')
        self.bg_group = pygame.sprite.Group(self.bg)



    def event_header(self):
        for event in pygame.event.get():
            if event.type == pygame.quit():
                exit(1)

    def update_sprite(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)


    def start_game(self):
        while True:
            self.clock.tick(60)
            self.event_header()
            self.update_sprite()
            pygame.display.update()
if __name__ == "__main__":
    game = Game()
    game.start_game()