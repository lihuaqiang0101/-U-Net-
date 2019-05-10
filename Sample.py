import SimpleITK as sitk
import matplotlib.image as implt
import numpy as np
import os
from greymatrix import test

class Sample:
    def __init__(self):
        # 定义一个数据集，用于存放训练样本和标签
        """
        获取训练样本
        """
        self.images = os.listdir('train/image') # 遍历每一个数据
        self.images.sort(key=lambda x:int(x.split('.')[0]))
        self.GTs = os.listdir('train/GT')
        self.GTs.sort(key=lambda x: int(x.split('.')[0]))

    def get_batch(self, n):
        xs = []  # 用于存放拿到的随机样本
        ys = []  # 用于存放拿到的随机样本的标签
        for i in range(n):
            index = np.random.randint(0, len(self.images))  # 生成用于随机抽取样本的索引
            ds = sitk.ReadImage('train/image/{}'.format(self.images[index]))
            img_array = sitk.GetArrayFromImage(ds)
            xs.append(img_array)
            y = implt.imread(os.path.join('train/GT', self.GTs[index]))
            ys.append(y)
        return xs, ys

class tsample:
    def __init__(self):
        pass
    def get_batch(self,n):
        images = os.listdir('tumour')
        xs = []  # 用于存放拿到的随机样本
        ys = []  # 用于存放拿到的随机样本的标签
        for i in range(n):
            index = np.random.randint(0, len(images))  # 生成用于随机抽取样本的索引
            x = test(os.path.join('tumour', images[index]))
            xs.append(x)
            y = int(images[index][0])
            ys.append(y)
        return xs, ys
class sample:
    def __init__(self):
        pass
    def get_batch(self,n):
        images = os.listdir('tumour')
        xs = []  # 用于存放拿到的随机样本
        ys = []  # 用于存放拿到的随机样本的标签
        for i in range(n):
            index = np.random.randint(0, len(images))  # 生成用于随机抽取样本的索引
            x = implt.imread(os.path.join('tumour', images[index]))
            xs.append(x)
            y = int(images[index][0])
            ys.append(y)
        return xs, ys
# s = sample()
# x,y = s.get_batch(10)
# x = np.array(x)
# y = np.array(y)
# x = np.reshape(x,[10,1,512,512])
# print(x.shape,y)
