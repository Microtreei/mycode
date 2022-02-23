# -*- coding = utf-8 -*-
# @Time : 2021/7/19 22:19
# @Author : Microtree
# @File : girl爬虫.py
# @Software : PyCharm
import requests
from lxml import etree
import os
if not os.path.exists('./girl爬虫'):
    os.mkdir('./girl爬虫')
if __name__ == "__main__":
    for i in range(0,10):
        url = 'https://pic.netbian.com/4kmeinv/index_%d.html' % i
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70"
        }
        page_text = requests.get(url=url,headers=headers).text
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="wrap clearfix"]//ul/li')
        # for li in li_list:
        #     img_data = li.xpath('./a/img/@src')[0]
        #     img_name = li.xpath('./a/img/@alt')[0]
        #     src = 'https://pic.netbian.com'+img_data
        #     img_name = img_name.encode('iso-8859-1').decode('gbk')
        #     content = requests.get(url=src,headers=headers).content
        #     with open('girl爬虫/'+img_name+'.jpg',"wb") as fp:
        #         fp.write(content)
        #     print(img_name,"下载成功！！")
        #

