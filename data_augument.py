import cv2 as cv
import numpy as np

img = cv.imread("/media/gnss/系统/seg_competation/data/cropimg.tif",-1)

# x,y,xy轴对称翻转   
# cv.flip >0:沿x轴翻转 <0:x,y轴同时翻转 =0:沿y轴翻转
dst1 = cv.flip(img, 0, dst=None)
dst2 = cv.flip(img, 1, dst=None)
dst3 = cv.flip(img, -1, dst=None)
cv.imwrite('/media/gnss/系统/seg_competation/data/data_augment/_flip_x.tif',dst1)
cv.imwrite('/media/gnss/系统/seg_competation/data/data_augment/_flip_y.tif',dst2)
cv.imwrite('/media/gnss/系统/seg_competation/data/data_augment/_flip_x_y.tif',dst3)

# 高斯噪声
dst4 = cv.GaussianBlur(img, (5, 5), 0)
dst5 = cv.GaussianBlur(dst1, (5, 5), 0)
dst6 = cv.GaussianBlur(dst2, (5, 5), 0)
dst7 = cv.GaussianBlur(dst3, (5, 5), 0)
cv.imwrite('/media/gnss/系统/seg_competation/data/data_augment/guassian.tif', dst4)
cv.imwrite('/media/gnss/系统/seg_competation/data/data_augment/guassian_flip_x.tif', dst5)
cv.imwrite('/media/gnss/系统/seg_competation/data/data_augment/guassian_flip_y.tif', dst6)
cv.imwrite('/media/gnss/系统/seg_competation/data/data_augment/guassian_flip_x_y.tif', dst7)

# 亮暗
reduce = 0.5
increase = 1.4
# brightness
g = 10
h, w, ch = img.shape
add = np.zeros([h, w, ch], img.dtype)
dst8 = cv.addWeighted(img, reduce, add, 1-reduce, g)
dst9 = cv.addWeighted(dst1, increase, add, 1-increase, g)
dst10 = cv.addWeighted(img, reduce, add, 1 - reduce, g)
dst11 = cv.addWeighted(dst1, increase, add, 1 - increase, g)
cv.imwrite('/media/gnss/系统/seg_competation/data/data_augment/_ReduceEp.tif', dst8)
cv.imwrite('/media/gnss/系统/seg_competation/data/data_augment/_ReduceEp_flip_x.tif', dst9)
cv.imwrite('/media/gnss/系统/seg_competation/data/data_augment/_IncreaseEp.tif', dst10)
cv.imwrite('/media/gnss/系统/seg_competation/data/data_augment/_IncreaseEp_flip_x.tif', dst11)

