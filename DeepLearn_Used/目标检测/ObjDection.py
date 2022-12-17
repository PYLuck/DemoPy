# 常用目标检测算法相关
"""
目标检测的算法，通常都是对图片上的四个参数做处理：分别是中心点x轴、y轴坐标，框的高和宽
如Yolo和SSD，主要思路是均匀地在图片的不同位置进行密集抽样，抽样时可以采用不同尺度和长宽比，
然后利用CNN提取特征后直接进行分类与回归

# Two stage目标检测
先进行区域生成（region proposal,RP）(一个可能包含待检测物体的预选框)，再通过卷积神经网络进行样本分类。
任务：特征提取->生成RP->分类/定位回归。
常见Two stage目标检测算法有:R-CNN、SPP-Net、Fast R-CNN和R-FCN等。
# One stage 目标检测
不用RP，直接在网络中提取特征来预测物体分类和位置。
任务：特征提取->分类/定位回归。
常见的one stage目标检测算法有：OverFeat、YOLOv1、YOLOv3、SSD和RetinaNet等。
# https://github.com/tensorflow/models
"""

# 目标检测相关
def indicators():
    """
    # bounding box: (x_{min},y_{min},x_{max},y_{max})  |  (c_x,c_y,w,h)，中心点+宽高
    # IOU:判断检测框好坏--(frac{A{cap}B}{A{cup}B})交集除以并集
    # 设定NMS(非极大值抑制)：找到最佳的目标边界框（max IoU），消除周围多余的边界框

    # mAP
    TP: IoU>0.5的Num(bbox);    FP: IoU<=0.5;
    FN: 漏检的bbox数量;
    Precision: TP/(TP+FP)   查准率-预测的所有box中正确的比例
    Recall: TP/(TP+FN)      查全率-所有真实box中正确的比例
    AP: Precision-Recall曲线下的面积
    mAP: 各类别AP的平均值



    # 基础网络： 特征提取的基础架构，VGG、ResNet、DenseNet等

    # 先验框（prior box）
    # 置信度： 模型表达自己框出了物体的概率程度。假设网络要预测m类物体，那么实际网络会预测出m+1类，一般第一列就是置信度
    # 模型输出：预测box, 预测种类




    """
    return


def loss():
    """
    # Loss
    Loss = 位置回归损失(smooth L1 loss)和分类损失(CE)的加权和。
    L1 Loss、Smooth L1 Loss、IOU Loss
    如 YoloV5的三种损失函数：Loss = 分类损失(BCE)+定位损失(GIoU)+置信度损失(BCE)

    """

    return


def datasets():
    """
    数据集: pascal voc   |   coco
    Usage: import pycocotools

    [VOC]:
    例 AP@[ IoU=0.50 | area= all | maxDets=100 ] = 0.807

    [COCO]:
    例 AP@[ IoU=0.50:0.95 | area= all | maxDets=100 ] = 0.526

    - AP:
    AP@.50:.05:.95  (IoU=0.5~0.95,间隔0.05的均值,即mAP)
    AP@IoU=.50
    AP@IoU=.75
    - AP Across Scales:
    AP@area=all
    AP@area=small    (目标像素面积<32^2 的小目标的AP, 关注检测目标较小的指标)
    AP@area=medium   (32^2~96^2)
    AP@area=large    (>96^2)

    - AR (平均Recall)
    AR@maxDets=1    (最多检测1个bbox/per img)
    AR@maxDets=10    (最多检测10个bbox/per img)
    AR@maxDets=100    (最多检测100个bbox/per img)

    """
    return
#




# One-Stage: Yolo、SSD
'''
基于anchors直接分类及调整边界      | 速度快

SSD采用VGG16作为基础模型
'''



# Two-Stage: Faster-RCNN
'''
1) 专门模块生成RPN(候选框)、寻找前景及调整边界(基于anchors)
2) 基于RPN进行分类及调整边界框(基于proposals)                     | 检测更准确
'''