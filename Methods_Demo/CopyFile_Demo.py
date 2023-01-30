import os
import shutil


class CpFile_A2B(object):
    """用path_A的文件和标签 Copy并替换 到path_B的同名文件"""
    def __init__(self, path_A, path_B):
        self.path_A = path_A    # 源路径，包含文件和标签
        self.path_B = path_B        # 人工筛选的路径
        self.list_A = os.listdir(path_A)    # 以list读取path_A文件夹下-所有文件
        self.list_B = os.listdir(path_B)        # 人工筛选的路径

        print(self.list_A, self.list_B)

    def Cp_Replace(self):
        for img in self.list_B:
            name = os.path.splitext(img)[0]
            if img in self.list_A:
                src = self.path_A+img
                dst = self.path_B + img
                dst_lab = self.path_B + name + '.xml'
                shutil.copyfile(src, dst)  # 将src复制到dst
                shutil.copyfile(src, dst_lab)  # 将src复制到dst

            else:
                raise EOFError


if __name__ == '__main__':
    pass
    CpFile_A2B(path_A='../DataLoad/dataTest/', path_B='../DataLoad/GroziImg/').Cp_Replace()
