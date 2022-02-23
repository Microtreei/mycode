# -*- coding = utf-8 -*-
# @Time : 2021/7/17 20:49
# @Author : Microtree
# @File : spider.py
# @Software : PyCharm
import requests
import re
import os
import base64

if not os.path.exists("./城市剪影"):
    os.mkdir('./城市剪影')
kw = input('请输入：')
if __name__ == "__main__":
    for j in range(0,10):
        kw = kw +str(j*25)
        data = {
            'q': '城市摄影',
            'first': kw,
            'count': '35',
            'cw': '1536',
            'ch': '760',
            'relp': '35',
            'tsc': 'ImageBasicHover',
            'datsrc': 'I',
            'layout': 'RowBased_Landscape',
            'mmasync': '1',
            'dgState': 'x*0_y*0_h*0_c*6_i*316_r*53',
            'IG': '59CA4F5CDB4D44DB88CE96F6880315E7',
            'SFX': '10',
            'iid': "images.5555"
        }
        url = "https://cn.bing.com/images/search?q=%e5%9f%8e%e5%b8%82%e6%91%84%e5%bd%b1&FORM=ISTRTH&id=58DC0BE0C9BE34D33D525D56BDFD2FD4FE10E842&cat=%E6%91%84%E5%BD%B1&lpversion=&disoverlay=1"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70"
        }
        response = requests.post(url=url, headers=headers,data=data).text

        ex = '<div class="img_cont hoff"><img class="mimg.*?src="h(.*?)" alt.*?</div>'
        image_data = re.findall(ex, response, re.S)



        i = 1+j*35
        for data in image_data:
            src = 'h'+data
            img = requests.get(url=src, headers=headers).content
            # with open("./Libs/"+str(i)+".jpg", "wb") as fp:
            with open('./城市剪影/' + src.split('.')[4][0:16] + '.jpg', 'wb') as fp:
                fp.write(img)
                print("%d个图片下载完成"%i)
                i += 1
