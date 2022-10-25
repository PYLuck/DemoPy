# tensorflow1.4实现conv2d()运算；numpy创建张量
"""
兼容性问题:
import tensorflow.compat.v1 as tf
"""

import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print(tf.test.is_gpu_available())


# 通过 numpy 构建输入张量
input_data = [i + 1 for i in range(9)]
input_data = np.asarray(input_data)
input_data = input_data.reshape(1, 3, 3, 1)

input_tensor = tf.constant(input_data, dtype=tf.float32)        # tf创建常量
print("input_tensor",input_tensor.shape)       # <tf.Tensor 'Const_1:0' shape=(1, 3, 3, 1) dtype=float32>

# 通过 numpy 构建卷积核
filter_data = [i + 1 for i in range(4)]
filter_data = np.asarray(filter_data).reshape(2, 2, 1, 1)
filter_data = filter_data.astype(np.float32)

filter_tensor = tf.constant(filter_data, dtype=tf.float32)      # <tf.Tensor 'Const_3:0' shape=(2, 2, 1, 1) dtype=float32>

# 使用 TensorFlow 中的二维卷积操作
output_tensor = tf.nn.conv2d(input=input_tensor, filter=filter_tensor, strides=[1, 1, 1, 1], padding="VALID")
print("output_tensor",output_tensor.shape)      # <tf.Tensor 'Conv2D:0' shape=(1, 2, 2, 1) dtype=float32>

# 初始化所有的变量
init_op = tf.compat.v1.global_variables_initializer()

# 通过会话（Session）来运行默认图中的相关计算操作
# 为查看结果必须创建一个会话，并用取值函数eval()来查看创建的tensor的值：
with tf.compat.v1.Session() as sess:
    sess.run(init_op)
    result = sess.run(output_tensor)
    print('结果是：', output_tensor.eval())



print("Result",result.shape)         # Tensor("Shape:0", shape=(4,), dtype=int32)


