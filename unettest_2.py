import torch
from torch.autograd import Variable
import numpy as np
import os
from greymatrix import test
from Unet import Unet
import matplotlib.pyplot as plt
from matplotlib import image
import cv2

def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return sorted(result.items(), key=lambda k: k[1],reverse=True)[0][0]

if __name__ == '__main__':
    net = Unet(1,1)
    net.load_state_dict(torch.load('unet_params.pkl'))
    datasets = os.listdir('/home/lhq/桌面/B 题：直肠癌淋巴结转移的智能诊断/B题-测试数据/数据集3')
    datasets.sort(key=lambda x:int(x))
    for dataset in datasets:
        dirs = os.listdir('/home/lhq/桌面/B 题：直肠癌淋巴结转移的智能诊断/B题-测试数据/数据集3/'+dataset)
        for dir in dirs:
            # if dir == 'arterial phase':
            lable = []
            for img in os.listdir('/home/lhq/桌面/B 题：直肠癌淋巴结转移的智能诊断/B题-测试数据/数据集3/' + dataset + '/' + dir):
                # if len(img) == 9:
                x = image.imread('/home/lhq/桌面/B 题：直肠癌淋巴结转移的智能诊断/B题-测试数据/数据集3/' + dataset + '/' + dir + '/' + img)
                x = torch.Tensor(x)
                x = Variable(x)
                x = x.view(-1, 1, 512, 512)
                out = net(x)
                out = out.detach().numpy()
                test_img = np.reshape(out, [512, 512])
                plt.imsave('/home/lhq/桌面/B 题：直肠癌淋巴结转移的智能诊断/B题-测试数据/数据集2/' + dataset + '/' + dir + '/' + '{}_mask.png'.format(img.split('.')[0]),test_img)
