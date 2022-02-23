# -*- coding = utf-8 -*-
# @Time : 2021/7/26 15:37
# @Author : Microtree
# @File : 爬虫  萌系.py
# @Software : PyCharm
import os
import requests
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70"
        }
if __name__ == "__main__":

   url = 'https://tse1-mm.cn.bing.net/th/id/OIP-C.9FhUZzcMnWrL8tuIeTb0oQHaKt?w=206&h=299&c=7&o=5&dpr=1.25&pid=1.7'
   data = requests.get(url=url,headers=headers).content
   with open('./城市.jpg','wb') as fp:
       fp.write(data)
