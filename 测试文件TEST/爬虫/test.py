# -*- coding = utf-8 -*-
# @Time : 2021/7/17 22:13
# @Author : Microtree
# @File : test.py
# @Software : PyCharm
import requests
if __name__ == "__main__":
    url = "https://tse3-mm.cn.bing.net/th/id/OIP-C.dN6TpW5W1h0w_A6d4bADCwHaEE?pid=ImgDet&rs=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70"
    }
    page_text = requests.get(url=url,headers=headers).content
    with open("tupian.jpg","wb") as fp:
        fp.write(page_text)