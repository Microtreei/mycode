# -*- coding = utf-8 -*-
# @Time : 2021/7/17 20:49
# @Author : Microtree
# @File : spider.py
# @Software : PyCharm
import requests
import re
import os
import base64
if not os.path.exists("./Libs"):
    os.mkdir('./Libs')
if __name__ == "__main__":
    url = "https://cn.bing.com/images/search?q=%e5%9f%8e%e5%b8%82%e6%91%84%e5%bd%b1&form=ISTRTH&id=58DC0BE0C9BE34D33D525D56BDFD2FD4FE10E842&cat=%e6%91%84%e5%bd%b1&disoverlay=1&first=1&tsc=ImageBasicHover"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70"
    }
    response = requests.get(url=url, headers=headers).text
    
    ex = '<div class="img_cont hoff"><img class="mimg.*?src="(.*?)" alt.*?></div>'
    image_data = re.findall(ex, response, re.S)
    for data in image_data:
        #print(data)
        if len(data) >100:
            data = base64.urlsafe_b64encode(data+'='*(4-len(data)%4))
        print(data)
    # for data in image_data:
    #     img = requests.get(url=data,headers=headers).content
    #     imgname = data.split('/')[-1]
    #     #print(imgname)
    #     with open("./Libs/"+str(img[10])+".png", "wb") as fp:
    #         fp.write(img)
