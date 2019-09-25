# -*- coding: utf8 -*-
import cv2

# 读取图像
img_head = cv2.imread('C:/Users/01181249/Desktop/pic0.jpg')
img_lower = cv2.imread('C:/Users/01181249/Desktop/pic1.jpg')
# 获取图像宽度
w_head, h_head = img_head.shape[:2]
w_lower, h_lower = img_lower.shape[:2]
# 计算缩放比例并缩放
scale = w_head / w_lower / 4
img_lower = cv2.resize(img_lower, (0, 0), fx=scale, fy=scale)
# 获取缩放后新宽度
w_lower, h_lower = img_lower.shape[:2]
# 合并图片
for c in range(0, 3):
    img_head[w_head - w_lower:, h_head - h_lower:, c] = img_lower[:, :, c]

cv2.imwrite('C:/Users/01181249/Desktop/new_pic.jpg', img_head)
