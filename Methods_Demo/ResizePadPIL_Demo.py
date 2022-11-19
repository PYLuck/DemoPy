'''PIL读取图片,resize等'''
import os
from PIL import Image
import math
from torchvision import transforms

'''
io.imread, cv2.imread                                               # 读取的图片是ndarray
PIL.Image.open(image_path)
AImage = Image.new('RGB', (224, 224), color=(255, 255, 255))        # 生成图片        

PILimg.resize(w, h)
transforms.Resize([h, w])           # * PIL.Image对象size属性返回的是w, h，而resize的参数顺序是h, w
transforms.Resize(x)        # 将图片短边缩放至x，长宽比保持不变
'''


def resize_pad(image, target_size):
    w,h = image.size
    minx = min(w,h)
    if minx == h:
        # w可以缩放到224, h进行padding
        new_h = int(h * (target_size/w))
        # image = image.resize((target_size, new_h), Image.Resampling.BICUBIC)
        image = image.resize((target_size, new_h), Image.BICUBIC)
        # 生成一张targe_size大小的图
        aimage = Image.new('RGB', (target_size, target_size), (127, 127, 127))
        # 计算上面需要贴的大小
        psize_up = (target_size - new_h)//2
        # 将缩放后的图像贴上去
        aimage.paste(image, (0, psize_up))
        aimage.show()
        tensor_img = transforms.ToTensor()(aimage).unsqueeze(0)
        print(tensor_img.shape)
    else:          # minx==w
        # h可以缩放到224, w进行padding
        new_w = int(w * (target_size/h))
        image = image.resize((new_w, target_size), Image.Resampling.BICUBIC)
        # 生成一张targe_size大小的图
        aimage = Image.new(mode='RGB', size=(target_size, target_size), color=(127, 127, 127))
        # 计算左边需要贴的大小
        psize_left = (target_size - new_w)//2
        # 将缩放后的图像贴上去
        aimage.paste(image,(psize_left,0))
        aimage.show()


if __name__ == '__main__':

    image_path = "/home/xk/图片/Im_test.jpeg"
    # 无失真缩放：resize_pad
    image = Image.open(image_path).convert('RGB')
    resize_pad(image, target_size=640)

    # 附 失真缩放
    # ori = image.resize((128, 128))
    # ori.show()

