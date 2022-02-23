# -*- coding = utf-8 -*-
# @Time : 2021/8/3 20:55
# @Author : Microtree
# @File : 弹幕爬取.py
# @Software : PyCharm
import requests
from lxml import etree
from selenium import webdriver
import time
if __name__ == "__main__":
    url = "https://www.bilibili.com/video/BV1K64y147UY?spm_id_from=333.851.b_7265636f6d6d656e64.5"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70"
    }
    bro = webdriver.Chrome(executable_path='./chromedriver.exe')
    bro.get(url=url)
    time.sleep(5)
    bro.maximize_window()

    open = bro.find_element_by_xpath('//*[@id="playerAuxiliary"]/div/div[1]/div/div[1]/div[1]/span')
    open.click()
    time.sleep(5)
    bro.find_element_by_xpath('//*[@id="playerAuxiliary"]/div/div[1]/div/div[2]/div/div[2]/div[3]/div[1]/ul/li[3]/span[2]')
    time.sleep(0.5)
    js = 'document.getElementsByClassName("bscroll-indicator")[0].scrollTop=1100'
    bro.execute_script(js)
    time.sleep(0.5)
    page_text = bro.page_source
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="playerAuxiliary"]/div/div[1]/div/div[2]/div/div[2]/div[3]/div[1]/ul/li')
    for li in li_list:
        print(li.xpath('./span[2]/text()')[0])