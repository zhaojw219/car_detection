# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2 as cv
import numpy as np

#读取图片位置
original = cv.imread("/media/gnss/系统/seg_competation/rssrai2019_semantic_segmentation/1_new.tif",-1)

# original = cv.imread('/media/gnss/系统/seg_competation/rssrai2019_semantic_segmentation/train/train/GF2_PMS1__20150212_L1A0000647768-MSS1 (2).tif')

# cv.imshow('Original', original)

blue = np.zeros_like(original)
blue[..., 0] = original[..., 0]

if blue[1][1] ==25:
	print('345')
print(blue)
print(blue.shape)

cv.imshow('blue', blue)

green = np.zeros_like(original)
green[..., 1] = original[..., 1]
cv.imshow('green', green)

red = np.zeros_like(original)
red[..., 2] = original[..., 2]
cv.imshow('red', red)

nir = np.zeros_like(original)
red[..., 3] = original[..., 3]
cv.imshow('nir', nir)

cv.waitKey()
#图片写入
# cv.imwrite('C:/Users/Administrator/Desktop/spider/hua_red.jpg', red)
