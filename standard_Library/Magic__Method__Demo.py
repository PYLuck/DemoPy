# python常用的魔法方法使用 __init__(), __setattr__(),
# 介绍详见 Manual Doc/Magic Methods.md

# Demo-1
class Tag:
    def __init__(self):
        self.change = {'python': 'This is python',
                       'php': 'PHP 是一门好语言'}

    def __getitem__(self, item):
        print('调用getitem, 获取')
        return self.change[item]

    def __setitem__(self, key, value):
        print('调用setitem, 修改')
        self.change[key] = value

# Demo-2
class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__  # dict.k  ==>  dict[k]
    # __getattr__ = dict.get  # dict.k  ==>  dict.get(k)
    # __getattr__ = lambda d, k: d.get(k, '')  # dict.k  ==>  dict.get(k,default)





if __name__ == '__main__':
    pass
    # ==================== Magic Method : __setattr__() ============================
    '''Demo-1: 获取与修改'''
    a = Tag()
    print(a['php'])
    a['php'] = 'PHP is not a good language'     # 传参的同时，调用 __getitem__(self, item)
    print(a['php'], 'Demo-1\n')

    '''Demo-2:实现字典转对象，即字典可以用dict.key获取 值'''
    D = Dict({'a': '123', 'b': 365})
    D.c = '233'
    print(D.c, 'Demo-2\n')

    # ==================================================================