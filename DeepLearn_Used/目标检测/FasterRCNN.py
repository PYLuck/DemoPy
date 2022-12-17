# RCNN -> FastRCNN -> FasterRCNN 两阶段代表模型
"""
RCNN流程:
- 一张图生成1~2k个候选区域(use Selective Search算法通过图像分割、合并策略)
- resize bbox, 分类网络提取特征
- 特征向量 送入每个类别的2分类SVM分类器，判断类别
- 训练回归器 精细修正候选框

Fast RCNN:
- 一张图生成1~2k个候选区域(use Selective Search算法通过图像分割、合并策略)
[训练数据采样: 2k张图取正负样本]
- 图像输入网络生成Feature Map, 将候选框 投影 到特征图上, 形成候选区的FeatureMap
- 候选区FeatureMap 输入 RoI Pooling layer 缩放到7X7 -> Fc -> RoI特征向量(感兴趣区域)
- 分类器:并联两个Fc层, 预测N+1个类别(1个背景类)
  回归器: 输出N+1个(dx,dy,dw,dh)
- Loss = 分类损失CCE + 入 bbox回归损失(SmoothL1)             # L1=∑|(pre-rel)|/n
# https://www.cnblogs.com/wangguchangqing/p/12021638.html

Faster RCNN: (RPN+FastRCNN)
- Img -> VGG -> FeatureMap
- Use RPN(Region Proposal Net)生成候选bbox —投影到特征图-> 特征矩阵
- 特征矩阵 -> RoI pooling -> Fc -> bbox特征向量
- 分类+回归

训练:
backbone + RPN Loss + FastRCNN Loss 联合训练
1、训练backbone + RPN, 用训练好的结构生成bbox
2、用生成的bbox训练backbone + FastRCNN(RoI+Fc..),用训练好的结构微调RPN部分



"""


if __name__ == '__main__':
    pass