import cv2
import numpy as np

if __name__ == "__main__":
    img_path = "./train/GF2_PMS2__20160510_L1A0001573999-MSS2_label.tif"
    img = cv2.imread(img_path,-1)

    img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    # cv2.imwrite('./train/gray_label.tif', img_gray)


    Xlenth = img.shape[1]  # 图片列数 7200
    Ylenth = img.shape[0]  # 图片行数 6800
    a = 1
    for i in range(Ylenth):
        for j in range(Xlenth):
            print(img_gray[i][j])
            if img[i][j][0]==0 and img[i][j][1]==200 and img[i][j][2]==0:
                img_gray[i][j]=10 # 水田

            elif img[i][j][0]==0 and img[i][j][1]==250 and img[i][j][2]==150:
                img_gray[i][j]=20 # 水浇地

            elif img[i][j][0]==150 and img[i][j][1]==200 and img[i][j][2]==150:
                img_gray[i][j]=30 # 旱耕地

            elif img[i][j][0]==200 and img[i][j][1]==0 and img[i][j][2]==200:
                img_gray[i][j]=40 # 园地

            elif img[i][j][0]==250 and img[i][j][1]==0 and img[i][j][2]==150:
                img_gray[i][j]=50 # 乔木林地

            elif img[i][j][0]==250 and img[i][j][1]==150 and img[i][j][2]==150:
                img_gray[i][j]=60 # 灌木林地

            elif img[i][j][0]==0 and img[i][j][1]==200 and img[i][j][2]==250:
                img_gray[i][j]=70 # 天然草地

            elif img[i][j][0]==0 and img[i][j][1]==200 and img[i][j][2]==200:
                img_gray[i][j]=80 # 人工草地

            elif img[i][j][0]==0 and img[i][j][1]==200 and img[i][j][2]==200:
                img_gray[i][j]=90 # 工业用地

            elif img[i][j][0]==150 and img[i][j][1]==0 and img[i][j][2]==250:
                img_gray[i][j]=100 # 城市住宅

            elif img[i][j][0]==150 and img[i][j][1]==150 and img[i][j][2]==200:
                img_gray[i][j]=110 # 村镇住宅

            elif img[i][j][0]==150 and img[i][j][1]==150 and img[i][j][2]==250:
                img_gray[i][j]=120 # 交通运输

            elif img[i][j][0]==200 and img[i][j][1]==0 and img[i][j][2]==0:
                img_gray[i][j]=130 # 河流

            elif img[i][j][0]==200 and img[i][j][1]==150 and img[i][j][2]==0:
                img_gray[i][j]=140 # 湖泊

            elif img[i][j][0]==250 and img[i][j][1]==200 and img[i][j][2]==0:
                img_gray[i][j]=150 # 坑塘

            elif img[i][j][0]==0 and img[i][j][1]==0 and img[i][j][2]==0:
                img_gray[i][j]=160 # 其他类别
            print(img_gray[i][j])
    cv2.imwrite('./gray_label8.tif', img_gray)
    # cv2.imshow("img_gray",img_gray)
    # cv2.waitKey()
