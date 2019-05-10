from Unet import Unet
from Sample import Sample
import torch
from torch.autograd import Variable
import numpy as np
import cv2


if __name__ == '__main__':
    unet = Unet(1,1)
    if torch.cuda.is_available():
        unet = unet.cuda()
    unet.load_state_dict(torch.load('unet_params.pkl'))
    sample = Sample()
    cout1 = 0
    cout2 = 0
    for epoch in range(100):
        imgs,gts = sample.get_batch(4)
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
        masks = out.data.cpu().numpy()
        images = imgs.data.cpu().numpy()
        for mask in masks:
            mask = np.transpose(mask, [1, 2, 0])
            cv2.imwrite('image_test/{}_predict_mask.jpg'.format(cout1), mask)
            cout1 += 1
        for img in images:
            img = np.transpose(img, [1, 2, 0])
            cv2.imwrite('image_test/{}.jpg'.format(cout2), img)
            cout2 += 1
