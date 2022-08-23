# use numpy do 一些 操作[handle]:
import numpy as np
'''
[Abstract]
·遍历numpy数组的每一个元素：nditer(array, order='C')


'''

Array = np.arange(6);                                                   print(Array.shape)
# 行序优先order='C'，列'F'
new_array = [i for i in np.nditer(op=Array, order='C')];                print(Array == new_array)
