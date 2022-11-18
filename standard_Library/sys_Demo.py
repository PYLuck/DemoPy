# sys 基础库：sys模块是与python解释器交互的一个接口。sys 模块提供了许多函数和变量来处理 Python 运行时环境的不同部分。
import sys

"""
sys.argv[0] 表示程序自身
sys.argv[1] 表示程序的第一个参数
sys.argv[2] 表示程序的第二个参数
"""

print(sys.path[0])
print(sys.argv[0])
print(__file__)