# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from wordcloud import WordCloud


class TieMat():
    def client_pie(self, data):
        "发帖来源饼图"
        # client缺失值填充为网页端
        data = data.fillna({'client':'网页端'})
        data_client = data['client'].value_counts()
        # 合并数据为其它
        data1 = pd.concat([data_client[:3],
              pd.Series([data_client[3:].sum()], index=['其它'])])
        labels = data1.index
        # 饼图
        fig, ax = plt.subplots(figsize=(12,9))
        ax.pie(data1, labels=labels, autopct = '%2.1f%%', startangle =90,)
        ax.set_title("发帖来源饼图", fontsize=19)
        plt.axis('equal')
        # 图例
        ax.legend(loc=3)
        plt.show()
        plt.savefig('发帖来源饼图')
        
    def level_bar(self, data):
        "用户等级条形图"
        # 去掉重复数据
        data1 = data.drop_duplicates(['user_name','user_level'])
        y = data1['user_level'].value_counts()
        x = y.index
        # 条形图
        plt.figure(figsize=(12,9))
        plt.bar(x, y)
        plt.xticks(x)
        plt.ylim(0,60000)
        # 显示横轴标签
        plt.xlabel("等级", fontsize=15)
        # 显示图标题
        plt.title("用户等级分布条形图", fontsize=19)
        for a,b in zip(x,y):
            plt.text(a, b + 1000, '%.0f'%b, ha='center', 
                     va='bottom', fontsize=10)
        plt.show()
        plt.savefig('用户等级分布条形图')
    
    def time_plot(self, data):
        "用户发帖时间折线图"
        # 取发帖时间的小时作为发帖时间
        data['create_time'] = data['create_time'].str[:2]
        y = data['create_time'].value_counts()
        x = y.index
        label = [str(i) + '时' for i in range(0,24)]
        # 折线图
        plt.figure(figsize=(12,9))
        plt.plot(x, y)
        plt.xticks(x, label)
        plt.xlabel('发帖时间', fontsize=15)
        plt.title('用户发帖时间折线图', fontsize=19)
        plt.show()
        plt.savefig('用户发帖时间折线图')
        
    def name_wordcloud(self, data):
        "昵称词云图"
        # 过滤掉nan
        data2 = data['user_name'].dropna()
        txt = ' '.join(data2)
        w = WordCloud(width=800, height=600, 
                      background_color='white',
                      font_path='C:\Windows\Fonts\simsun.ttc')
        w.generate(txt)
        # 显示词云图片
        plt.figure(figsize=(12,9))
        plt.imshow(w)
        plt.axis('off')
        # 保存图片
        w.to_file('昵称词云图.png')
        plt.show()
        
if __name__ == "__main__":
    data = pd.read_csv('hai.csv')
    # 设置matplotlib正常显示中文
    matplotlib.rcParams['font.sans-serif']=['SimHei']
    tu = TieMat()
    
    tu.client_pie(data)
    tu.level_bar(data)
    tu.time_plot(data)
    tu.name_wordcloud(data)
