# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#设置matplotlib正常显示中文和负号
matplotlib.rcParams['font.sans-serif']=['SimHei']
matplotlib.rcParams['axes.unicode_minus']=False 

def salary(x):
    """
    例：salary  8k-15k
    取salary范围的中值作为salary
    """
    li = x.split("-")
    if "K" in li[0]:
        s1 =  li[0].replace("K","000")
        s2 =  li[1].replace("K","000")
    elif "k" in li[0]:
        s1 =  li[0].replace("k","000")
        s2 =  li[1].replace("k","000")
    return (eval(s1)+eval(s2))/2

#导入数据
f = open('lagou深圳.csv',encoding='utf-8')
lagou_data = pd.read_csv(f)
f.close()

#取salary值作为直方图绘图数据
data = lagou_data['salary'].apply(salary)
#取finance_stage作为饼图数据
data1 = lagou_data['finance_stage'].value_counts()

#薪资直方图
fig1 = plt.figure()
plt.hist(data[data<30000],bins=20,edgecolor='black')
plt.xlabel("区间")
plt.title("公司薪资水平直方图")

#公司融资阶段饼图
fig2 = plt.figure(figsize=(6,6))
explode = [0,0,0,0,0,0,0,0.1]
plt.title('公司融资阶段')
plt.pie(data1,labels=data1.index,
        explode=explode,
        autopct='%1.1f%%',
        startangle=90)
#设置横轴纵轴相等
plt.axis('equal')
