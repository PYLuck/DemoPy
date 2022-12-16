# 常用目标检测算法
"""
# Two stage目标检测算法
先进行区域生成（region proposal,RP）(一个可能包含待检测物体的预选框)，再通过卷积神经网络进行样本分类。
任务：特征提取->生成RP->分类/定位回归。
常见Two stage目标检测算法有:R-CNN、SPP-Net、Fast R-CNN和R-FCN等。
# One stage 目标检测算法
不用RP，直接在网络中提取特征来预测物体分类和位置。
任务：特征提取->分类/定位回归。
常见的one stage目标检测算法有：OverFeat、YOLOv1、YOLOv3、SSD和RetinaNet等。
"""

# 目标检测相关
def concept():
    """
    # bounding box: (x_{min},y_{min},x_{max},y_{max})  |  (c_x,c_y,w,h)，中心点+宽高
    # IOU:判断检测框好坏--(frac{A{cap}B}{A{cup}B})交集除以并集
    # 基础网络： 特征提取的基础架构，VGG、ResNet、DenseNet等

    # 先验框（prior box）
    # 置信度： 模型表达自己框出了物体的概率程度。
    # NMS(非极大值抑制)：找到最佳的目标边界框，消除周围多余的边界框
    # 模型输出：预测box, 预测种类

    # Loss = 位置回归损失(smooth L1 loss)和分类损失( )的加权和。


    """
    return


'''
# 目标检测的算法，通常都是对图片上的四个参数做处理：分别是中心点x轴、y轴坐标，框的高和宽
如Yolo和SSD，其主要思路是均匀地在图片的不同位置进行密集抽样，抽样时可以采用不同尺度和长宽比，然后利用CNN提取特征后直接进行分类与回归

'''
# Yolo


# SSD
# SSD采用VGG16作为基础模型