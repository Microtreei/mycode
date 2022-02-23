# coding:utf-8
# @Time : 2021/8/4 15:47
# @Author : Micro_tree
# @File : WorldCloud 词云模块使用.py
# @Software : PyCharm
if __name__ == "__main__":
    from matplotlib.image import imread
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
    import os
    font = '你自己电脑中安装的字体的路径'
    kw_str = '今天 的 天气 真不错 啊，我们 一起 去 吃饭吧！'  # 你需要进行可视化的字符串
    color_mask = imread(os.getcwd() + "/python.jpg")  # 读取背景图片
    cloud = WordCloud(
        # 设置字体，不指定就会出现乱码
        font_path=font,  # 这个路径是pc中的字体路径
        # 设置背景色
        background_color='white',
        # 词云形状
        mask=color_mask,
        # 允许最大词汇
        max_words=2000,
        # 最大号字体
        max_font_size=40
    )
    word_cloud = cloud.generate(kw_str)  # 产生词云,输入的格式是以空格分隔的词语组成的字符串
    word_cloud.to_file("pjl_cloud4.jpg")  # 保存图片
    #  显示词云图片
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()
