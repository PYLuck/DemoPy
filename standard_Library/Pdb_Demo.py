# 代码调试工具：pdb pdb.set_trace()
import pdb
pdb.set_trace()
"""
参考：https://blog.csdn.net/weixin_44538273/article/details/88144977
"""

'''
步进：
n: 执行下一行，不会进入函数体
s: 执行下一行，会进入函数题内部
c: [continue]执行下一行，在函数中时会直接执行到函数返回处

步进到指定行
until [运行到125行]：until 125   


查看指令：
where(w) 找出当前代码运行位置
list(l) 显示当前代码的部分上下文
list <line number> 显示指定行的上下文
list <line number1, line number2> 显示指定开始行到结束行的代码



5. up(u) 返回上个调用点

6. down(d) 返回下个调用点

7. args(a) 显示当前所有变量

9 ! 运行python命令，比如!test='hello' 将会把test变量的值改变为hello

10. pp 打印美化过的表达式结果

11. step 步进运行至下行代码（如果是调用函数，则运行至所调用函数的第一行）

14. return 运行至return代码处

15. break <line number> 运行时设置断点

16. continue 运行程序直至遇到下一个断点

17. break <file name:line number> 运行时设置另一个文件的断点

18. break 显示断点情况

19. disable <break number> 将指定的断点失效（但存在）

20. enable <break number> 将指定的断点生效

21. clear <break number> 删除断点

22. tbreak <line number> 运行时设置临时断点（运行一次后自动删除）

23. break <line number> <condition> 运行时设置断点，当满足condition条件时触发断点，ex: break 11 i > 10 表示在第11行代码处，当变量i大于10时，触发断点

24. condition <break number> <condition> 设置指定断点的触发条件

25. ignore <break number> <n> 忽略指定断点n次

26. commands <break number> ... end 对指定断点编写脚本，当运行到该断点时自动执行
'''
try:
    e
except:
    print("YYY")



import torch

x = torch.randn(2375, 185)
indices = torch.tensor(3)
y = torch.index_select(x, -1, indices)
print(y.shape)

print()

'''如何删除断点并继续运行'''



