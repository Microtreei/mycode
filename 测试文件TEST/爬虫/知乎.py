# coding:utf-8
# @Time : 2021/9/8 10:56
# @Author : Micro_tree
# @File : 知乎.py
# @Software : PyCharm
import time

if __name__ == "__main__":
    import requests
    from lxml import etree
    from selenium import webdriver

    bro = webdriver.Chrome(executable_path='./chromedriver.exe')
    bro.get('https://www.zhihu.com/hot')
    bro.maximize_window()
    time.sleep(2)
    tree_list = bro.find_element_by_xpath('//*[@id="TopstoryContent"]/div/div/div[2]/section')

    for tr in tree_list:
        page = tr.xpath('./div[2]/h2/text()')
        page2 = tr.xpath('./div[2]/p/text()')
        print(page)
        print(page2)


