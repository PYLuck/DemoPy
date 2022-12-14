# opencv-python==4.6.0      常用库函数
import cv2
print(cv2.__version__)          # 4.6.0

import numpy as np
img = np.ones((256, 360), dtype=np.uint8)
sum = 0
for x in range(256):
    for y in range(360):
        img[x, y] = 255/(1024*720) * sum
        sum += 1
cv2.imshow('img', img)
cv2.waitKey(5000)           # 显示保持



if __name__ == '__main__':
    pass
