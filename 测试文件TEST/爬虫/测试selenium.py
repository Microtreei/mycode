# -*- coding = utf-8 -*-
# @Time : 2021/7/25 22:39
# @Author : Microtree
# @File : 测试selenium.py
# @Software : PyCharm

#标签定位
#滚轮拖动
#搜索
#搜索框输入

import requests
import time
from selenium import webdriver
from lxml import etree
from time import sleep
import os
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70"
        }
if __name__ == "__main__":
    bro = webdriver.Chrome(executable_path='./chromedriver.exe')
    bro.get('https://cn.bing.com/images/search?q=%E5%8F%AF%E7%88%B1%E7%BE%8E%E5%A5%B3')
    bro.execute_script('window.scroll(0,document.body.scrollHeight)')
    sleep(2)
    bro.execute_script('window.scroll(0,document.body.scrollHeight)')
    sleep(2)
    bro.execute_script('window.scroll(0,document.body.scrollHeight)')
    sleep(2)
    bro.execute_script('window.scroll(0,document.body.scrollHeight)')
    page = bro.page_source
    tree = etree.HTML(page)
    if not os.path.exists('./python爬虫cute'):
        os.mkdir('./python爬虫cute')


    for a in range(1,10):
        li_list = tree.xpath('//*[@id="mmComponent_images_1_list_%s"]/li' % str(a))
        for li in li_list:
            src = li.xpath('.//img[@class]/@src')[0]
            if src[0:3]!='htt':
                continue
            name =str(time.time())
            content = requests.get(url=src,headers=headers).content
            with open('python爬虫cute/' +name+'.jpg','wb') as fp:
                fp.write(content)
            print('%s下载完成'%name)

    sleep(5)
    bro.quit()

