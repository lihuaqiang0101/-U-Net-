# import PIL.Image as Image
# import os
# from torchvision import transforms as transforms
#
# datasets = os.listdir('train/Image')
# count = len(datasets)
# datasets.sort(key=lambda x:int(x[:-4]))
# GTs = os.listdir('train/GT')
# GTs.sort(key=lambda x:int(x[:-4]))
# for i in range(len(datasets)):
#     imagepath = os.path.join('train/Image',datasets[i])
#     gtpath = os.path.join('train/GT', GTs[i])
#     outfile1 = 'train/Image'
#     outfile2 = 'train/GT'
#     im1 = Image.open(imagepath)
#     im2 = Image.open(gtpath)
#
#     # 随机水平/垂直翻转
#     new_im1 = transforms.RandomHorizontalFlip(p=1)(im1)  # p表示概率
#     new_im2 = transforms.RandomHorizontalFlip(p=1)(im2)  # p表示概率
#     new_im1.save(os.path.join(outfile1, '{}.png'.format(count)))  # 将水平翻转的CT图像保存下来
#     new_im2.save(os.path.join(outfile2, '{}.png'.format(count)))  # 将水平翻转的mask图像保存下来
#     count += 1#同步保存完一次后将图片数量加一
#     new_im1_1 = transforms.RandomVerticalFlip(p=1)(im1)#将原来的CT图像做垂直翻转
#     new_im2_1 = transforms.RandomVerticalFlip(p=1)(im2)  # 将原来的mask图像做垂直翻转
#     new_im1_1.save(os.path.join(outfile1, '{}.png'.format(count)))
#     new_im2_1.save(os.path.join(outfile2, '{}.png'.format(count)))
#     count += 1
#     new_im1_2 = transforms.RandomVerticalFlip(p=1)(new_im1_1)#将水平翻转以后的CT图像再垂直翻转
#     new_im2_2 = transforms.RandomVerticalFlip(p=1)(new_im2_1)  # 将水平翻转以后的mask图像再垂直翻转
#     new_im1_2.save(os.path.join(outfile1, '{}.png'.format(count)))
#     new_im2_2.save(os.path.join(outfile2, '{}.png'.format(count)))
#     count += 1
#
#     # 随机角度旋转
#     new_im1_3 = transforms.RandomRotation(45)(im1)  # 对原CT图像随机旋转45度
#     new_im2_3 = transforms.RandomRotation(45)(im2)  # 对原mask图像随机旋转45度
#     new_im1_3.save(os.path.join(outfile1, '{}.png'.format(count)))
#     new_im2_3.save(os.path.join(outfile2, '{}.png'.format(count)))
#     count += 1
#     new_im1_4 = transforms.RandomRotation(45)(new_im1)  # 对原CT图像水平翻转以后的图像随机旋转45度
#     new_im2_4 = transforms.RandomRotation(45)(new_im2)  # 对原mask图像水平翻转以后的图像随机旋转45度
#     new_im1_4.save(os.path.join(outfile1, '{}.png'.format(count)))
#     new_im2_4.save(os.path.join(outfile2, '{}.png'.format(count)))
#     count += 1
#     new_im1_5 = transforms.RandomRotation(45)(new_im1_1)  # 对原CT图像垂直翻转以后的图像随机旋转45度
#     new_im2_5 = transforms.RandomRotation(45)(new_im2_1)  # 对原mask图像垂直翻转以后的图像随机旋转45度
#     new_im1_5.save(os.path.join(outfile1, '{}.png'.format(count)))
#     new_im2_5.save(os.path.join(outfile2, '{}.png'.format(count)))
#     count += 1
#     new_im1_6 = transforms.RandomRotation(45)(new_im1_2)  # 对原CT图像水平翻转以后再垂直翻转后的图像随机旋转45度
#     new_im2_6 = transforms.RandomRotation(45)(new_im2_2)  # 对原mask图像水平翻转以后再垂直翻转后的图像随机旋转45度
#     new_im1_6.save(os.path.join(outfile1, '{}.png'.format(count)))
#     new_im2_6.save(os.path.join(outfile2, '{}.png'.format(count)))
#     count += 1
#
#     # 色度、亮度、饱和度、对比度的变化
#     new_im1_7 = transforms.ColorJitter(brightness=1)(im1)
#     new_im1_7 = transforms.ColorJitter(contrast=1)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(saturation=0.5)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(hue=0.5)(new_im1_7)
#     new_im2_7 = transforms.ColorJitter(brightness=1)(im2)
#     new_im2_7 = transforms.ColorJitter(contrast=1)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(saturation=0.5)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(hue=0.5)(new_im2_7)
#     new_im1_7.save(os.path.join(outfile1, '{}.png'.format(count)))#将原CT图像经过一系列变换之后保存下来
#     new_im2_7.save(os.path.join(outfile2, '{}.png'.format(count)))#将原mask图像经过一系列变换之后保存下来
#     count += 1
#
#     new_im1_7 = transforms.ColorJitter(brightness=1)(new_im1)
#     new_im1_7 = transforms.ColorJitter(contrast=1)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(saturation=0.5)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(hue=0.5)(new_im1_7)
#     new_im2_7 = transforms.ColorJitter(brightness=1)(new_im2)
#     new_im2_7 = transforms.ColorJitter(contrast=1)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(saturation=0.5)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(hue=0.5)(new_im2_7)
#     new_im1_7.save(os.path.join(outfile1, '{}.png'.format(count)))
#     new_im2_7.save(os.path.join(outfile2, '{}.png'.format(count)))
#     count += 1
#
#     new_im1_7 = transforms.ColorJitter(brightness=1)(new_im1_1)
#     new_im1_7 = transforms.ColorJitter(contrast=1)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(saturation=0.5)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(hue=0.5)(new_im1_7)
#     new_im2_7 = transforms.ColorJitter(brightness=1)(new_im2_1)
#     new_im2_7 = transforms.ColorJitter(contrast=1)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(saturation=0.5)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(hue=0.5)(new_im2_7)
#     new_im1_7.save(os.path.join(outfile1, '{}.png'.format(count)))
#     new_im2_7.save(os.path.join(outfile2, '{}.png'.format(count)))
#     count += 1
#
#     new_im1_7 = transforms.ColorJitter(brightness=1)(new_im1_2)
#     new_im1_7 = transforms.ColorJitter(contrast=1)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(saturation=0.5)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(hue=0.5)(new_im1_7)
#     new_im2_7 = transforms.ColorJitter(brightness=1)(new_im2_2)
#     new_im2_7 = transforms.ColorJitter(contrast=1)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(saturation=0.5)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(hue=0.5)(new_im2_7)
#     new_im1_7.save(os.path.join(outfile1, '{}.png'.format(count)))
#     new_im2_7.save(os.path.join(outfile2, '{}.png'.format(count)))
#     count += 1
#
#     new_im1_7 = transforms.ColorJitter(brightness=1)(new_im1_3)
#     new_im1_7 = transforms.ColorJitter(contrast=1)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(saturation=0.5)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(hue=0.5)(new_im1_7)
#     new_im2_7 = transforms.ColorJitter(brightness=1)(new_im2_3)
#     new_im2_7 = transforms.ColorJitter(contrast=1)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(saturation=0.5)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(hue=0.5)(new_im2_7)
#     new_im1_7.save(os.path.join(outfile1, '{}.png'.format(count)))
#     new_im2_7.save(os.path.join(outfile2, '{}.png'.format(count)))
#     count += 1
#
#     new_im1_7 = transforms.ColorJitter(brightness=1)(new_im1_4)
#     new_im1_7 = transforms.ColorJitter(contrast=1)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(saturation=0.5)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(hue=0.5)(new_im1_7)
#     new_im2_7 = transforms.ColorJitter(brightness=1)(new_im2_4)
#     new_im2_7 = transforms.ColorJitter(contrast=1)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(saturation=0.5)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(hue=0.5)(new_im2_7)
#     new_im1_7.save(os.path.join(outfile1, '{}.png'.format(count)))
#     new_im2_7.save(os.path.join(outfile2, '{}.png'.format(count)))
#     count += 1
#
#     new_im1_7 = transforms.ColorJitter(brightness=1)(new_im1_5)
#     new_im1_7 = transforms.ColorJitter(contrast=1)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(saturation=0.5)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(hue=0.5)(new_im1_7)
#     new_im2_7 = transforms.ColorJitter(brightness=1)(new_im2_5)
#     new_im2_7 = transforms.ColorJitter(contrast=1)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(saturation=0.5)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(hue=0.5)(new_im2_7)
#     new_im1_7.save(os.path.join(outfile1, '{}.png'.format(count)))
#     new_im2_7.save(os.path.join(outfile2, '{}.png'.format(count)))
#     count += 1
#
#     new_im1_7 = transforms.ColorJitter(brightness=1)(new_im1_6)
#     new_im1_7 = transforms.ColorJitter(contrast=1)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(saturation=0.5)(new_im1_7)
#     new_im1_7 = transforms.ColorJitter(hue=0.5)(new_im1_7)
#     new_im2_7 = transforms.ColorJitter(brightness=1)(new_im2_6)
#     new_im2_7 = transforms.ColorJitter(contrast=1)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(saturation=0.5)(new_im2_7)
#     new_im2_7 = transforms.ColorJitter(hue=0.5)(new_im2_7)
#     new_im1_7.save(os.path.join(outfile1, '{}.png'.format(count)))
#     new_im2_7.save(os.path.join(outfile2, '{}.png'.format(count)))
#     count += 1

