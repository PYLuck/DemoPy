import torch
from torchvision import models
from torch import nn

print(dir(models))
model = getattr(models, 'resnet18')()  # 获取属性值
my = nn.Sequential(*list(model.children())[:-3])
# print(my)
# print(model)

name = "zhs"
# print(dir(name).__class__)


pred = torch.tensor([[-0.5816, -0.3873, 44, -1.0145, 0.4053],
                     [0.7265, 1.4164, 1.3443, 1.2035, 55],
                     [66, 0.1673, 1.2590, -2.0757, 1.7255],
                     [0.2021, 0.3041, 0.1383, 0.3849, 99]])

values, indices = torch.topk(pred, 3)
# print(values)
# print(indices)


# ========================updata==================================
"""Pytorch中的model.modules()和model.children()的区别"""

a = torch.randn([128, 3, 224, 224])
# print(a.shape)
# print(a[0:-1:2].shape)

#
m = nn.Linear(256, 66)
input = torch.randn(128, 256)
output1 = m(input)
# print(output1.size())  # [(128--40])


# ================pytorch 优化器(optim)不同参数组，不同学习率 策略===================
'''   
optimizer = torch.optim.SGD([
            {'params': other_params}, 
            {'params': first_params, 'lr': 0.01*args.learning_rate},
            {'params': second_params, 'weight_decay': args.weight_decay}],
            lr=args.learning_rate,
            momentum=args.momentum,)
'''

import numpy as np

# print(np.random.random_sample())

# 查看当前目录已使用总大小可输入：du -h --max-depth=0


import torch

l1 = torch.tensor(1.5644)
print(l1)
l2 = torch.tensor(3.1524564)
s = torch.stack([l1, l2])
print(s)
print(torch.sum(s))

nu = [lambda x1: x1 * 0.001, lambda x: x + 2000, lambda y: y ** 2]
print(nu[0])
# print(nu[1](10000))
out = [n(3) for n in nu]
print(out)

logi = []
for n in nu:
    oin = n(3)
    logi.append(oin)
print(logi)
