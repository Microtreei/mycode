# coding:utf-8
# @Time : 2021/8/25 15:37
# @Author : Micro_tree
# @File : 1.散点图的绘制.py
# @Software : PyCharm
import xlrd
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r'D:\下载-----------\IDM下载\seaborn-data-master\tips.csv')
data.head()
sns.scatterplot(x='total_bill',y='sex',data=data)
plt.show()