import PIL.Image as Image
import os
from torchvision import transforms as transforms

datasets = os.listdir('tumour')
ying = 1795
yang = 1746
# datasets.sort(key=lambda x:int(x[:-4]))
for data in datasets:
    img = Image.open('tumour/'+data)
#     # 随机水平/垂直翻转
    new_img = transforms.RandomHorizontalFlip(p=1)(img)  # p表示概率
    if data[0] == '0':
        new_img.save(os.path.join('tumour', '0_{}.png'.format(ying)))  # 将水平翻转的CT图像保存下来
        print(new_img)
        ying += 1
    elif data[0] == '1':
        new_img.save(os.path.join('tumour', '1_{}.png'.format(yang)))  # 将水平翻转的CT图像保存下来
        print(new_img)
        yang += 1
    new_img_1 = transforms.RandomVerticalFlip(p=1)(img)#将原来的CT图像做垂直翻转
    if data[0] == '0':
        new_img_1.save(os.path.join('tumour', '0_{}.png'.format(ying)))  # 将水平翻转的CT图像保存下来
        ying += 1
    elif data[0] == '1':
        new_img_1.save(os.path.join('tumour', '1_{}.png'.format(yang)))  # 将水平翻转的CT图像保存下来
        yang += 1
    new_img_2 = transforms.RandomVerticalFlip(p=1)(new_img_1)#将水平翻转以后的CT图像再垂直翻转
    if data[0] == '0':
        new_img_2.save(os.path.join('tumour', '0_{}.png'.format(ying)))  # 将水平翻转的CT图像保存下来
        ying += 1
    elif data[0] == '+':
        new_img_2.save(os.path.join('tumour', '1_{}.png'.format(yang)))  # 将水平翻转的CT图像保存下来
        yang += 1
