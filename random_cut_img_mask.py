import cv2
import os
import sys
import time

def cut_img(img_paths,output_dir):
    scale = len(img_paths)
    for i,img_path in enumerate(img_paths):
        a = "#"* int(i/1000)
        b = "."*(int(scale/1000)-int(i/1000))
        c = (i/scale)*100
        time.sleep(0.2)
        print('正在处理图像： %s' % img_path.split('/')[-1])
        img = cv2.imread(img_path)
        weight = img.shape[1]
        if weight>1600:                         
            cropImg = img[50:200, 700:1500]    # 裁剪【行数据范围：列数据范围】
            #cropImg = cv2.resize(cropImg, None, fx=0.5, fy=0.5,
                                 #interpolation=cv2.INTER_CUBIC) #缩小图像
            cv2.imwrite(output_dir + '/' + img_path.split('/')[-1], cropImg)
        else:                                        
            cropImg_01 = img[30:150, 50:600]
            cv2.imwrite(output_dir + '/'+img_path.split('/')[-1], cropImg_01)
        print('{:^3.3f}%[{}>>{}]'.format(c,a,b))

if __name__ == '__main__':
    img_path = "./src/1.tif"
    img = cv2.imread(img_path,-1)
    mask_path = "./label/1.tif"
    # mask = cv2.imread(mask_path,-1)
    # mask = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    mask = cv2.imread(mask_path,-1)
    output_dir = "./seg_competation/data" # 保存截取的图像目录

    Xlenth = img.shape[1]  # 图片列数 7200
    Ylenth = img.shape[0]  # 图片行数 6800
    
    print(img.shape)
    print(mask.shape)
     
    cropimg = img[500:1500, 500:1500]
    cropmask = mask[500:1500, 500:1500]
    cv2.imwrite('./data/cropimg.tif', cropimg)
    cv2.imwrite('./data/cropmask.tif', cropmask)

    print('图片获取完成 。。。！')
    # cut_img(img_paths,output_dir)
