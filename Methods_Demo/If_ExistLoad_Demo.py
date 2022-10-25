# 判断文件\某个变量\Val是否存在，存在则加载文件，不存在则写入文件并保存
"""
assert + 空格 + 要判断语句，“报错语句”
3种方式：
"""
import os
import numpy as np
import torch


try:
    assert os.path.exists('None')
except:
    a = 1000000
    print(a)

