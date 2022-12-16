# 常用的SVM核函数
from sklearn import svm
'''
SVM核函数:
RBF,
线性核函数，

'''

models = [svm.SVC(C, kernel='linear') for C in [1, 100]]
# 支持向量机模型 (kernel:核函数选项，这里是线性核函数 , C:权重，这里取1和100)
# 线性核函数画的决策边界就是直线
# Create SVM classification object
svm.SVC(C=1.0, kernel='rbf', degree=3, gamma='auto', coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape=None,random_state=None)

