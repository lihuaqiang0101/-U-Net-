from Unet import Unet
from Sample import Sample
import evaluation
import torch
from torch import nn
from torch import optim
from torch.autograd import Variable
import numpy as np
import cv2
import matplotlib.pyplot as plt
import random
from torch.backends import cudnn

def adjust_learning_rate(optimizer,lr):
    """Sets the learning rate to the initial LR decayed by 10 every 30 epochs"""
    lr -= lr/40000
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr

if __name__ == '__main__':
    cudnn.benchmark = True
    unet = Unet(1,1)
    sample = Sample()
    if torch.cuda.is_available():
        unet = unet.cuda()
    criterion = nn.BCELoss()
    # optimizer = optim.RMSprop(unet.parameters(),lr=0.001)
    lr = random.random() * 0.0005 + 0.0000005
    optimizer = optim.Adam(unet.parameters(), lr=lr,betas=(0.9,0.999))
    cout1 = 0
    cout2 = 0
    cout3 = 0
    dice = 0
    for epoch in range(50000):
        while True:
            try:
                imgs,gts = sample.get_batch(4)
                break
            except:
                pass
        imgs = np.array(imgs)
        gts = np.array(gts)
        gts = np.expand_dims(gts,axis=1)
        imgs = torch.Tensor(imgs)
        gts = torch.Tensor(gts)
        if torch.cuda.is_available():
            imgs = imgs.cuda()
            gts = gts.cuda()
        else:
            imgs = Variable(imgs)
            gts = Variable(gts)
        out = unet(imgs)
        loss = criterion(out,gts)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        dice += evaluation.get_DC(out, gts)
        if epoch % 100 == 0:
            Dice = dice / 100
            print('训练次数：{},Dice系数{}'.format(epoch, Dice))
        dice = 0
        if epoch >= 40000:
            adjust_learning_rate(optimizer,lr)
        #     masks = out.data.cpu().numpy()
        #     images = imgs.data.cpu().numpy()
        #     gts = gts.data.cpu().numpy()
        #     for mask in masks:
        #         mask = np.transpose(mask,[1,2,0])
        #         cv2.imwrite('img/{}_predict_mask.jpg'.format(cout1),mask)
        #         cout1 += 1
        #     for img in images:
        #         img = np.transpose(img,[1,2,0])
        #         cv2.imwrite('img/{}.jpg'.format(cout2),img)
        #         cout2 += 1
        #     for mask in gts:
        #         mask = np.transpose(mask,[1,2,0])
        #         cv2.imwrite('img/real/{}_real_mask.jpg'.format(cout3),mask)
        #         cout3 += 1
    # 保存
    torch.save(unet, 'u_net.pkl')  # save entire net
    torch.save(unet.state_dict(), 'u_net_params.pkl')  # save parameters