#
#     # 随机角度旋转
    new_img_3 = transforms.RandomRotation(45)(img)  # 对原CT图像随机旋转45度
    if data[0] == '0':
        new_img_3.save(os.path.join('tumour', '0_{}.png'.format(ying)))  # 将水平翻转的CT图像保存下来
        ying += 1
    elif data[0] == '1':
        new_img_3.save(os.path.join('tumour', '1_{}.png'.format(yang)))  # 将水平翻转的CT图像保存下来
        yang += 1
    new_img_4 = transforms.RandomRotation(45)(new_img)  # 对原CT图像水平翻转以后的图像随机旋转45度
    if data[0] == '0':
        new_img_4.save(os.path.join('tumour', '0_{}.png'.format(ying)))  # 将水平翻转的CT图像保存下来
        ying += 1
    elif data[0] == '1':
        new_img_4.save(os.path.join('tumour', '1_{}.png'.format(yang)))  # 将水平翻转的CT图像保存下来
        yang += 1
    new_img_5 = transforms.RandomRotation(45)(new_img_1)  # 对原CT图像垂直翻转以后的图像随机旋转45度
    if data[0] == '0':
        new_img_5.save(os.path.join('tumour', '0_{}.png'.format(ying)))  # 将水平翻转的CT图像保存下来
        ying += 1
    elif data[0] == '1':
        new_img_5.save(os.path.join('tumour', '1_{}.png'.format(yang)))  # 将水平翻转的CT图像保存下来
        yang += 1
    new_img_6 = transforms.RandomRotation(45)(new_img_2)  # 对原CT图像水平翻转以后再垂直翻转后的图像随机旋转45度
    if data[0] == '0':
        new_img_6.save(os.path.join('tumour', '0_{}.png'.format(ying)))  # 将水平翻转的CT图像保存下来
        ying += 1
    elif data[0] == '1':
        new_img_6.save(os.path.join('tumour', '1_{}.png'.format(yang)))  # 将水平翻转的CT图像保存下来
        yang += 1
