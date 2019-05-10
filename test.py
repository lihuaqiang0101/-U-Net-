import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torch.autograd import Variable
from Sample import tsample
import numpy as np
from evaluation import get_F1
import os
from greymatrix import test

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.linear1 = nn.Linear(4,512)
        self.linear2 = nn.Linear(512,256)
        self.linear3 = nn.Linear(256,128)
        self.linear4 = nn.Linear(128,64)
        self.linear5 = nn.Sequential(nn.Linear(64,1),
                                     nn.Sigmoid())
    def forward(self,x):
        x = F.relu(self.linear1(x))
        x = F.relu(self.linear2(x))
        x = F.relu(self.linear3(x))
        x = F.relu(self.linear4(x))
        return self.linear5(x)


def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return sorted(result.items(), key=lambda k: k[1],reverse=True)[0][0]

if __name__ == '__main__':
    f1 = open('a样本阴阳性预测.txt','w')
    f2 = open('v样本阴阳性预测.txt', 'w')
    net3 = Net()
    net3.load_state_dict(torch.load('net_params.pkl'))
    datasets = os.listdir('/home/lhq/桌面/B 题：直肠癌淋巴结转移的智能诊断/B题-测试数据/数据集3')
    datasets.sort(key=lambda x:int(x))
    for dataset in datasets:
        dirs = os.listdir('/home/lhq/桌面/B 题：直肠癌淋巴结转移的智能诊断/B题-测试数据/数据集3/'+dataset)
        for dir in dirs:
            if dir == 'arterial phase':
                lable1 = []
                for img in os.listdir('/home/lhq/桌面/B 题：直肠癌淋巴结转移的智能诊断/B题-测试数据/数据集3/' + dataset + '/' + dir):
                    x = test('/home/lhq/桌面/B 题：直肠癌淋巴结转移的智能诊断/B题-测试数据/数据集3/' + dataset + '/' + dir + '/' + img)
                    x = np.array(x)
                    x = torch.Tensor(x)
                    x = Variable(x)
                    out = net3(x)
                    out = out.detach().numpy()
                    out[out < 1] = 0
                    lable1.append(int(out[0]))
                f1.write(dataset)
                f1.write(':')
                if all_list(lable) == 0:
                    print('-')
                    f1.write('-')
                elif all_list(lable) == 1:
                    print('+')
                    f1.write('+')
                f1.write('\n')
            else:
                lable = []
                for img in os.listdir('/home/lhq/桌面/B 题：直肠癌淋巴结转移的智能诊断/B题-测试数据/数据集3/' + dataset + '/' + dir):
                    x = test('/home/lhq/桌面/B 题：直肠癌淋巴结转移的智能诊断/B题-测试数据/数据集3/' + dataset + '/' + dir + '/' + img)
                    x = np.array(x)
                    x = torch.Tensor(x)
                    x = Variable(x)
                    out = net3(x)
                    out = out.detach().numpy()
                    out[out < 1] = 0
                    lable.append(int(out[0]))
                f2.write(dataset)
                f2.write(':')
                if all_list(lable) == 0:
                    print('-')
                    f2.write('-')
                elif all_list(lable) == 1:
                    print('+')
                    f2.write('+')
                f2.write('\n')

    f1.close()
    f2.close()
