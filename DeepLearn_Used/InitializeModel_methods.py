# coding=utf-8
"""
模型初始化-加载权重方法：
1、pytorch中利用self.module()方法来初始化模型权重
2、先初始化，再加载权重
"""
import torch.nn as nn

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
                # 手动初始化权重,使用 m.weight.data.tensor方法() e.g. m.weight.data.zero_()、normal_()
                nn.init.kaiming_normal_(m.weight)           # 使用正态分布对输入张量(Conv2d.weight)赋值      print(m.weight)
            elif isinstance(m, nn.BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()

        # self.modules 深度优先遍历：
        for i, j in enumerate(self.modules()):
            print(i, "->:", j)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn(x)
        return self.relu(x)


if __name__ == '__main__':
    net1 = Network()
