import cv2
import math
import os
import numpy as np

# 定义最大灰度级数
gray_level = 16


def maxGrayLevel(img):
    max_gray_level = 0
    (height, width) = img.shape
    for y in range(height):
        for x in range(width):
            if img[y][x] > max_gray_level:
                max_gray_level = img[y][x]
    return max_gray_level + 1


def getGlcm(input, d_x, d_y):
    srcdata = input.copy()#将原始的灰度图拷贝一份
    ret = [[0.0 for i in range(gray_level)] for j in range(gray_level)]#生成16x16的全零矩阵
    (height, width) = input.shape

    max_gray_level = maxGrayLevel(input)#获取当前图片的最大灰度值

    # 若灰度级数大于gray_level，则将图像的灰度级缩小至gray_level，减小灰度共生矩阵的大小
    if max_gray_level > gray_level:
        for j in range(height):
            for i in range(width):
                srcdata[j][i] = srcdata[j][i] * gray_level / max_gray_level

    for j in range(height - d_y):
        for i in range(width - d_x):
            rows = srcdata[j][i]
            cols = srcdata[j + d_y][i + d_x]
            ret[rows][cols] += 1.0

    for i in range(gray_level):
        for j in range(gray_level):
            ret[i][j] /= float(height * width)

    return ret


def feature_computer(p):
    Con = 0.0
    Eng = 0.0
    Asm = 0.0
    Idm = 0.0
    for i in range(gray_level):
        for j in range(gray_level):
            Con += (i - j) * (i - j) * p[i][j]
            Asm += p[i][j] * p[i][j]
            Idm += p[i][j] / (1 + (i - j) * (i - j))
            if p[i][j] > 0.0:
                Eng += p[i][j] * math.log(p[i][j])
    return Asm, Con, -Eng, Idm


def test(image_name):
    img = cv2.imread(image_name)
    try:
        img_shape = img.shape
    except:
        print('imread error')
        return

    img = cv2.resize(img, (img_shape[1] // 2, img_shape[0] // 2), interpolation=cv2.INTER_CUBIC)#将原始图片缩放为原来大小的一半

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#将原始图像转换为灰度图

    glcm_0 = getGlcm(img_gray, 1, 0)#统计整福图像在角度为0，步距为1上的每一种灰度值组合出现的概率矩阵P

    asm, con, eng, idm = feature_computer(glcm_0)#获取角二阶矩，熵，对比度，反差分矩阵作为纹理分类特征

    return [asm, con, eng, idm]


def get_batch(n):
    data = os.listdir('ying')
    r = []
    for a in A:
        result = test('ying/{}'.format(a))
        r.append(result)
    r = np.array(r)
    # result = np.reshape(result,(1,4))
    print(r,type(r),r.shape)
    # print('*'*30)
    # B = os.listdir('b')
    # for b in B:
    #     result = test('b/{}'.format(b))
    #     print(result)
