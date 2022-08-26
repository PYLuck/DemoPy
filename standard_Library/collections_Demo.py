# collections Python标准库：namedtuple、deque、defaultdict、Couter
# 参考：https://blog.csdn.net/qq_41007998/article/details/120953231
import collections
'''
Abstract: 包含4个usage
1、函数 = defaultdict(函数)                                      # 当读取dict不存在的属性时，会返回默认值
2、含有列表的类 = namedtuple(列表名称，列表)                          # 创建一个可以使用属性名称而不是索引获取值的元组
3、列表 = deque(列表)                                              # 解决 频繁删除插入带来的效率问题
4、字典的Counter类_iteration = collections.Counter('字符串')        # 计数
'''

# 1、
d1 = {"one":1,"two":2,"three":3}
print("four")
#上面的会报错，下面的就会返回函数，告诉我们错了
func = lambda: "错了"
d2 = collections.defaultdict(func)
d2['one']= 1
d2['two']= 2
print(d2['four'])

score = collections.defaultdict(list)
print(score)

# 2、
# help(collections.namedtuple)
Point = collections.namedtuple("Point",['x','y'])
p = Point(15,45)
print(p.x+p.y)
print(p[0]+p[1])
#支持索引等
#应用举例
Circle = collections.namedtuple('Circle',['x','y','r'])
circle = Circle(14,15,45)
propotion = circle[2]*circle[2]*3.141596
print("圆的面积为",propotion)




# 3、
q = collections.deque(['a','b','c'])
print(q)
q.append('sada')
q.appendleft('left')
print(q)
help(collections.deque)


# 4、
list1 = collections.Counter("aaabbbccc")
print(list1)
list2 = collections.Counter(['abc','sad','sad','abc','abc','ffds'])
print(list2)