#
#     # 色度、亮度、饱和度、对比度的变化
    new_img_7 = transforms.ColorJitter(brightness=1)(img)
    new_img_7 = transforms.ColorJitter(contrast=1)(new_img_7)
    new_img_7 = transforms.ColorJitter(saturation=0.5)(new_img_7)
    new_img_7 = transforms.ColorJitter(hue=0.5)(new_img_7)
    if data[0] == '0':
        new_img_7.save(os.path.join('tumour', '0_{}.png'.format(ying)))  # 将水平翻转的CT图像保存下来
        ying += 1
    elif data[0] == '1':
        new_img_7.save(os.path.join('tumour', '1_{}.png'.format(yang)))  # 将水平翻转的CT图像保存下来
        yang += 1
#
    new_img_7 = transforms.ColorJitter(brightness=1)(new_img_1)
    new_img_7 = transforms.ColorJitter(contrast=1)(new_img_7)
    new_img_7 = transforms.ColorJitter(saturation=0.5)(new_img_7)
    new_img_7 = transforms.ColorJitter(hue=0.5)(new_img_7)
    if data[0] == '0':
        new_img_7.save(os.path.join('tumour', '0_{}.png'.format(ying)))  # 将水平翻转的CT图像保存下来
        ying += 1
    elif data[0] == '1':
        new_img_7.save(os.path.join('tumour', '1_{}.png'.format(yang)))  # 将水平翻转的CT图像保存下来
        yang += 1
#
    new_img_7 = transforms.ColorJitter(brightness=1)(new_img_2)
    new_img_7 = transforms.ColorJitter(contrast=1)(new_img_7)
    new_img_7 = transforms.ColorJitter(saturation=0.5)(new_img_7)
    new_img_7 = transforms.ColorJitter(hue=0.5)(new_img_7)
    if data[0] == '0':
        new_img_7.save(os.path.join('tumour', '0_{}.png'.format(ying)))  # 将水平翻转的CT图像保存下来
        ying += 1
    elif data[0] == '1':
        new_img_7.save(os.path.join('tumour', '1_{}.png'.format(yang)))  # 将水平翻转的CT图像保存下来
        yang += 1
#
    new_img_7 = transforms.ColorJitter(brightness=1)(new_img_3)
    new_img_7 = transforms.ColorJitter(contrast=1)(new_img_7)
    new_img_7 = transforms.ColorJitter(saturation=0.5)(new_img_7)
    new_img_7 = transforms.ColorJitter(hue=0.5)(new_img_7)
    if data[0] == '0':
        new_img_7.save(os.path.join('tumour', '0_{}.png'.format(ying)))  # 将水平翻转的CT图像保存下来
        ying += 1
    elif data[0] == '1':
        new_img_7.save(os.path.join('tumour', '1_{}.png'.format(yang)))  # 将水平翻转的CT图像保存下来
        yang += 1
#
    new_img_7 = transforms.ColorJitter(brightness=1)(new_img_4)
    new_img_7 = transforms.ColorJitter(contrast=1)(new_img_7)
    new_img_7 = transforms.ColorJitter(saturation=0.5)(new_img_7)
    new_img_7 = transforms.ColorJitter(hue=0.5)(new_img_7)
    if data[0] == '0':
        new_img_7.save(os.path.join('tumour', '0_{}.png'.format(ying)))  # 将水平翻转的CT图像保存下来
        ying += 1
    elif data[0] == '1':
        new_img_7.save(os.path.join('tumour', '1_{}.png'.format(yang)))  # 将水平翻转的CT图像保存下来
        yang += 1
#
    new_img_7 = transforms.ColorJitter(brightness=1)(new_img_5)
    new_img_7 = transforms.ColorJitter(contrast=1)(new_img_7)
    new_img_7 = transforms.ColorJitter(saturation=0.5)(new_img_7)
    new_img_7 = transforms.ColorJitter(hue=0.5)(new_img_7)
    if data[0] == '0':
        new_img_7.save(os.path.join('tumour', '0_{}.png'.format(ying)))  # 将水平翻转的CT图像保存下来
        ying += 1
    elif data[0] == '1':
        new_img_7.save(os.path.join('tumour', '1_{}.png'.format(yang)))  # 将水平翻转的CT图像保存下来
        yang += 1
#
    new_img_7 = transforms.ColorJitter(brightness=1)(new_img_6)
    new_img_7 = transforms.ColorJitter(contrast=1)(new_img_7)
    new_img_7 = transforms.ColorJitter(saturation=0.5)(new_img_7)
    new_img_7 = transforms.ColorJitter(hue=0.5)(new_img_7)
    if data[0] == '0':
        new_img_7.save(os.path.join('tumour', '0_{}.png'.format(ying)))  # 将水平翻转的CT图像保存下来
        ying += 1
    elif data[0] == '1':
        new_img_7.save(os.path.join('tumour', '1_{}.png'.format(yang)))  # 将水平翻转的CT图像保存下来
        yang += 1
