# python 常用内置函数-汇总



# vars()返回对象object的 属性和属性值的 字典对
class obj: print(locals())
opt = obj()          # {'__module__': '__main__', '__qualname__': 'obj'}
opt.moss = "NAME"

print(vars(opt))     # {'moss': 'NAME'}
