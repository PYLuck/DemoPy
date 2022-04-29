import xlrd             # pip3 install xlrd==1.2.0
from xlrd import open_workbook

import os
import torch
import numpy as np
from pathlib import Path
from torch.utils.data import Dataset
import random
from tqdm import tqdm

book = open_workbook(r'G:\DeepLearn\DemoPy\DataLoad\BreathHeart\SY\Breathdata(SY).xlsx')
sheet = book.sheets()[0]
arr = np.array([x.value for x in sheet.col(1,start_rowx=1)])

import pandas as pd
a=1
if a==0:
    def PandasDemo():
        # 1：读取指定行
        print("----读取指定的单行，数据会存在列表里面----")
        df = pd.read_excel('测试.xlsx')  # 这个会直接默认读取到这个Excel的第一个表单
        data = df.loc[0].values  # 0表示第一行 这里读取数据并不包含表头，要注意哦！
        print("读取指定行的数据：\n{0}".format(data))

        print("\n------读取指定的多行，数据会存在嵌套的列表里面----------")
        df = pd.read_excel('测试.xlsx')
        data = df.loc[[1, 2]].values  # 读取指定多行的话，就要在loc[]里面嵌套列表指定行数:如[0,2] 0和2行的数据
        print("读取指定行的数据：\n{0}".format(data))

        print("\n----------------读取指定的行列-----------------------")
        df = pd.read_excel('测试.xlsx')
        data = df.iloc[1, 2]  # 读取第一行第二列的值，这里不需要嵌套列表
        print("读取指定行的数据：\n{0}".format(data))

        print("\n----------------读取指定的多行多列值-----------------------")
        df = pd.read_excel('测试.xlsx')
        data = df.loc[[1, 2], ['title', 'data']].values  # 读取第一行第二行的title以及data列的值，这里需要嵌套列表
        print("读取指定行的数据：\n{0}".format(data))

        print("\n-----------获取所有行的指定列----------------------------")
        df = pd.read_excel('测试.xlsx')
        data = df.loc[:, ['title', 'data']].values  # 读所有行的title以及data列的值，这里需要嵌套列表
        print("读取指定行的数据：\n{0}".format(data))

    print("\n------------获取行号并打印输出---------------------------")
    df = pd.read_excel('测试.xlsx')
    print("输出行号列表", df.index.values)

    print("\n-------------获取列名并打印输出--------------------------")
    df = pd.read_excel('测试.xlsx')
    print("输出列标题", df.columns.values)

    print("\n------------获取指定行数的值---------------------------")
    df = pd.read_excel('测试.xlsx')

    print("输出值", df.sample(3).values)  # 这个方法类似于head()方法以及df.values方法
    print("\n-----------获取指定列的值----------------------------")
    df = pd.read_excel('测试.xlsx')
    print("输出值\n", df['data'].values)
else:


    print("\n------读取指定的多行，数据会存在嵌套的列表里面----------")

    if 'Breath0'.startswith('Breath'):
        print("J")


    df = pd.read_excel('G:\DeepLearn\DemoPy\DataLoad\测试.xlsx')
    data = df.loc[[i for i in range(0, 4)]].values  # 读取指定多行的话，就要在loc[]里面嵌套列表指定行数
    print("读取指定行的数据：\n",data)
    a_data = np.delete(data,obj=0,axis=1)
    nrows = a_data.shape[0]  # 行数
    ncols = a_data.shape[1]  # 列数
    print("测试")
    for i in range(nrows):
        half = a_data[i,0:3]



import random
import time

r4 = random.sample(range(1, 100), 40)

start_time = time.time()
for _ in range(100000):
    a = []
    a.append(3.5)
    a.append(5.1)

    a.extend(r4)
    b = np.asarray(a, dtype=np.float32)




