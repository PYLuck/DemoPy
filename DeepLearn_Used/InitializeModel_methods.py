# coding=utf-8
"""
模型初始化-加载权重方法：
1、pytorch中利用self.module()方法来初始化模型权重
2、先初始化，再加载权重
参数初始化分为：固定值初始化、预训练初始化、随机初始化。
"""
import torch.nn as nn


# 常用随机初始化方法：
def Random_Initialize(m=nn.Conv2d(3, 1, kernel_size=3)):
    """
    param m: module of torch
    """
    # 高斯分布
    nn.init.normal_(m.weight, mean=0.0, std=1.0)  # → torch.Tensor
    # 均匀分布
    nn.init.uniform_(m.weight, a=0.0, b=1.0)  # → torch.Tensor
    # 常数分布
    nn.init.constant_(m.weight, val=float())  # → torch.Tensor
    # 全0分布
    nn.init.zeros_(m.weight)  # → torch.Tensor
    # 全1分布
    nn.init.ones_(m.weight)  # → torch.Tensor
    return

# Xavier初始化方法
def Weight_init_Xavier(m):
    """
    Xavier初始化： 不适用于sigmoid函数和ReLU函数
    m.weight.data：得到的是一个Tensor的张量（向量），不可训练的类型
    m.weight：得到的是一个parameter的变量，可以计算梯度的
    """
    classname = m.__class__.__name__
    if classname.find('Conv') != -1:
        nn.init.xavier_normal_(m.weight.data, gain=1.0)  # 正态分布 → torch.Tensor
    else:
        nn.init.xavier_uniform_(m.weight.data, gain=1.0)  # 均匀分布 → torch.Tensor
    return


# Usage:
class Network(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7)
        self.relu = nn.ReLU()
        self.conv2 = nn.Conv2d(64, 128, kernel_size=3)
        self.bn = nn.BatchNorm2d(128)
        self.lls = nn.Sequential(self.relu, nn.Linear(10, 10))

        # 在初始化网络时, 初始化网络中的每个module
        '''self.modules(), 以迭代器形式返回此前声明的所有layers'''
        for m in self.modules():  # 继承nn.Module的方法
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight)  # Kaiming初始化-使用正态分布对输入张量(Conv2d.weight)赋值      print(m.weight)
            elif isinstance(m, nn.BatchNorm2d):
                # 手动初始化权重,使用 m.weight.data.tensor方法()
                m.weight.data.fill_(1)
                m.bias.data.zero_()

        # self.modules 深度优先遍历 顺序：
        for i, j in enumerate(self.modules()):
            print(i, "->:", j)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn(x)
        return self.relu(x)


if __name__ == '__main__':
    net1 = Network()
    # model.apply(func): 会递归地将函数func应用到父模块net1的每个子模块submodule
    net1.apply(Weight_init_Xavier)
