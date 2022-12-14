import torch
import torch.nn as nn

import torch.nn.functional as F


class FocalLoss(nn.Module):
    """用于不平衡数据集和难易样本的学习"""
    def __init__(self, weight=None, reduction='mean', gamma=0, eps=1e-7):
        super(FocalLoss, self).__init__()
        self.gamma = gamma
        self.eps = eps
        self.ce = nn.CrossEntropyLoss(weight=weight, reduction=reduction)   # weight用于样本均衡处理，给每一类样本一个权值

    def forward(self, input, target):
        logp = self.ce(input, target)
        p = torch.exp(-logp)
        loss = (1 - p) ** self.gamma * logp
        return loss.mean()

def L1Loss():
    loss = nn.L1Loss()
    input = torch.randn(3, 5, requires_grad=True)
    target = torch.randn(3, 5)
    output = loss(input, target)
    output.backward()

def MSELoss():
    loss = nn.MSELoss()
    input = torch.randn(3, 5, requires_grad=True)
    target = torch.randn(3, 5)
    output = loss(input, target)
    output.backward()

def CrossEntropy():
    """nn.LogSoftmax()+nn.NLLLoss()"""
    loss = nn.CrossEntropyLoss()
    input = torch.randn(3, 5, requires_grad=True)
    target = torch.empty(3, dtype=torch.long).random_(5)
    output = loss(input, target)
    output.backward()

def KLDivLoss():
    loss = nn.KLDivLoss()
    log_input = torch.randn(5, 2, requires_grad=True)
    target = torch.randn(5, 2)

    m = nn.LogSoftmax()
    output = loss(m(log_input), target.softmax(dim=-1))
    output.backward()

    kl = F.kl_div(log_input.softmax(dim=-1).log(), target.softmax(dim=-1))  # 判断nn和F下计算结果是否相同
    print(kl.item() == output.item())


if __name__ == '__main__':
    print('Loss-')