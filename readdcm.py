# coding:utf-8
import SimpleITK as sitk
import cv2
import os

# LKDS-00058,-102.655469971,108.188810974,438.759994507,12.2279986879
def dcmtopng(filename,outpath,data):
    # filename = "10001.dcm"
    ds = sitk.ReadImage(filename)
    img_array = sitk.GetArrayFromImage(ds)
    frame_num, width, height = img_array.shape

    # index = -1
    for img_item in img_array:
        # index = index + 1
        cv2.imwrite("%s/%s.png" % (outpath,data.split('.')[0]), img_item)

for i in range(1109,1129):
    dirs = os.listdir('/home/lhq/桌面/B 题：直肠癌淋巴结转移的智能诊断/B题-测试数据/数据集2/{}'.format(i))
    for dir in dirs:
        datasets = os.path.join('/home/lhq/桌面/B 题：直肠癌淋巴结转移的智能诊断/B题-测试数据/数据集2/{}'.format(i),dir)
        imagepaths = os.listdir(datasets)
        for imagepath in imagepaths:
            dcmtopng(os.path.join(datasets,imagepath), os.path.join('/home/lhq/桌面/B 题：直肠癌淋巴结转移的智能诊断/B题-测试数据/数据集3/{}'.format(i),dir), imagepath)

# datasets = os.listdir('/home/lhq/桌面/B 题：直肠癌淋巴结转移的智能诊断/B题-测试数据/数据集2')
# for dataset in datasets:
#     imagepath = os.path.join('train/image',dataset)
    # dcmtopng(imagepath,'train/Image',dataset)
    # for dir in dirs:
    #     if dir == 'arterial phase':
    #         datas = os.listdir('../B题-全部数据/数据集1/'+dataset+'/'+dir)
    #         for data in datas:
    #             if 'dcm' in data:
    #                 dcmtopng('../B题-全部数据/数据集1/'+dataset+'/'+dir+'/'+data,'../B题-全部数据/数据集2/'+dataset+'/'+'arterial phase',data)
    #     else:
    #         datas = os.listdir('../B题-全部数据/数据集1/' + dataset + '/' + dir)
    #         for data in datas:
    #             if 'dcm' in data:
    #                 dcmtopng('../B题-全部数据/数据集1/'+dataset+'/'+dir+'/'+data,'../B题-全部数据/数据集2/'+dataset+'/'+'venous phase',data)
